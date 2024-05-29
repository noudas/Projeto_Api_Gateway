from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

clientes = []
enderecos = []

@app.route('/api/v1/cliente', methods=['POST'])
def criar_cliente():
    cliente = request.json
    cliente['id'] = len(clientes) + 1
    clientes.append(cliente)
    return jsonify(cliente), 201

@app.route('/api/v1/cliente/<int:id>', methods=['GET'])
def obter_cliente(id):
    cliente = next((cli for cli in clientes if cli["id"] == id), None)
    if cliente:
        return jsonify(cliente), 200
    else:
        return jsonify({'message': 'Cliente não encontrado'}), 404

@app.route('/api/v1/cliente', methods=['GET'])
def listar_clientes():
    return jsonify(clientes), 200

@app.route('/api/v1/cliente/<int:id>/endereco', methods=['POST'])
def criar_endereco(id):
    endereco = request.json
    endereco['id'] = len(enderecos) + 1
    endereco['cliente_id'] = id
    enderecos.append(endereco)
    return jsonify(endereco), 201

@app.route('/api/v1/cliente/<int:id>/endereco', methods=['GET'])
def listar_enderecos_por_cliente(id):
    enderecos_filtrados = [end for end in enderecos if end["cliente_id"] == id]
    return jsonify(enderecos_filtrados), 200

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Algo de errado não está certo'}), 500

if __name__ == '__main__':
    app.run(debug=True)
