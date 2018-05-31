import pytest
from click.testing import CliRunner
import re
import covered_client.cli as cli

@pytest.fixture
def runner():
    runner = CliRunner()
    return runner

def test_version(runner):
    result = runner.invoke(cli.version)
    assert result.exit_code == 0
    assert re.match("covered [0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}", result.output)
