#!/bin/sh

KONG_GATEWAY_URL="http://localhost:8001"
KONG_GATEWAY_SERVICES_ENDPOINT="${KONG_GATEWAY_URL}/services"
PYTHON_SERVICE="crudpy"
PYTHON_APP_URL="http://localhost:5000"

curl -i -s -X POST "${KONG_GATEWAY_SERVICES_ENDPOINT}" \
  --data name="${PYTHON_SERVICE}" \
  --data url="http://crudpy:5000"

curl -i -X POST "${KONG_GATEWAY_SERVICES_ENDPOINT}"/"${PYTHON_SERVICE}"/routes \
  --data 'paths[]=/mock' \
  --data name=crudpy_route

curl -i -X POST "${PYTHON_APP_URL}"/api/v1/cliente \
  -H "Content-Type: application/json" \
  --data '{"nome": "Joao da Silva"}'

curl -i -X POST "${PYTHON_APP_URL}"/api/v1/cliente \
  -H "Content-Type: application/json" \
  --data '{"nome": "Joselito Neves"}'

curl -i -X POST "${PYTHON_APP_URL}"/api/v1/cliente \
  -H "Content-Type: application/json" \
  --data '{"nome": "Maria Oliveira"}'

curl -i -X POST "${PYTHON_APP_URL}"/api/v1/cliente \
  -H "Content-Type: application/json" \
  --data '{"nome": "Pedro Santos"}'

curl -i -X POST "${PYTHON_APP_URL}"/api/v1/cliente \
  -H "Content-Type: application/json" \
  --data '{"nome": "Ana Costa"}'



curl -i -X POST "${PYTHON_APP_URL}"/api/v1/cliente/1/endereco \
  -H "Content-Type: application/json" \
  --data '{
    "logradouro": "Rua Exemplo",
    "numero": 123,
    "complemento": "Apartamento 101",
    "cidade": "Exemplópolis",
    "estado": "EX",
    "cep": "12345-678"
  }'

  curl -i -X POST "${PYTHON_APP_URL}"/api/v1/cliente/2/endereco \
  -H "Content-Type: application/json" \
  --data '{
    "logradouro": "Avenida das Flores",
    "numero": 456,
    "complemento": "Bloco B, Apartamento 201",
    "cidade": "Floresville",
    "estado": "FL",
    "cep": "98765-432"
  }'

  curl -i -X POST "${PYTHON_APP_URL}"/api/v1/cliente/3/endereco \
  -H "Content-Type: application/json" \
  --data '{
    "logradouro": "Rua dos Empreendedores",
    "numero": 789,
    "complemento": "Loja A",
    "cidade": "Empreendedor City",
    "estado": "EC",
    "cep": "65432-109"
  }'

curl -i -X POST "${PYTHON_APP_URL}"/api/v1/cliente/4/endereco \
  -H "Content-Type: application/json" \
  --data '{
    "logradouro": "Travessa Campo Aberto",
    "numero": 321,
    "complemento": "Fazenda Verde",
    "cidade": "Campo Aberto",
    "estado": "CA",
    "cep": "56789-012"
  }'

curl -i -X POST "${PYTHON_APP_URL}"/api/v1/cliente/5/endereco \
  -H "Content-Type: application/json" \
  --data '{
    "logradouro": "Champs Elysées",
    "numero": 555,
    "complemento": "",
    "cidade": "Paris",
    "estado": "ID", 
    "cep": "75008"
  }'
