from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path_to_file = "tests/mocks/brazilians_jobs.csv"
    new_dict = read_brazilian_file(path_to_file)
    for key in new_dict:
        assert "title" in key
        assert "titulo" not in key

        assert "salary" in key
        assert "salario" not in key

        assert "type" in key
        assert "tipo" not in key
