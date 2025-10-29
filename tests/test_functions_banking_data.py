import unittest
from unittest.mock import patch
from src.functions_banking_data import process_bank_search, process_bank_operations

class TestBankSearch(unittest.TestCase):

    @patch("src.functions_banking_data.process_bank_search")
    def test_search_in_description(self, mock_process_bank_search):
        """Проверка поиска по полю 'description'. Используем patch для моков."""
        test_data = [
            {"id": 1, "amount": 1000, "description": "Оплата услуг"},
            {"id": 2, "amount": 500},
            {"id": 3, "amount": 2000, "description": "Зарплата"},
            {"id": 4, "amount": 300, "description": "Пополнение"}
        ]
        search_query = 'услуг'
        expected_result = [{"id": 1, "amount": 1000, "description": "Оплата услуг"}]


        mock_process_bank_search.return_value = expected_result


        actual_result = process_bank_search(test_data, search_query)

        self.assertEqual(actual_result, expected_result)

    @patch("src.functions_banking_data.process_bank_search")
    def test_no_match(self, mock_process_bank_search):
        """Проверка ситуации, когда нет совпадений."""
        test_data = [
            {"id": 1, "amount": 1000, "description": "Оплата товаров"},
            {"id": 2, "amount": 500},
            {"id": 3, "amount": 2000, "description": "Зарплата"},
            {"id": 4, "amount": 300, "description": "Пополнение"}
        ]
        search_query = 'услуг'
        expected_result = []

        mock_process_bank_search.return_value = expected_result
        actual_result = process_bank_search(test_data, search_query)
        self.assertEqual(actual_result, expected_result)

class TestProcessBankOperations(unittest.TestCase):
    def test_valid_data(self):
        """Тест с валидными данными"""
        data = [
            {'id': 1, 'amount': 1000, 'description': 'food'},
            {'id': 2, 'amount': 500, 'description': 'transport'},
            {'id': 3, 'amount': 2000, 'description': 'entertainment'},
            {'id': 4, 'amount': 800, 'description': 'food'}
        ]
        categories = ['food', 'transport', 'entertainment']
        expected_result = {'food': 2, 'transport': 1, 'entertainment': 1}
        self.assertEqual(process_bank_operations(data, categories), expected_result)


