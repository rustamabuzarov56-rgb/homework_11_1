import re


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
    category_count = {}

    for cat in categories:
        category_count[cat] = 0

    for operation in data:
        desc = operation.get('description', '')
        for cat in categories:
            if cat.lower() in desc.lower():
                category_count[cat] += 1
                break

    return category_count

