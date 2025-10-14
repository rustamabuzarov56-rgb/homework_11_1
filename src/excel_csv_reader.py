import csv
import openpyxl
import pandas as pd


def transaction_csv(path):
    try:
        with open(path, encoding="utf8") as file:
            reader = csv.DictReader(file, delimiter=";")
            data_list = list(reader)
            return data_list
    except FileNotFoundError:
            print(f"Ошибка: файл {path} не найден")
            return None
    except ValueError:
            print("Ошибка: некорректный формат файла или поврежденный файл.")
            return None
    except Exception as e:
            print(f"Произошла неизвестная ошибка {e} .")
            return None


def transaction_excel(path_file):
    try:
        df = pd.read_excel(path_file)
        return df.to_dict('records')
    except FileNotFoundError:
        print(f"Ошибка: файл {path_file} не найден")
        return None
    except ValueError:
        print("Ошибка: некорректный формат файла или поврежденный файл.")
        return None
    except Exception as e:
        print(f"Произошла неизвестная ошибка {e} .")
        return None

