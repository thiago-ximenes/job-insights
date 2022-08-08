from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    csv_report = read(path)

    return {jobs["job_type"] for jobs in csv_report}


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    get_job_type = [job for job in jobs if job["job_type"] == job_type]
    return get_job_type


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    csv_report = read(path)

    return {jobs["industry"] for jobs in csv_report if jobs["industry"] != ""}


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    csv_reports = read(path)
    max_salary = 0
    for jobs in csv_reports:
        get_salary = int(
            jobs["max_salary"] if jobs["max_salary"].isdigit() else 0
        )
        if get_salary > max_salary:
            max_salary = get_salary

    return max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    csv_reports = read(path)

    for job in csv_reports:
        if job["min_salary"].isdigit():
            min_salary = int(job["min_salary"])
            break

    for job in csv_reports:
        get_salary = int(
            job["min_salary"] if job["min_salary"].isdigit() else min_salary
        )
        if get_salary < min_salary:
            print(min_salary)
            min_salary = get_salary
    return min_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        MIN_SALARY = int(job["min_salary"])
        MAX_SALARY = int(job["max_salary"])

        if MIN_SALARY > MAX_SALARY:
            raise ValueError()

        return MIN_SALARY <= salary <= MAX_SALARY
    except (TypeError, KeyError):
        raise ValueError()


def filter_by_salary_range(jobs, salary):
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
    salary_range_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salary_range_jobs.append(job)
        except ValueError:
            continue

    return salary_range_jobs
