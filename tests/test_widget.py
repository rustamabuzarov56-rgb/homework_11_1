import pytest
from src.widget import mask_account_card, get_date

def test_mask_account_card_1(card_type):
    assert mask_account_card(card_type) == "Visa Platinum 7000 79** **** 6361"

def test_mask_account_card_2(account_number):
    assert mask_account_card(account_number) == "Счет **4305"

@pytest.mark.parametrize("type, expected_result", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Счет 35383033474447895560", "Счет **5560")
])

def test_mask_account_card(type, expected_result):
    assert mask_account_card(type) == expected_result

def test_get_date(date):
    assert get_date(date) == "11.03.2024"

def test_get_short_date(short_date):
    assert get_date(short_date) == "11.03.2024"

def test_get_date_missing(date_missing):
    assert get_date(date_missing) == "Дата отсутствует"

