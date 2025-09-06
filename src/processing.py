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

print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': 'T18:35:29.512364.2019-0-03'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': 'T02:08:58.425572.2018-06-30'},
            {'id': 594226727, 'state': 'CANCELED', 'date': 'T21:27:25.241689.2018-09-12'},
            {'id': 615064591, 'state': 'CANCELED', 'date': 'T08:21:33.419441.2018-10-14'}]))