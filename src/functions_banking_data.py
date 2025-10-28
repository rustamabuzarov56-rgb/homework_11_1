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

