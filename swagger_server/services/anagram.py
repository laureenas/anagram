import sqlalchemy as sa

from application import db
from services.models import get_letter_map


def find_anagrams(word):
    '''Find anagrams based on word letter map'''
    corpus = db.metadata.tables['corpus']

    letter_map = get_letter_map(word)
    query = (
        sa.select(corpus.c.word).
        select_from(corpus).
        where(corpus.c.letter_map == letter_map)
    )

    anagrams = []
    result = db.session.execute(query)
    for row in result:
        # Word is not its own anagram
        if row[0] == word:
            continue
        anagrams.append(row[0])

    return anagrams
