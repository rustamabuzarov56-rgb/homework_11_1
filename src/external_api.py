import json
from locale import currency

import requests
import os
from dotenv import load_dotenv


load_dotenv()
apikey = os.getenv('API_KEY')


def get_transaction_amount(transactions: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if transactions["operationAmount"]["currency"]["code"] == "RUB":
        return transactions["operationAmount"]["amount"]
    if transactions["operationAmount"]["currency"]["code"] == "USD":
        base = "USD"
        symbols = "RUB"
        headers = {"apikey": apikey}
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}&base={base}"
        response = requests.get(url, headers=headers)
        result = response.json()
        return result["rates"]["RUB"]
    if transactions["operationAmount"]["currency"]["code"] == "EUR":
        base = "EUR"
        symbols = "RUB"
        headers = {"apikey": apikey}
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}&base={base}"
        response = requests.get(url, headers=headers)
        result = response.json()
        return result["rates"]["RUB"]



print(get_transaction_amount({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "EUR"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }))