# coding: utf-8

from flask import json

from models.word_list import WordList
from services.corpus import corpus_add_word, corpus_has_word


def test_words_post_empty(client):
    """Test case for words_post hollow

    Add English-language words to the corpus.
    """
    body = WordList()
    response = client.post(
        '/api/v1/words',
        data=json.dumps(body),
        content_type='application/json')
    assert response.status_code == 200
    assert response.json == {}


def test_words_post(client):
    """Test case for words_post hollow

    Add English-language words to the corpus.
    """
    body = {"words": ["read", "dear", "dare"]}
    response = client.post(
        '/api/v1/words',
        data=json.dumps(body),
        content_type='application/json')
    assert response.status_code == 201
    assert response.json == {}


def test_words_post_single(client):
    """Test case for words_post single word

    Add English-language word to the corpus.
    """
    body = WordList(['dare'])
    response = client.post(
        '/api/v1/words',
        data=json.dumps(body),
        content_type='application/json')
    assert response.status_code == 201
    assert response.json == {}


def test_words_delete(client):
    """Test case for delete all words

    Delete all words in the corpus.
    """
    corpus_add_word('dare')
    corpus_add_word('read')

    response = client.delete('/api/v1/words')

    assert response.status_code == 204
    assert not corpus_has_word('dare')
    assert not corpus_has_word('read')


def test_words_word_delete(client):
    """Test for deleting a single word from a corpus"""
    corpus_add_word('dear')
    corpus_add_word('read')

    response = client.delete('/api/v1/words/dear')

    assert response.status_code == 204
    assert corpus_has_word('read')
    assert not corpus_has_word('dare')


def test_words_word_delete_hollow(client):
    """Test for deleting without a positional argument
    """
    response = client.delete('/api/v1/words/')
    assert response.status_code == 404


def test_words_word_delete_non_existent(client):
    """Test for deleting a non-existing word"""
    response = client.delete('/api/v1/words/nonsuch')
    assert response.status_code == 404
