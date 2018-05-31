import os
import subprocess

def get_service_name():
    return os.environ.get("CI", None)


def get_job_number():
    # TODO: other services
    return os.environ.get("DRONE_JOB_NUMBER", None)


def get_build_number():
    # TODO: other services
    return os.environ.get("DRONE_BUILD_NUMBER", None)


def call(command):
    return subprocess.check_output(command).strip().decode("utf-8")


def get_git_branch():
    """Returns the current branch name"""
    return call(["git", "symbolic-ref", "HEAD", "--short"])


def get_git_commit():
    """Returns the current commit hash"""
    return call(["git", "rev-parse", "HEAD"])
