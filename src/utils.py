import json


def get_transaction_data(path: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла
     и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding="utf-8") as file:
            try:
                transaction_data = json.load(file)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
    return transaction_data

print(get_transaction_data("../data/data.json"))


