# coding: utf-8
import json

import pytest

from services.corpus import corpus_add_word, corpus_has_word


@pytest.mark.xfail(reason = 'Figure out Swagger for optional positional parameters in connexion')
def test_anagrams_word_get_empty(client):
    """Test case for anagrams_word_get empty parameter

    Takes a JSON array of English-language words and adds them to the corpus.
    """
    response = client.get('/api/v1/anagrams/')
    assert response.status_code == 200
    assert response.json == {}


def test_anagrams_word_get_not_found(client):
    """Test case for anagrams_word_get empty parameter

    Takes a JSON array of English-language words and adds them to the corpus.
    """
    response = client.get('/api/v1/anagrams/dare')
    assert response.status_code == 200
    assert response.json == {'anagrams': []}


def test_anagrams_word_get(client):
    """Test case for anagrams_word_get

    Takes a JSON array of English-language words and adds them to the corpus.
    """
    corpus_add_word('read')

    response = client.get('/api/v1/anagrams/dare')
    assert response.json == {"anagrams": ["read"]}


def test_anagrams_word_get_word_not_its_own_anagram(client):
    """Test that word is not its anagram"""
    corpus_add_word('read')

    response = client.get('/api/v1/anagrams/read')

    assert corpus_has_word('read')
    assert response.json == {"anagrams": []}
