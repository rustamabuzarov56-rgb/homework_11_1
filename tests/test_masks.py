import pytest

from src.masks import get_mask_card_number, get_mask_account
from tests.conftest import account_number_2

@pytest.mark.parametrize("card_num, expected_result", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("70007922896063611", "Номер карты должен состоять из 16 цифр"),
    (" ", "Номер карты должен состоять из 16 цифр")
])

def test_get_mask_card_number(card_num, expected_result):
    assert get_mask_card_number(card_num) == expected_result

@pytest.mark.parametrize("account, expected_result", [
     ("73654108430135874305", "**4305"),
     ("173654108430135874305", "Номер счета должен состоять из 20 цифр"),
     (" ", "Номер счета должен состоять из 20 цифр")
 ])

def test_get_mask_account(account, expected_result):
    assert get_mask_account(account) == expected_result
