import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(list_dict):
    assert filter_by_state(list_dict, state="EXECUTED") == (
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
    )


def test_filter_by_state_canceled(list_dict):
    assert filter_by_state(list_dict, state="CANCELED") == (
        [
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )


def test_filter_by_state_error(list_dict_2):
    with pytest.raises(KeyError):
        filter_by_state(list_dict_2)


def test_sort_by_date_descending(list_dict):
    assert sort_by_date(list_dict) == (
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
    )


def test_sort_by_date_ascending(list_dict):
    assert sort_by_date(list_dict, sort_order=False) == (
        [
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        ]
    )


def test_sort_by_date_same(same_dates):
    assert sort_by_date(same_dates) == (
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        ]
    )


def test_sort_by_date(non_standard_date):
    assert sort_by_date(non_standard_date) == [
        {"id": 594226727, "state": "CANCELED", "date": "T21:27:25.241689.2018-09-12"},
        {"id": 41428829, "state": "EXECUTED", "date": "T18:35:29.512364.2019-0-03"},
        {"id": 615064591, "state": "CANCELED", "date": "T08:21:33.419441.2018-10-14"},
        {"id": 939719570, "state": "EXECUTED", "date": "T02:08:58.425572.2018-06-30"},
    ]
