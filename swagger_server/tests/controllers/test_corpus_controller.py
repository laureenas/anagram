# coding: utf-8
import pytest

from flask import json

from services.corpus import corpus_add_word, corpus_has_word


def test_words_post_empty(client):
    """Test words_post without words."""
    body = {'words': []}
    response = client.post(
        '/api/v1/words',
        data=json.dumps(body),
        content_type='application/json')
    assert response.status_code == 200
    assert response.json == {}


@pytest.mark.parametrize('words', [
    ['read', 'dear', 'dare'],
    ['Read', 'dEAr', 'darE']
])
def test_words_post(client, words):
    """Test add English-language words to the corpus."""
    body = {'words': ['read', 'dear', 'dare']}
    response = client.post(
        '/api/v1/words',
        data=json.dumps(body),
        content_type='application/json')
    assert response.status_code == 201
    assert response.json == {}


@pytest.mark.parametrize('word', ('dear', 'Dear', 'DeaR'))
def test_words_post_single(client, word):
    """Test case for post words with a single word."""
    body = {'words': [word]}
    response = client.post(
        '/api/v1/words',
        data=json.dumps(body),
        content_type='application/json')
    assert response.status_code == 201
    assert response.json == {}


def test_words_delete(client):
    """Test case for delete all words."""
    corpus_add_word('dare')
    corpus_add_word('read')

    response = client.delete('/api/v1/words')

    assert response.status_code == 204
    assert not corpus_has_word('dare')
    assert not corpus_has_word('read')


@pytest.mark.parametrize('word', ('dear', 'Dear', 'DeaR'))
def test_words_word_delete(client, word):
    """Test for deleting a single word from a corpus."""
    corpus_add_word('dear')
    corpus_add_word('read')

    response = client.delete(f'/api/v1/words/{word}')

    assert response.status_code == 204
    assert corpus_has_word('read')
    assert not corpus_has_word('dare')


def test_words_word_delete_hollow(client):
    """Test for deleting without a positional argument."""
    response = client.delete('/api/v1/words/')
    assert response.status_code == 404


def test_words_word_delete_non_existent(client):
    """Test for deleting a non-existing word."""
    response = client.delete('/api/v1/words/nonsuch')
    assert response.status_code == 404


@pytest.mark.skip(reason='Ingesting ~235k English words takes ~25 minutes')
def test_words_post_load(client):
    """Test loading all words in English language."""
    BATCH_SIZE = 1000
    BATCH_COUNT = 10

    with open('../homework_task/dictionary.txt', 'r') as dictionary:
        lines = dictionary.readlines()
    words_en = [word.strip() for word in lines]

    for start in range(0, len(words_en), BATCH_SIZE):
        batch = words_en[start: start + BATCH_SIZE]

        body = {'words': batch}
        response = client.post(
            '/api/v1/words',
            data=json.dumps(body),
            content_type='application/json')
        assert response.status_code == 201
        assert response.json == {}

        # NB: pytest does not expose stdout until a test completed and if so
        # only in the case when the test failed
        print(f'Batch {start}:{start + BATCH_SIZE} processed...')
