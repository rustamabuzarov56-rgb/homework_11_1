def mask_account_card(account_card: str) -> str:
    """Функция которая обробатывает информацию о картах и счетах"""
    card_type = ""
    if "Счет" in account_card:
        return f"Счет **{account_card[-4:]}"
    else:
        for i in account_card:
            if i.isalpha() or i == " ":
                card_type += i
    return card_type + f"{account_card[-16:-12]} {account_card[-12:-10]}** **** {account_card[-4:]}"
print(mask_account_card("Visa Platinum 7000792289606361"))

def get_date(date: str) -> str:
    """Функция которая возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
