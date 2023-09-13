import sqlalchemy as sa
from sqlalchemy.sql import func

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


def corpus_delete_all():
    corpus = db.metadata.tables['corpus']
    query = (
        sa.delete(corpus)
    )
    result = db.session.execute(query)
    db.session.commit()

    return result


def corpus_delete_word(word):
    corpus = db.metadata.tables['corpus']

    query = (
        sa.delete(corpus).
        where(corpus.c.word == word)
    )
    result = db.session.execute(query)
    db.session.commit()

    return result


def words_statistics():
    corpus = db.metadata.tables['corpus']

    query_min = (
        sa.select(func.min(corpus.c.word_length).label('min')).
        select_from(corpus)
    )
    query_max = (
        sa.select(func.max(corpus.c.word_length).label('max')).
        select_from(corpus)
    )
    query_count = (
        sa.select(func.count(corpus.c.word_length).label('count')).
        select_from(corpus)
    )

    min_ = max_ = average = None
    result_min = db.session.execute(query_min)
    for row in result_min:
        min_ = row[0]
    result_max = db.session.execute(query_max)
    for row in result_max:
        max_ = row[0]
    result_count = db.session.execute(query_count)
    for row in result_count:
        count = row[0]

    if min_ is not None and max_ is not None:
        average = (min_ + max_) / 2
    else:
        average = None

    return {
        'min': min_,
        'max': max_,
        'average': average,
        'count': count,
    }
