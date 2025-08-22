from masks import get_mask_card_number, get_mask_account

def mask_account_card(account_card: str) -> str:
    """Функция которая обробатывает информацию о картах и счетах"""
    card_type = ""
    if "Счет" in account_card:
        return f"Счет **{account_card[-4:]}"
    else:
        for i in account_card:
            if i.isalpha() or i ==" ":
                card_type += i
    return card_type + f"{account_card[-16:-12]} {account_card[-12:-10]}** **** {account_card[-4:]}"

result = mask_account_card("Visa Platinum 8990922113665229")
print(result)










    # def get_mask_card_number(number: int) -> str:
    #     """Функция принимает на вход номер карты и возвращает ее маску"""
    #     number_str = str(number)
    #     if len(number_str) != 16:
    #         return "Карта должна сосотоять из 16 цифр"
    #     return f"{number_str[0:4]} {number_str[4:6]}** **** {number_str[12:]}"
    #
    # def get_mask_account(account_number: int) -> str:
    #     """Функция принимает на вход номер счета и возвращает маску"""
    #     account_number_str = str(account_number)
    #     if len(account_number_str) != 20:
    #         return "Счет должен состоять из 20 цифр"
    #     return f"**{account_number_str[-4:]}"
