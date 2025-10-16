import csv
from collections.abc import Hashable
from typing import Any

import pandas as pd


def read_transactions_from_csv(path_file_csv: str) -> list[Any]:
    """Функция для считывания финансовых операций из CSV принимает путь к файлу CSV в качестве аргумента
    и выдает список словарей с транзакциями."""
    try:
        with open(path_file_csv, encoding="utf8") as file:
            reader = csv.DictReader(file, delimiter=";")
            data_list = list(reader)
            return data_list
    except FileNotFoundError:
        print(f"Ошибка: файл {path_file_csv} не найден")
    except ValueError:
        print("Ошибка: некорректный формат файла или поврежденный файл.")
    except Exception as e:
        print(f"Произошла неизвестная ошибка {e} .")


def read_transactions_from_xlsx(path_file_xlsx: str) -> list[dict[Hashable, Any]]:
    """Функция для считывания финансовых операций из excel  принимает путь к файлу xlsx в качестве аргумента
    и выдает список словарей с транзакциями."""
    try:
        df = pd.read_excel(path_file_xlsx)
        return df.to_dict("records")
    except FileNotFoundError:
        print(f"Ошибка: файл {path_file_xlsx} не найден")
    except ValueError:
        print("Ошибка: некорректный формат файла или поврежденный файл.")
    except Exception as e:
        print(f"Произошла неизвестная ошибка {e} .")
