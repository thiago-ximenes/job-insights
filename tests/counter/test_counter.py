from src.counter import count_ocurrences


def test_counter():
    csv_jobs_file = "src/jobs.csv"

    assert count_ocurrences(csv_jobs_file, "Javascript") == 122
    assert count_ocurrences(csv_jobs_file, "Python") == 1639
