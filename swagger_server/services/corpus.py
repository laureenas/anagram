import sqlalchemy as sa

from application import db
from services.models import get_letter_map


def corpus_has_word(word):
    '''Does corpus already contain word?'''
    if not word:
        return False

    corpus = db.metadata.tables['corpus']

    word_letter_map = get_letter_map(word)
    query = (
        sa.select(corpus.c.word).
        select_from(corpus).
        where(corpus.c.word == word)
    )

    result = db.session.execute(query)
    for row in result:
        # One row means that a word has been found
        return True
    return False


def corpus_add_word(word):
    if not word:
        return

    corpus = db.metadata.tables['corpus']
    letter_map = get_letter_map(word)
    query = (
        sa.insert(corpus).
        values(word=word, word_length=len(word), letter_map=letter_map)
    )
    result = db.session.execute(query)
    db.session.commit()

    return word
