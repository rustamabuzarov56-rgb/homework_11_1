import unittest
from unittest.mock import patch, mock_open
import csv
import pandas as pd
import pytest
from src.excel_csv_reader import read_transactions_from_csv, read_transactions_from_xlsx

class ReadTransactionsFromCsv(unittest.TestCase):
    @patch('builtins.open',new_callable=mock_open, read_data='transaction_id;amount;currency\n1;100.00;USD\n2;-50.00;EUR\n')
    def test_read_transactions_from_csv(self, mock_file):
        result = read_transactions_from_csv("/fake/path/to/file.csv")
        expected_output = [
            {"transaction_id": "1", "amount": "100.00", "currency": "USD"},
            {"transaction_id": "2", "amount": "-50.00", "currency": "EUR"}
        ]
        assert result == expected_output

    @patch('builtins.open', side_effect=FileNotFoundError())
    def test_read_transactions_file_not_found(self, mock_file):
        path_to_file = "/nonexistent/path/to/file.csv"
        transactions = read_transactions_from_csv(path_to_file)
        self.assertIsNone(transactions)

    @patch('builtins.open', side_effect=ValueError())
    def test_read_transactions_invalid_format(self, mock_file):
        path_to_file = "/invalid/path/to/file.csv"
        transactions = read_transactions_from_csv(path_to_file)
        self.assertIsNone(transactions)

class ReadTransactionsFromXlsx(unittest.TestCase):
    @patch('pandas.read_excel')
    def test_read_transactions_from_xlsx(self, mock_read_excel):
        mock_df = pd.DataFrame({
            'TransactionID': ['T1', 'T2'],
            'Amount': [100.0, -50.0],
            'Currency': ['USD', 'EUR']
        })
        mock_read_excel.return_value = mock_df
        result = read_transactions_from_xlsx('/fake/path.xlsx')
        expected_output = [
            {'TransactionID': 'T1', 'Amount': 100.0, 'Currency': 'USD'},
            {'TransactionID': 'T2', 'Amount': -50.0, 'Currency': 'EUR'}
        ]
        assert result == expected_output

    @patch('pandas.read_excel', side_effect=FileNotFoundError())
    def test_read_transactions_file_not_found(self, _):
        result = read_transactions_from_xlsx('/nonexistent/path.xlsx')
        self.assertIsNone(result)

    @patch('pandas.read_excel', side_effect=ValueError())
    def test_read_transactions_invalid_format(self, _):
        result = read_transactions_from_xlsx('/invalid/path.xlsx')
        self.assertIsNone(result)