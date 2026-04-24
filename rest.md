## O que é REST?

Representational State Transfer (Transferência de estado representacional)

## Os 6 princípios do REST

----

### 1. Cliente-Servidor

Cliente e servidor são INDEPENDENTES.

Ex: Pizzaria

- Cliente vai fazer o pedido
- Cozinha vai preparar
- Eles não precisam saber como o outro funciona

No mundo dev:
- Front-end faz a requisição
- Back-end responde

----

### 2. Stateless (Sem estado)

O servidor **não guarda informações de requisições anteriores**.

Cada requisição PRECISA conter **todas as informações necessárias**.

Ex: Também pizzaria

- Cada pedido deve conter todos os detalhes
- Não se importa com o que foi pedido anteriormente

----

### 3. Cache

As respostas **PODEM** ser armazenadas para reutilização.

Ex:

- Você pergunta ao vizinho sobre o trânsito
- Ele confere, responde
- Se eu perguntar novamente depois, ele pode reutilizar a resposta

----

### 4. Interface Uniforme (Coração do REST)

- Devem seguir um contrato padronizado.
- Métodos HTTP têm um significado claro
- Respostas são padronizadas (Ex: 404(not found), 200(ok), 500(Erro interno de servidor))

- Get -> Buscar
- Post -> Criar
- Put -> Atualizar
- Delete -> Apagar

/buscarPedido seria errado pois fica redundant, pois o GET já nos informa que será uma busca

/pedidos ok, pois o verbo já está embutido no método HTTP.

----

### 5. Sistema em Camadas

O cliente **não sabe o que acontece entre ele e o servidor**.

Pode haver:
- Load balancer
- Firewall
- Cache

O que importa é que a resposta chegue.

----

### 6. Código sob Demanda

O servidor PODE enviar código para o cliente executar.

Ex: HTML, css, js.

pip install fastapi
pip install uvicorn

uvicorn main:app --reload



curl -X POST -H "Content-Type: application/json" "http://127.0.0.1:8000/items?item=chapeu"


GET (buscar/id_item)
curl -X GET -H "Content-Type: application/json" "http://127.0.0.1:8000/items/0"


Essa chamada será para os itens de 0 a limite(parâmetro que passamos) ?queryParam
GET (Buscar)
curl -X GET -H "Content-Type: application/json" "http://127.0.0.1:8000/items?limite=3"


PUT (Atualizar)
curl -X PUT -H "Content-Type: application/json" "http://127.0.0.1:8000/items/0?new_item=sapato"


Delete (Apagar)
curl -X DELETE -H "Content-Type: application/json" "http://127.0.0.1:8000/items/0"

