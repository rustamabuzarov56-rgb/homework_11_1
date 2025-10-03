import json
from typing import Any


def get_transaction_data(path: str) -> Any:
    """Функция принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            transaction = json.load(f)
        return transaction
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
    except TypeError:
        return []
