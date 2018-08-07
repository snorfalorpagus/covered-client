from setuptools import setup

setup(
    name="covered-client",
    use_scm_version=True,
    packages=["covered_client"],
    entry_points={
        "console_scripts": [
            "covered = covered_client.cli:main"
        ]
    },
    setup_requires=[
        "setuptools_scm"
    ],
    install_requires=[
        "click",
        "coverage",
        "requests",
    ]
)
