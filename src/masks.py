def get_mask_card_number(card_number: str) -> str:
    """Функция, которая создает маску номера карты."""
    card_number = card_number.replace(" ", "")
    mask_c = "******"
    mask_card_number = card_number[:6] + mask_c + card_number[12:]
    gr_mask_card_number = " ".join(mask_card_number[i: i + 4] for i in range(0, len(mask_card_number), 4))
    return gr_mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция, которая создает маску номера счета."""
    account_number = account_number.replace(" ", "")
    mask_a = "**"
    mask_account = mask_a + account_number[-4:]
    return mask_account
