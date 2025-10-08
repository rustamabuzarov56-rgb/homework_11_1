import json
import logging
import os
from typing import Any
from charset_normalizer.md import getLogger

# Создание экземпляра логгера
logger = getLogger("utils")
logger.setLevel(logging.DEBUG)

# Определение формата сообщений
file_formatter = logging.Formatter("Request time:%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Создание FileHandler и настройка его форматов
log_file_path = os.path.join(os.path.dirname(__file__),"../logs/utils.log")
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)

def get_transaction_data(path: str) -> Any:
    """Функция принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        logger.debug(f"Открытие файла {path}")
        with open(path, "r", encoding="utf-8") as f:
            transaction = json.load(f)
        return transaction
    except json.JSONDecodeError as ex:
        logger.error(f"Произошла ошибка {ex}")
        return []
    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка {ex}")
        return []
    except TypeError as ex:
        logger.error(f"Произошла ошибка {ex}")
        return []
