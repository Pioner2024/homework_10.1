def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску."""
    card_number_digits = list(filter(str.isdigit, card_number))
    card_number_str = "".join(card_number_digits)

    beginning_number = card_number_str[:4]
    middle_number = card_number_str[4:6]
    end_number = card_number_str[-4:]

    mask = f"{beginning_number} {middle_number}** **** {end_number}"
    return mask


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску."""
    last_digits = account_number[-4:]
    return f"Счет **{last_digits}"
