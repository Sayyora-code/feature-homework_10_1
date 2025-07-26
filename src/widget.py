from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_card: str) -> str:
    """Функция обрабатывает информацию о картах и счетах, возвращает замаскированный номер"""
    info_card_split = info_card.split()

    if len(info_card_split) < 2:
        return "Некорректный формат строки"

    name = " ".join(info_card_split[:-1])
    card_number = info_card_split[-1]

    if name == "Счет":
        result = get_mask_account(card_number)  # type: str
    else:
        result = get_mask_card_number(card_number)  # type: str

    return f"{name} {result}"


def get_date(date_str: str) -> str:
    """Функция возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    if len(date_str) < 10:
        return "Некорректный формат даты"
    new_date_str = f"{date_str[8:10]}.{date_str[5:7]}.{date_str[:4]}"
    return new_date_str
