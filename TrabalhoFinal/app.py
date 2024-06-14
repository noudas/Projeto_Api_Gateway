from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import uuid #Biblioteca para criar um codigo unico por cliente


app = Flask(__name__)
CORS(app)

DATABASE = "api_gateway_projeto.db"

def get_db_connection():
    return sqlite3.connect(DATABASE)

def recreate_tables():
    conn = get_db_connection()
    with conn:
        c = conn.cursor()
        c.execute('DROP TABLE IF EXISTS Cliente')
        c.execute('DROP TABLE IF EXISTS Endereco')
        # Tabela Cliente
        c.execute('''CREATE TABLE IF NOT EXISTS Cliente (
                            id INTEGER PRIMARY KEY,
                            codigo TEXT UNIQUE,
                            nome TEXT NOT NULL);''')
        # Tabela Endereço
        c.execute('''CREATE TABLE IF NOT EXISTS Endereco (
                            id INTEGER PRIMARY KEY,
                            cliente_id INTEGER,
                            logradouro TEXT NOT NULL,
                            numero INTEGER,
                            complemento TEXT,
                            cidade TEXT NOT NULL,
                            estado TEXT NOT NULL,
                            cep TEXT NOT NULL,
                            FOREIGN KEY(cliente_id) REFERENCES Cliente(id));''')


# Executando a função para limpar e recriar as tabelas
recreate_tables()


#Criar Cliente
@app.route('/api/v1/cliente', methods=['POST'])
def criar_cliente():
    cliente = request.json
    if 'nome' in cliente:
        codigo = str(uuid.uuid4())  # Gerando um código UUID único
        conn = get_db_connection()
        try:
            with conn:
                c = conn.cursor()
                c.execute('INSERT INTO Cliente (codigo, nome) VALUES (?, ?)', (codigo, cliente['nome']))
                cliente_id = c.lastrowid
                conn.commit()
        finally:
            conn.close()
        cliente['id'] = cliente_id
        cliente['codigo'] = codigo
        return jsonify(cliente), 201
    else:
        return jsonify({'error': 'O JSON enviado não contém o campo "nome"'}), 400


#Pegar Cliente Via ID
@app.route('/api/v1/cliente/<int:id>', methods=['GET'])
def obter_cliente(id):
    conn = get_db_connection()
    try:
        with conn:
            c = conn.cursor()
            c.execute('SELECT * FROM Cliente WHERE id=?', (id,))
            cliente = c.fetchone()
            if cliente:
                return jsonify({'id': cliente[0], 'codigo': cliente[1], 'nome': cliente[2]}), 200
            else:
                return jsonify({'message': 'Cliente não encontrado'}), 404
    finally:
        conn.close()


#PEgar Lista de todos os Clientes
@app.route('/api/v1/cliente', methods=['GET'])
def listar_clientes():
    conn = get_db_connection()
    try:
        with conn:
            c = conn.cursor()
            c.execute('SELECT * FROM Cliente')
            clientes = [{'id': row[0], 'codigo': row[1], 'nome': row[2]} for row in c.fetchall()]
            return jsonify(clientes), 200
    finally:
        conn.close()



#Criar Endereco a partir do id do cliente
@app.route('/api/v1/cliente/<int:id>/endereco', methods=['POST'])
def criar_endereco(id):
    endereco = request.json
    required_fields = ['logradouro', 'cidade', 'estado', 'cep']
    if all(field in endereco for field in required_fields):
        conn = get_db_connection()
        try:
            with conn:
                c = conn.cursor()
                c.execute('INSERT INTO Endereco (cliente_id, logradouro, numero, complemento, cidade, estado, cep) VALUES (?, ?, ?, ?, ?, ?, ?)',
                          (id, endereco['logradouro'], endereco.get('numero'), endereco.get('complemento'), endereco['cidade'], endereco['estado'], endereco['cep']))
                endereco_id = c.lastrowid
                conn.commit()
        finally:
            conn.close()
        endereco['id'] = endereco_id
        endereco['cliente_id'] = id
        return jsonify(endereco), 201
    else:
        return jsonify({'error': 'O JSON enviado não contém todos os campos necessários'}), 400


# Listar o Endereco a partir do id do cliente
@app.route('/api/v1/cliente/<int:id>/endereco', methods=['GET'])
def listar_enderecos_por_cliente(id):
    conn = get_db_connection()
    try:
        with conn:
            c = conn.cursor()
            c.execute('SELECT * FROM Endereco WHERE cliente_id=?', (id,))
            enderecos = [{'id': row[0], 'cliente_id': row[1], 'logradouro': row[2], 'cidade': row[3], 'estado': row[4], 'cep': row[5]} for row in c.fetchall()]
            return jsonify(enderecos), 200
    finally:
        conn.close()


#Erro 500
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Erro interno do servidor'}), 500

if __name__ == '__main__':
    app.run(debug=True)
