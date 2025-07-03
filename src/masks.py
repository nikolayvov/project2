import logging


logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая создает маску номера карты."""
    card_number = card_number.replace(" ", "")
    mask_c = "******"
    mask_card_number = card_number[:6] + mask_c + card_number[12:]
    logger.info("Создание маски номера карты")
    gr_mask_card_number = " ".join(mask_card_number[i: i + 4] for i in range(0, len(mask_card_number), 4))
    return gr_mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция, которая создает маску номера счета."""
    account_number = account_number.replace(" ", "")
    mask_a = "**"
    logger.info("Создание маски номера счета")
    mask_account = mask_a + account_number[-4:]
    return mask_account


# print(get_mask_card_number("1234567890123456"))
# print(get_mask_account("12345678901234563456"))
