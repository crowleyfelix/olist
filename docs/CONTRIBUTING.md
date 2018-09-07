# Getting Started

These instructions should be sufficiente to set up a development environment. <br />

## Prerequisites

After clonning these repository, you'll need the following tools.

- [Python 3.6]
- [pip]

## Virtual environment

Using a tool called [pipenv], you can either managing your dependencies and virtual environments of the project.

Pipenv automatic loads environment variables from a [.env] in root project. So, set up the variables described on .env.example in a new file.

Installing pipenv

```shell
pip install pipenv
```

Installing application and development dependencies.

```shell
pipenv install -d
```

With the follow command you will access the virtual environment:

```shell
pipenv shell
```

**Pipenv only supports Linux. To other systems you should use pip with other virtual environment manager, and set environment variables in your terminal session.**

## Linting

The linting tooling is provided by [pylama] wich is a wrapper that group all python popular linters. Some text editors provide a configuration to automatize the pylama executions and expose the messages. Please, check yours text editor docs for more details.

To mannualy execute pylama:

```shell
pylama
```

## Running tests

To run all tests

```shell
pytest
```

To run unit tests:

```shell
pytest tests/unit
```

To run integration tests:

```shell
pytest tests/integration -sv
```

To run coverage report:

```shell
pytest --cov=app --cov-report html
```

**The coverage report is generated in htmlcov folder**

[Python 3.6]: https://www.python.org/downloads/
[pip]: https://docs.python.org/3/installing/index.html
[pipenv]: https://docs.pipenv.org/
[pylama]: https://pylama.readthedocs.io/en/latest/
[.env]: https://docs.pipenv.org/advanced/#automatic-loading-of-env
