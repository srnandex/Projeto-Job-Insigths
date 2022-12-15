from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf8") as file:
        return list(csv.DictReader(file))


def get_unique_job_types(path: str) -> List[str]:
    data_jobs = read(path)
    jobs = set()
    for job in data_jobs:
        jobs.add(job["job_type"])
    return jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job["job_type"] == job_type]
