
# Desafio Backend na MaisTODOS

## Descrição
O desafio proposto é a criação de uma API intermediária, na qual receberá os dados do produto,
comprador e valor total, fará todo o controle da aplicação e  enviará para uma API externa
o valor do cashback, que retornará o benefício do cashback para o cliente.


## Intalação e Dependências

### Requisitos
1. Docker
2. Docker Compose

## Configurar a aplicação para rodar localmente:
Clone o repositório para criar uma cópia local no seu computador 

	``git clone https://github.com/mairaafreitas/backend-python-wallet.git``

## Inicialização
1. Abra o diretório clonado no terminal

1. O docker precisa preparar as imagens declaradas no repositório, criando os containers e inicializando-os,
para isso, utilize o comando:
   
	``docker-compose up``
   
3. Para que a estrutura do banco de dados seja criada dentro do container, execute o comando:
	
    ``docker-compose run web python manage.py migrate``
   
4. Crie o seu usuário para acessar o painel administrativo
   
	``docker-compose run web python manage.py createsuperuser``
   
5. Para verificar se está funcionando, acesse o painel administrativo
   
	``localhost:8000/admin ``
   
6. Ao acessar o painel, é necessário criar um usuário e senha, que será usado na api para obter um token 

![create user](./docs/create-user.png)

## Instruções de uso da API
O primeiro acesso à API deverá ser a autenticação do usuário criado no painel administrativo (passo 6 da etapa anterior),
para obtenção de um token, que será utilizado nos acessos posteriores. 
O endpoint (POST /login) 
espera os campos username e password e retorna um JSON com a propriedade token.

``POST /login``
![get token](./docs/get-token.png)

Retorno da API:

```
{
    "token": "4hfddaf1832aea98huy74f77d771028c0b3d4397be2"
}
```

Para os demais acessos, a chave retornada acima deve ser inserida no header Authorization da requisição


A api recebe as informações enviadas pelo varejista:

``POST /cashback``


``
Authorization: Token 4hfddaf1832aea98huy74f77d771028c0b3d4397be2
``

```
{
    "sold_at": "2021-09-02 14:00:00",
    "customer": {
       "document": "11111111111",
       "name": "ANA CLAUDIA OLIVEIRA",
    },
    "total": "50.00",
    "products": [
       {
          "type": "A",
          "value": "10.00",
          "qty": 1,
       },
       {
          "type": "B",
          "value": "20.00",
          "qty": 2,
       }
    ],
}
```

Para verificar e testar os recursos que da API, pode-se utilizar uma ferramenta como o [Postman](https://www.postman.com/).

## Autor
* **Maíra Freitas** - [*Backend Developer Junior*](https://github.com/mairaafreitas)