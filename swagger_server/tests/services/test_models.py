import pytest

from services.models import LETTER_IDX_EN, get_letter_map


def test_get_letter_map():
    result = get_letter_map('dear')
    assert result == '100110000000000001000000000'


def test_get_letter_map_empty():
    result = get_letter_map(None)
    assert result is None


def test_get_letter_map_empty_string():
    result = get_letter_map('')
    assert result == '000000000000000000000000000'


def test_get_letter_map_multiple_letters():
    result = get_letter_map('door')
    assert result == '000100000000002001000000000'


def test_get_letter_map_multiple_hiphen():
    result = get_letter_map('jean-christophe')
    assert result == '101020021100011101110000001'


def test_get_letter_map_letter_idx():
    result = get_letter_map(''.join(LETTER_IDX_EN.keys()))
    assert result == '111111111111111111111111111'
