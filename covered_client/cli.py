import click
import sys
import os

import covered_client.reporter as reporter

@click.group()
@click.pass_context
def cli(ctx):
    pass


def main():
    cli()


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
    reporter.upload(server, report)


if __name__ == "__main__":
    sys.exit(main())