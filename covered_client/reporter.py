import os
import json
import coverage
import requests
from io import StringIO

from .ci import get_service_name, get_build_number, get_job_number, get_git_branch, get_git_commit


def create_report():
    cov = coverage.coverage()
    cov.load()
    cov_data = cov.get_data()

    report = {
        "service": service_info(),
        "git": git_info(),
    }

    paths = cov_data.measured_files()
    paths.sort()

    report["source_files"] = [create_report_for_file(cov, path) for path in paths]
    return report


def service_info():
    service = {
        "name": get_service_name(),
        "job_id": get_job_number(),
        "build_id": get_build_number(),
    }
    return service


def git_info():
    git = {
        "branch": get_git_branch(),
        "commit": get_git_commit(),
    }


def create_report_for_file(cov, path):
    relative_path = os.path.relpath(path).replace("\\", "/")
    analysis = cov._analyze(path)

    # get line-by-line coverage
    count_lines = len(list(analysis.file_reporter.source_token_lines()))
    line_coverage = [get_coverage(n, analysis) for n in range(1, count_lines + 1)]

    hit = len(analysis.statements) - len(analysis.missing)
    if len(analysis.statements) > 0:
        coverage = hit / len(analysis.statements) * 100
    else:
        coverage = 100

    summary = {
        "missing": len(analysis.missing),
        "excluded": len(analysis.excluded),
        "hit": hit,
        "total": len(analysis.statements),
        "coverage": coverage,
    }

    # read source code
    with open(path, "r") as f:
        source = f.read()

    report = {
        "name": relative_path,
        "source": source,
        "coverage": line_coverage,
        "summary": summary,
    }
    return report


def get_coverage(n, analysis):
    if n in analysis.missing:
        return 0
    if n not in analysis.statements:
        return None
    return 1


def upload(api_root, report):
    url = f"{api_root}/upload"
    report_json = json.dumps(report)

    res = requests.post(url, files={"file": ("coverage.json", StringIO(report_json), "application/json")})  # TODO: as file? gz?
    assert res.status_code == 200  # TODO
    print(res.text)
