# coding: utf-8

def test_anagrams_word_get(client):
    """Test case for anagrams_word_get

    Takes a JSON array of English-language words and adds them to the corpus.
    """
    response = client.get('/api/v1/anagrams/{}')
    assert response.json == {}

