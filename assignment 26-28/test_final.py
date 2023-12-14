import final_functions as ff


def test_min_max_sum():
    assert ff.min_max_sum(1, 2, 3) == (1, 3, 6)
    assert ff.min_max_sum(5, 4, 7) == (4, 7, 16)


def test_min_max_sum_improved():
    assert ff.min_max_sum_improved(5, 4, 7) == (4, 7, 16)
    assert ff.min_max_sum_improved(3, 7, 97, 234, 32) == (3, 234, 373)


def test_if_elif_else():
    assert ff.if_elif_else(4) == "Your number is less than 5."
    assert ff.if_elif_else(7) == "Your number is less than or equal to 10."
    assert ff.if_elif_else(23) == "Your number is greater than 10."


# Test for the purposefully bugged function
def test_min_max_sum_improved_bug():
    assert ff.min_max_sum_improved_bug(5, 4, 7) == (4, 7, 16)
    assert ff.min_max_sum_improved_bug(3, 7, 97, 234, 32) == (3, 234, 373)
