from setuptools import setup

setup(
    name="covered-client",
    packages=["covered_client"],
    entry_points={
        "console_scripts": [
            "covered = covered_client.cli:main"
        ]
    },
    install_requires=[
        "click",
        "coverage",
        "requests",
    ]
)
