import connexion
import six

import util
from models.word_list import WordList


def words_delete():
    """Delete all words in the corpus.

    :rtype: Object
    """
    return {}, 204


def words_post(body=None):
    """Add English-language words to the corpus.

    Takes a JSON array of English-language words and adds them to the corpus.

    :param body:
    :type body: dict | bytes

    :rtype: Object
    """
    if connexion.request.is_json:
        body = WordList.from_dict(connexion.request.get_json())
    return {}, 200


def words_word_delete(word):
    """Delete a single word from the corpus.

    :param word: English languate word
    :type single_word: str

    :rtype: Object
    """
    return {
        "message": "Not found",
        "error_code": "NotFound"
    }, 404
