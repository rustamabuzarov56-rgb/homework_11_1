import os
import json
import csv
import pandas as pd
import logging
import re
import requests

from excel_csv_reader import read_transactions_from_csv, read_transactions_from_xlsx
from external_api import get_transaction_amount
from processing import filter_by_state, sort_by_date
from functions_banking_data import process_bank_search
from utils import get_transaction_data



logger = logging.getLogger(__name__)  # Логгер для отслеживания действий

def main():
    # Директория, содержащая проект
    current_dir = os.path.dirname(__file__)
    # Определим пути к данным
    json_file_path = os.path.join(current_dir, '..', 'data', 'operations.json')
    csv_file_path = os.path.join(current_dir, '..', 'data', 'transactions.csv')
    xlsx_file_path = os.path.join(current_dir, '..', 'data', 'transactions_excel.xlsx')

    # Выбор типа файла
    file_type = int(input("""
Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""))

    # Чтение данных в зависимости от выбранного типа файла
    if file_type == 1:
        print("Для обработки выбран JSON-файл")
        data = get_transaction_data(json_file_path)
    elif file_type == 2:
        print("Для обработки выбран CSV-файл")
        data = read_transactions_from_csv(csv_file_path)
    elif file_type == 3:
        print("Для обработки выбран XLSX-файл")
        data = read_transactions_from_xlsx(xlsx_file_path)
    else:
        print("Неверный номер пункта меню!")
        return

    # Фильтрация по статусу
    user_input_status = input("""
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""").strip().upper()

    while user_input_status not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f'Статус операции "{user_input_status}" недоступен.')
        user_input_status = input("""
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""").strip().upper()

    print(f'Операции отфильтрованы по статусу "{user_input_status}"')
    filtered_by_status = filter_by_state(data, user_input_status)

    # Дополнительные настройки фильтрации и сортировки
    user_input_sort = input("Отсортировать операции по дате? Да/Нет").strip().lower()
    if user_input_sort == "да":
        ascending_or_descending = input("Отсортировать по возрастанию или по убыванию?").strip().lower()
        if ascending_or_descending == "по возрастанию":
            sorted_data = sort_by_date(filtered_by_status, False)
        elif ascending_or_descending == "по убыванию":
            sorted_data = sort_by_date(filtered_by_status)
        else:
            print("Неправильный ввод, сортировка не применялась.")
            sorted_data = filtered_by_status
    else:
        sorted_data = filtered_by_status

    # Рублевые транзакции
    user_input_currency = input("Выводить только рублевые транзакции? Да/Нет").strip().lower()
    if user_input_currency == "да":
        ruble_transactions = []
        for trans in sorted_data:
            amount_in_rubles = get_transaction_amount(trans)
            if amount_in_rubles is not None:
                ruble_transactions.append(amount_in_rubles)
        final_data = ruble_transactions
    else:
        final_data = sorted_data

    # Поиск по ключевому слову
    user_input_filter_word = input("Отфильтровать список транзакций по определённому слову в описании? Да/Нет").strip().lower()
    if user_input_filter_word == "да":
        user_word = input("Введите слово для фильтрации:").strip().lower()
        filtered_list_transactions = process_bank_search(final_data, user_word)
        results = filtered_list_transactions
    else:
        results = final_data

    # Вывод результата
    print("Распечатываю итоговый список транзакций...")
    if results:
        print(f"Всего банковских операций в выборке: {len(results)}")
        for idx, result in enumerate(results):
            date = result.get('date', '')
            description = result.get('description', '')
            account_number = result.get('accountNumber', '')
            amount = result.get('amount', '')
            print(f"{idx+1}: Дата: {date}, Описание: {description}, Номер счёта: {account_number}, Сумма: {amount}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

