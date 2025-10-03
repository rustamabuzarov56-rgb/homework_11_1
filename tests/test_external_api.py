from unittest.mock import patch

from src.external_api import get_transaction_amount


def test_get_transaction_amount(test_transaction_list):
    result = get_transaction_amount(test_transaction_list)
    assert result == "100.0"


@patch("requests.get")
def test_get_transaction_amount_usd(mock_get):
    mock_get.return_value.json.return_value = 899.0
    assert get_transaction_amount({"operationAmount": {"currency": {"code": "USD"}, "amount": 899.0}}) == 899.0
    mock_get.assert_called_once()


@patch("requests.get")
def test_get_transaction_amount_eur(mock_get):
    mock_get.return_value.json.return_value = 999.0
    assert get_transaction_amount({"operationAmount": {"currency": {"code": "EUR"}, "amount": 999.0}}) == 999.0
    mock_get.assert_called_once()
