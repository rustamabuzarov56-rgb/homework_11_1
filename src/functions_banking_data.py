import re
from typing import List, Dict
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция ищет банковские операции по указанному слову или строке в описании.
    """
    result = []
    try:
        pattern = re.compile(search, re.IGNORECASE)
        for item in data:
            try:
                description = item.get('description')
                if description is not None and pattern.search(description):
                    result.append(item)

            except Exception as e:
                print(f"Произошла ошибка при обработке элемента: {item}. Ошибка: {e}")

    except re.error as regex_error:
        print(f"Ошибка компиляции регулярного выражения: {regex_error}")

    return result

def process_bank_operations(data:list[dict], categories:list)->dict:
    """Функция которая принимает список словарей с данными о банковских операциях и список категорий операций
    и возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""

    try:

        if not isinstance(data, list):
            raise ValueError("Параметр 'data' должен быть списком.")

        if not all(isinstance(op, dict) for op in data):
            raise ValueError("Все элементы параметра 'data' должны быть словарями.")

        if not isinstance(categories, list):
            raise ValueError("Параметр 'categories' должен быть списком.")

        if not all(isinstance(cat, str) for cat in categories):
            raise ValueError("Все элементы параметра 'categories' должны быть строками.")


        operation_descriptions = []
        for op in data:
            description = op.get('description')
            if description is None or not isinstance(description, str):
                continue
            operation_descriptions.append(description)


        category_counts = Counter(operation_descriptions)

        result = {}
        for cat in categories:
            result[cat] = category_counts.get(cat, 0)

        return result
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return {}
