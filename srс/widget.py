from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(card_number: str) -> str:
    """Обрабатывает данные карты и счета."""
    masked_number = get_mask_card_number(card_number)
    part_of_the_map: list[str] = []

    # Отделяем слова от цифр.
    for character in card_number:
        if character.isalpha():
            part_of_the_map.append(character)

    valid_characters = ''.join(part_of_the_map)

    # Анализируем, присутствует ли ключевое слово, и разделяем его пробелом.
    key = "Visa"
    if key in valid_characters:
        result = valid_characters.replace(key, key + " ")
        return f"{result} {masked_number}"
    else:
        return f"{valid_characters} {masked_number}"


# Получение ввода номера карты
card_number = input("Введите номер карты: ")
print(mask_account_card(card_number))

# Получение ввода номера счёта
account_number = input("Введите номер счёта: ")
account_mask = get_mask_account(account_number)
print(account_mask)


def get_date(correct: str) -> str:
    """Возвращает строку с датой в формате 'ДД.ММ.ГГГГ'."""
    year = correct[2:4]
    month = correct[5:7]
    day = correct[8:10]
    # Получаем дату в формате 'ДД.ММ.ГГГГ'
    return f"{day}.{month}.{year}"
