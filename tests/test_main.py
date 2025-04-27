from package_name import add_digit


def test_sum_digit():
    assert add_digit(1, 1) == 2
    assert add_digit(10, 1) == 11
    assert add_digit(10, 10) == 20
