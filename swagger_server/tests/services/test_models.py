from test import services


def test_get_letter_map():
    result = get_letter_map('dear')
    assert result == ''


def test_get_letter_map_emppty():
    result = get_letter_map()
    assert result is None
