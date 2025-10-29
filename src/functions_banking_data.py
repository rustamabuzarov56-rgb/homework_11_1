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
    try:
        result = {category: 0 for category in categories}

        for operation in data:
            for category in categories:
                if category.lower() in operation.get('description', '').lower():
                    result[category] += 1
                    break  # Каждая операция относится только к одной категории

        return result
    except AttributeError as e:
        print(f"Ошибка: Неправильный формат данных ({e})")
        return {}
    except TypeError as e:
        print(f"Ошибка: Некорректный тип данных ({e})")
        return {}
    except Exception as e:
        print(f"Возникла неизвестная ошибка: {e}")
        return {}

