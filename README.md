# covered-client

Client application for the *covered* coverage tool.

See also the server-side component: https://github.com/snorfalorpagus/covered-server

## Installation

```
python setup.py install
```

For development, use Pipenv:

```
pipenv install --dev
pipenv shell
```

## Testing

You must generate coverage data for the `example_project` before running tests. See [example_project/README.md](example_project/README.md).

Running tests locally:

```
pytest tests -v --cov=covered_client --cov=tests
```

Testing with Drone CI:

```
drone exec
```

## Usage

First, run your tests with coverage.py:

```
coverage run my_program.py arg1 arg2
```

Or:

```
pytest tests --cov=my_program --cov=tests
```

Then upload the results to the server (where `--server` is the URL of coverage-server):

```
covered upload --server=http://localhost:5000
```

The server will respond with the URL the report is available at.
