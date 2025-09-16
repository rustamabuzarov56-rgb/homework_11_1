import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

def test_filter_by_currency_usd(checklist):
    generator = (filter_by_currency(checklist, "USD"))
    assert next(generator)   == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    assert next(generator) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }

def test_filter_by_currency_rub(checklist):
    generator = (filter_by_currency(checklist, "RUB"))
    assert next(generator) == {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    assert next(generator) == {
           "id": 594226727,
           "state": "CANCELED",
           "date": "2018-09-12T21:27:25.241689",
           "operationAmount": {
            "amount": "67314.70",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
           },
           "description": "Перевод организации",
           "from": "Visa Platinum 1246377376343588",
           "to": "Счет 14211924144426031657"
           }

def test_transaction_descriptions(checklist):
    generator = (transaction_descriptions(checklist))
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"

def test_transaction_descriptions_cut(transactions_list_cut):
    result = list(transaction_descriptions(transactions_list_cut))
    assert len(result) == 2

def test_descriptions_empty_list(empty_list):
    result = list(transaction_descriptions(empty_list))
    assert result == []

def test_card_number_generator(card_number):
    generator = card_number_generator(1, 5)
    assert list(generator) == card_number

    generator = card_number_generator(1, 1)
    assert next(generator) == "0000 0000 0000 0001"

    generator = card_number_generator(1234567890123456, 1234567890123456)
    assert next(generator) == "1234 5678 9012 3456"

    generator = card_number_generator(0, 0)
    assert next(generator) == "0000 0000 0000 0000"

    generator = card_number_generator(9999999999999999, 9999999999999999)
    assert next(generator) == "9999 9999 9999 9999"
