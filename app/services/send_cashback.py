import requests

MAISTODOS_ENDPOINT = 'https://5efb30ac80d8170016f7613d.mockapi.io/api/mock/Cashback'


def customer_cashback(document, cashback):
    data = {
        "document": document,
        "cashback": cashback
    }
    response = requests.post(url=MAISTODOS_ENDPOINT, params=data)
    print(response.text)

