import pytest

@pytest.fixture
def card_type():
    return "Visa Platinum 7000792289606361"

@pytest.fixture
def account_number():
    return "Счет 73654108430135874305"

@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"

@pytest.fixture
def date_missing():
    return " "

@pytest.fixture
def short_date():
    return "2024-03-11T02"

