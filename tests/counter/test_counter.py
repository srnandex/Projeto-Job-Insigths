from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences('data/jobs.csv', 'javascript') == 122
    assert count_ocurrences('data/jobs.csv', 'senior') == 1791