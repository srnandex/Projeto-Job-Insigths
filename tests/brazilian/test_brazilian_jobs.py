from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    mock = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    assert mock[0] == {
        "title": "Maquinista",
        "salary": "2000",
        "type": "trainee",
    }
    assert mock[1] == {
        "title": "Motorista",
        "salary": "3000",
        "type": "full time",
    }
    assert mock[2] == {
        "title": "Analista de Software",
        "salary": "4000",
        "type": "full time",
    }
