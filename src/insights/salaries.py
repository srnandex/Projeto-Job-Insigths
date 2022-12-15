from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    return max([int(job['max_salary'])
                for job in read(path) if (job['max_salary'].isdigit())])


def get_min_salary(path: str) -> int:
    return min([int(job['min_salary'])
                for job in read(path) if (job['min_salary'].isdigit())])


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if (
        type(job.get("min_salary")) is not int
        or type(job["min_salary"]) is not int
        or isinstance(salary, (int, float, str)) is False
        or int(job["max_salary"]) < int(job["min_salary"])
        or ("min_salary" or "max_salary") not in job
    ):
        raise ValueError
    return job["min_salary"] <= int(salary) <= job["max_salary"]


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
