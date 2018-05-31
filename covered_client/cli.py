import click
import sys
import os

import covered_client.reporter as reporter
from covered_client import __version__


@click.group()
@click.pass_context
def cli(ctx):
    pass


def main():
    cli()


@cli.command()
def version():
    print("covered {}".format(__version__))


@cli.command()
@click.option("--server", type=str, default=None)
@click.pass_context
def upload(ctx, server):
    if not server:
        try:
            server = os.environ["COVERED_SERVER"]
        except KeyError:
            raise KeyError("Specify server with --server or COVERED_SERVER environment variable.")
    report = reporter.create_report()
    if not report["source_files"]:
        raise click.ClickException("Coverage data not found!")
    reporter.upload(server, report)


if __name__ == "__main__":
    sys.exit(main())
