from typing import Any, Iterator


def filter_by_currency(transactions: list[dict], currency: str = "USD") -> Iterator[Any]:
    """Функция возвращаeт итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Генератор который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for i in range(start, end + 1):
        card_number = f"{i:016d}"
        formatting_card_number = " ".join(card_number[i:i + 4] for i in range(0, 16, 4))
        yield formatting_card_number
