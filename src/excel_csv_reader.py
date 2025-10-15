import csv
import openpyxl
import pandas as pd


def read_transactions_from_csv(path_file_csv):
    """Функция для считывания финансовых операций из CSV принимает путь к файлу CSV в качестве аргумента
     и выдает список словарей с транзакциями."""
    try:
        with open(path_file_csv, encoding="utf8") as file:
            reader = csv.DictReader(file, delimiter=";")
            data_list = list(reader)
            return data_list
    except FileNotFoundError:
            print(f"Ошибка: файл {path_file_csv} не найден")
            return None
    except ValueError:
            print("Ошибка: некорректный формат файла или поврежденный файл.")
            return None
    except Exception as e:
            print(f"Произошла неизвестная ошибка {e} .")
            return None


def read_transactions_from_xlsx(path_file_xlsx):
    """Функция для считывания финансовых операций из excel  принимает путь к файлу xlsx в качестве аргумента
         и выдает список словарей с транзакциями."""
    try:
        df = pd.read_excel(path_file_xlsx)
        return df.to_dict('records')
    except FileNotFoundError:
        print(f"Ошибка: файл {path_file_xlsx} не найден")
        return None
    except ValueError:
        print("Ошибка: некорректный формат файла или поврежденный файл.")
        return None
    except Exception as e:
        print(f"Произошла неизвестная ошибка {e} .")
        return None

