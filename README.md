# Projeto_Api_Gateway
Projeto FullStack API Gateway - Python Flask


# API Gateway Projeto

Este é um projeto de exemplo que demonstra a criação de uma API simples usando Flask e SQLite, encapsulado em um contêiner Docker.

## Requisitos

- Docker
- Postman (opcional, para testar a API)

## Configuração do Ambiente

Certifique-se de ter o Docker instalado em sua máquina.

## Executando a Aplicação

1. Clone este repositório:

    ```bash
    git clone https://github.com/noudas/api-gateway-projeto.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd api-gateway-projeto
    ```

3. Rodar todos os serviços:

    ```bash
    docker compose up
    ```
    
4. Depois do Kong Api Gateway for incializado:

    ```bash
    ./kong-config.sh
    ```

O servidor estará em execução em `http://127.0.0.1:5000/`.

## Utilização da API

Você pode usar o Postman ou qualquer outra ferramenta para testar a API. Aqui estão alguns exemplos de endpoints:

### Criar Cliente

- **Método:** POST
- **URL:** http://127.0.0.1:5000/api/v1/cliente
- **Corpo da Solicitação:**
    ```json
    {
        "nome": "João Silva"
    }
    ```
- **Resposta de Exemplo:**
    ```json
    {
        "codigo": "c368bad5-95bc-48f5-938b-b5d98933bffd",
        "id": 1,
        "nome": "João Silva"
    }
    ```

### Obter Cliente

- **Método:** GET
- **URL:** http://127.0.0.1:5000/api/v1/cliente/{id}
- **Resposta de Exemplo:**
    ```json
    {
        "id": 1,
        "codigo": "c368bad5-95bc-48f5-938b-b5d98933bffd",
        "nome": "João Silva"
    }
    ```

### Listar Clientes

- **Método:** GET
- **URL:** http://127.0.0.1:5000/api/v1/cliente
- **Resposta de Exemplo:**
    ```json
    [
        {
            "id": 1,
            "codigo": "c368bad5-95bc-48f5-938b-b5d98933bffd",
            "nome": "João Silva"
        }
    ]
    ```

### Criar Endereço para Cliente

- **Método:** POST
- **URL:** http://127.0.0.1:5000/api/v1/cliente/{id}/endereco
- **Corpo da Solicitação:**
    ```json
    {
        "logradouro": "Rua Exemplo",
        "numero": 123,
        "complemento": "Apartamento 101",
        "cidade": "Exemplópolis",
        "estado": "EX",
        "cep": "12345-678"
    }
    ```
- **Resposta de Exemplo:**
    ```json
    {
        "id": 1,
        "cliente_id": 1,
        "logradouro": "Rua Exemplo",
        "cidade": "Exemplópolis",
        "estado": "EX",
        "cep": "12345-678"
    }
    ```

### Listar Endereços por Cliente

- **Método:** GET
- **URL:** http://127.0.0.1:5000/api/v1/cliente/{id}/endereco
- **Resposta de Exemplo:**
    ```json
    [
        {
            "id": 1,
            "cliente_id": 1,
            "logradouro": "Rua Exemplo",
            "cidade": "Exemplópolis",
            "estado": "EX",
            "cep": "12345-678"
        }
    ]
    ```

## Observações

- Todos os exemplos de URLs são para execução local. Certifique-se de substituir `http://127.0.0.1:5000/` pelo host correto se estiver implantando a API em um servidor remoto.
- Este projeto usa SQLite como banco de dados para simplificar a configuração. Para ambientes de produção, considere usar um banco de dados mais robusto, como PostgreSQL ou MySQL.
