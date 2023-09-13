# Anagram search application

## Overview
The anagram application POC (ProveOfConcept) is able to provide anagrams for a given English language word given a corpus of English language words.

The application is based on `connextion` wrapper over Flask framework. Persistent SQLite wrapped with SQLAlchemy is used for storage which should be enough for the POC scope. Date model is based on anagram map: letters in each word are counted and their count is noted in a letter 'map' (see swagger_server/services/models.py).

Full disclosure: The initial application boilerplate was generated in Swagger-frist manner. Swagger definitions were created in swagger.io SAAS and auto-generated boilerplate was exported (hence the name `swagger_server` of the server root folder). This was to experiment with Swagger-definition-first toolings out there. This turned out to be not a very productive choice, however. Generated server boilerplate was trimmed, mangled, and augmented. The original boilerplate can bee found under `/homework_task/boilerplate_generation/python-flask-server-generated.zip`. Detailed list of changes to the boilerplate presented in commit 3f71d686c7d8a60e3cf1b84b084660940946a762. In the end, the `connextion` wrapper was used only for input/output validation based on definitions in swagger/swagger.yaml and for the Swagger UI that comes for free.


## Requirements
Make, virtualenv, python (tested on v 3.10).

## Usage
To run the server, please execute the following from the root directory:

```
cd swagger_server && make run
```
### Command line

Adding words to the corpus
```
$ curl -i -X POST -H 'Content-Type: application/json' -d '{ "words": ["read", "dear", "dare"] }' http://localhost:8080/api/v1/words
HTTP/1.1 201 Created
...
```

Fetching anagrams
```
$ curl -i http://localhost:8080/api/v1/anagrams/read
HTTP/1.1 200 OK
...
{
  anagrams: [
    "dear",
    "dare"
  ]
}
```

Delete single word
```
$ curl -i -X DELETE http://localhost:8080/api/v1/words/read
HTTP/1.1 204 No Content
...
```

Delete all words
```
$ curl -i -X DELETE http://localhost:8080/api/v1/words
HTTP/1.1 204 No Content
```


### UI

You can open your browser to here to review Swagger and execute sample calls:

```
http://localhost:8080/api/v1/ui/
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
``**

## Testing

To launch unit and  integration tests, please execute the following from the root directory:
```
cd swagger_server && make test
```
## Performance

Ingesting ~235k English words from homework_task/dictionary.txt takes ~25 minutes.

Finding anagrams for word in ~235k corpus takes <100ms.


## TODOs:

### Knowwn bugs
- Add flake8 Make target and clean up PEP-8.
- Review configs: Use dev/testing/production config appropriatly.

### Immediate TODOs:

- Refactor weird auto-generated Swagger schema `inline_response_200`
- Add column `corpus.word.is_proper_nount` for proper nount statistics endpoint.

### Nice to haves:

- Switch from python's builtin web server to UWSGI (part of configuration?).
- Start using requirements.in and requirements-dev.in.
- Review errors - maybe not rely on connextion validation?
  CI/CD.
- Add Alembic DB schema migration.
