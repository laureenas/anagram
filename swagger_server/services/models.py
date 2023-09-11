LETTER_IDX_EN = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25,
    '-': 26,  # 'Jean-Christophe' is apparently an English word
}
LETTER_COUNT_EN = len(LETTER_IDX_EN)


def get_letter_map(word):
    '''Crate a 26 symbol string representing count of each letter in the word.

    Assumption: no more than 9 identical letters in an EN word
    (could be raised to 15 quite easily if need be).

    Example:

    'a' - '10000000000000000000000000'
    'b' - '01000000000000000000000000'
    'z' - '00000000000000000000000001'
    'aab' - '21000000000000000000000000'

    '''

    if word is None:
        return None

    # Assumption: anagrams are not case-sensitive
    word = word.lower()

    letter_map = [0]*LETTER_COUNT_EN
    for letter in word:
        if letter not in LETTER_IDX_EN:
            raise ValueError(f'Not supported Letter {letter} in word {word}')
        letter_map[LETTER_IDX_EN[letter]] += 1

    return ''.join(map(str, letter_map))
