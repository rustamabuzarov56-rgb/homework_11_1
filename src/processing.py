from mypy.state import state


def filter_by_state(transactions: list, key='EXECUTED') -> list:
    """ Функция возвращает новый список словарей, содержащий только те словари,
        у которых ключ соответствует указанному значению. """
    new_list = []
    for i in transactions:
        if i["state"] == key:
            new_list.append(i)
    return new_list

