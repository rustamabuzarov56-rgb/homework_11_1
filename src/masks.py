import logging
import os

from charset_normalizer.md import getLogger

# Создание экземпляра логгера
logger = getLogger("masks")
logger.setLevel(logging.DEBUG)

# Определение формата сообщений
file_formatter = logging.Formatter("Request time:%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Создание FileHandler и настройка его форматов
log_file_path = os.path.join(os.path.dirname(__file__), "../logs/masks.log")
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    number_str = str(number)
    if len(number_str) != 16:
        logger.error("Номера счета не соответсвует заданному формату")
        return "Номер карты должен состоять из 16 цифр"
    logger.debug("Функция выполнена без ошибок")
    return f"{number_str[0:4]} {number_str[4:6]}** **** {number_str[12:]}"


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает маску"""
    account_number_str = str(account_number)
    if len(account_number_str) != 20:
        logger.error("Номера счета не соответсвует заданному формату")
        return "Номер счета должен состоять из 20 цифр"
    logger.debug("Функция выполнена без ошибок")
    return f"**{account_number_str[-4:]}"
