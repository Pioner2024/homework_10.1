def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    card_number = list(filter(str.isdigit, card_number))
    sfsdf = ("".join(card_number))

    beginning_number = sfsdf[:4]
    middle_number = sfsdf[4:6]
    end_number = sfsdf[-4:]
    mask = f"{beginning_number} {middle_number}** **** {end_number}"
    return mask


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    last = account_number[-4:]
    return f"Счет **{last}"
