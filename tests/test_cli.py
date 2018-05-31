import pytest
from click.testing import CliRunner
import re
import covered_client.cli as cli
from unittest import mock
import os
import json
import uuid

@pytest.fixture
def runner():
    runner = CliRunner()
    return runner


@pytest.fixture
def example_project():
    original_directory = os.getcwd()
    os.chdir("example_project")
    yield
    os.chdir(original_directory)


class MockResponse():
    def __init__(self, status_code=200, content=None):
        self.status_code = status_code
        self.content = content

    @property
    def text(self):
        return self.content

    @property
    def json(self):
        return json.loads(self.content)


def test_version(runner):
    result = runner.invoke(cli.version)
    print(result.output.strip())
    assert result.exit_code == 0
    assert re.match("covered [0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}", result.output)


@mock.patch.dict(os.environ, {"COVERED_SERVER": "http://localhost"})
def test_upload_server_env(runner, example_project):
    response = MockResponse(
        status_code=200,
        content=f"http://localhost/view/{uuid.uuid4()}"
    )
    with mock.patch("requests.post", return_value=response):
        result = runner.invoke(cli.upload)
    print(result.output.strip())
    assert result.exit_code == 0
    assert "http://localhost" in result.output


def test_upload_server_arg(runner, example_project):
    response = MockResponse(
        status_code=200,
        content=f"http://localhost/view/{uuid.uuid4()}"
    )
    with mock.patch("requests.post", return_value=response):
        result = runner.invoke(cli.upload, ["--server", "http://localhost"])
    print(result.output.strip())
    assert result.exit_code == 0
    assert "http://localhost" in result.output
