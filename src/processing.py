def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ соответствует указанному значению."""
    new_list = []
    for i in transactions:
        if i["state"] == state:
            new_list.append(i)
    return new_list


def sort_by_date(list_dict: list[dict], sort_order: bool = True) -> list:
    """Функция принимает список словарей, параметр задающий порядок сортировки и
    возвращать новый список, отсортированный по дате"""
    return sorted(list_dict, key=lambda x: x["date"], reverse=sort_order)
