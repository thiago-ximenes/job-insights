from src.counter import count_ocurrences


def test_counter():
    cvs_jobs_file = "src/jobs.cvs"

    assert count_ocurrences(cvs_jobs_file, "Javascript") == 122
    assert count_ocurrences(cvs_jobs_file, "Python") == 1639
