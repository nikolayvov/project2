from masks import get_mask_card_number
from masks import get_mask_account

def mask_account_card(any_number: str) -> str:
    """Функция, которая созает маску номера карты или счета с названием."""
    parts = any_number.split()
    masked_parts = []

    for part in parts:
        if part.isdigit() and len(part) == 16:
            masked_parts.append(get_mask_card_number(part))
        elif part.isdigit():
            masked_parts.append(get_mask_account(part))
        else:
            masked_parts.append(part)

    return ' '.join(masked_parts)


def get_date(date_time: str) -> str:
    """Функция, которая выделяет дату из стоки с датой и временем"""
    date = date_time[:10]
    new_date = f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    return new_date

print(get_date("2024-03-11T02:26:18.671407"))
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))



