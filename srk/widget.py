#Импортируем функции
from masks import get_mask_card_number
from masks import get_mask_account

""" Создаем функцию для обработки данных карт и счетов."""
def mask_account_card(card_number):

    masked_number = get_mask_card_number(card_number)
    part_of_the_map = []
    # Отделяем слова от цифр.
    for character in card_number:
        if character.isalpha():
            part_of_the_map.append(character)
        valid_characters = ''.join(part_of_the_map)
    # Анализируем, присутствует ли ключевое слово, и разделяем его пробелом.
    key = "Visa"
    if key in valid_characters:
        result = valid_characters.replace(key,key +" ")
        return f"{result} {masked_number}"
    else:
        return f"{valid_characters} {masked_number}"





map = input("Введите номер карты: ")
print(mask_account_card(map))

score = input("Ведите номер счёта:")
account_mask = get_mask_account(score)
print(account_mask)



'''Возвращает строку с датой "ДД.ММ.ГГГГ" '''
def get_date(correct):
    year = correct[2:4]
    month = correct[5:8]
    day = correct[8:10]

    return f"{day}-{month}{year}"


dete="2024-03-11T02:26:18.671407"
print(get_date(dete))