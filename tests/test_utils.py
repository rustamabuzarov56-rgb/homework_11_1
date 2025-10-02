import pytest
import json
from src.utils import get_transaction_data

def test_get_transaction_data_1(json_data_1):
    data = json.loads(json_data_1)
    assert data == [{"name": "руб.","code": "RUB"}, {"name": "USD","code": "USD"}]

def test_get_transaction_data_2(json_data_2):
    data = json.loads(json_data_2)
    assert data == {"name": "руб.","code": "RUB"}

def test_get_transaction_data_empty(json_data_empty):
    data = json.loads(json_data_empty)
    assert data == []

