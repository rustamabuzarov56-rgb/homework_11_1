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

result_1 = mask_account_card("Visa Platinum 8990922113665229")
print(result_1)


def get_date(date: str) -> str:
    """Функция которая возвращает строку с датой в формате 'ДД.ММ.ГГГГ' """
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"

result = get_date("2024-03-11T02:26:18.671407")
print(result)