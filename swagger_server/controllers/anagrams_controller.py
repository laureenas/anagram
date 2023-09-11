import json

import connexion

from services.anagram import find_anagrams
from services.corpus import corpus_has_word


def anagrams_word_get(word):
    """Takes a word of English-language and returns its anagrams.

    Returns a JSON array of English-language words that are anagrams of the word passed in the URL.  # noqa: E501

    :param single_word: English languate word
    :type single_word: str

    :rtype: AnagramList
    """
    app = connexion.apps.flask_app

    # XXX: Connexion does not deal with positional arguments gracefully
    if word == '{}':
        word = ''

    anagrams = find_anagrams(word)
    if anagrams:
        app.logger.info(f'Word found in corpus: {word}')
    else:
        app.logger.info(f'Word not found in corpus: {word}')

    result = {'anagrams': anagrams}

    return result, 200
