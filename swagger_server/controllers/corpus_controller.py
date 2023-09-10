import connexion

from services.corpus import corpus_add_word, corpus_has_word


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
    app = connexion.apps.flask_app

    body = connexion.request.get_json()

    words = body.get('words', [])

    # local cache of corpus words by length
    added = []

    for word in words:

        if corpus_has_word(word):
            app.logger.info(f'Word already exists in corpus: {word}')
            # Add word to the corpus
            continue
        else:
            corpus_add_word(word)
            added.append(word)
            app.logger.info(f'Word added to corpus: {word}')

    if added:
        return {}, 201
    else:
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
