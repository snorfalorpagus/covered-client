import os
import subprocess


def get_service_name():
    return os.environ.get("CI_NAME", None)


def get_job_number():
    # TODO: other services
    return os.environ.get("DRONE_JOB_NUMBER", None)


def get_build_number():
    # TODO: other services
    return os.environ.get("DRONE_BUILD_NUMBER", None)


def call(command):
    return subprocess.check_output(command).strip().decode("utf-8")


def get_branch():
    branch = os.environ.get("CI_BRANCH", None)
    if branch:
        return branch
    branch = get_git_branch()
    return branch


def get_commit():
    commit = os.environ.get("CI_COMMIT", None)
    if commit:
        return commit
    commit = get_git_commit()
    return commit


def get_git_branch():
    """Returns the current branch name"""
    return call(["git", "symbolic-ref", "HEAD", "--short"])


def get_git_commit():
    """Returns the current commit hash"""
    return call(["git", "rev-parse", "HEAD"])
