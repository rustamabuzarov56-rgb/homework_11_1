from mypy.state import state


def filter_by_state(transactions: list, key='EXECUTED') -> list:
    """ Функция возвращает новый список словарей, содержащий только те словари,
        у которых ключ соответствует указанному значению. """
    new_list = []
    for i in transactions:
        if i["state"] == key:
            new_list.append(i)
    return new_list


def sort_by_date(list_dict: list, sort_order=True) -> list:
    """  Функция принимает список словарей, параметр задающий порядок сортировки и
         возвращать новый список, отсортированный по дате  """
    return sorted(list_dict, key=lambda x: x["date"], reverse=sort_order)
