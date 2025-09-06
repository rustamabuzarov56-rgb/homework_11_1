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

@pytest.fixture
def list_dict():
    return ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])

@pytest.fixture
def list_dict_2():
    return ([{'id': 41428829, 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727,  'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'date': '2018-10-14T08:21:33.419441'}])

@pytest.fixture
def same_dates():
    return ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])

@pytest.fixture
def non_standard_date():
    return ([{'id': 41428829, 'state': 'EXECUTED', 'date': 'T18:35:29.512364.2019-0-03'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': 'T02:08:58.425572.2018-06-30'},
            {'id': 594226727, 'state': 'CANCELED', 'date': 'T21:27:25.241689.2018-09-12'},
            {'id': 615064591, 'state': 'CANCELED', 'date': 'T08:21:33.419441.2018-10-14'}])