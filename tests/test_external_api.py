from unittest.mock import patch

from src.external_api import get_transaction_amount


def test_get_transaction_amount(test_transaction_list):
    result = get_transaction_amount(test_transaction_list)
    assert result == "100.0"


