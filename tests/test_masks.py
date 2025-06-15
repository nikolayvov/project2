from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(correct_c_number):
    assert get_mask_card_number("126 456789123 4888") == correct_c_number


def test_get_mask_account(correct_a_number):
    assert get_mask_account("2345 678998765 4323086") == correct_a_number
