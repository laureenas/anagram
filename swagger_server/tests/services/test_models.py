import pytest

from services.models import LETTER_IDX_EN, get_letter_map


def test_get_letter_map():
    result = get_letter_map('dear')
    assert result == '10011000000000000100000000'


def test_get_letter_map_empty():
    result = get_letter_map(None)
    assert result is None


def test_get_letter_map_empty_string():
    result = get_letter_map('')
    assert result == '00000000000000000000000000'


def test_get_letter_map_multiple_letters():
    result = get_letter_map('door')
    assert result == '00010000000000200100000000'


def test_get_letter_map_letter_idx():
    result = get_letter_map(''.join(LETTER_IDX_EN.keys()))
    assert result == '11111111111111111111111111'
