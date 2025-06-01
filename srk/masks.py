def get_mask_card_number(card_number: str) -> str:
    """Пинимает на вход номер карты и возвращает ее маску"""
    beginning_nomber = card_number[:4]
    middle_nomber = card_number[5:7]
    end_nomber = card_number[-4:]
    return f"{beginning_nomber} {middle_nomber}** **** {end_nomber}"


print(get_mask_card_number(input()))


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    last = account_number[-4:]
    return f"**{last}"


print(get_mask_account(input()))
