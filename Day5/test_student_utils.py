from student_utils import average, highest, lowest, pass_rate, summarise

MARKS = [88, 92, 79, 40]


def test_average_basic():
    assert average(MARKS) == 74.75


def test_average_empty():
    assert average([]) is None


def test_average_single():
    assert average([55]) == 55


def test_average_floats():
    assert average([1.5, 2.5]) == 2.0


def test_highest_basic():
    assert highest(MARKS) == 92


def test_highest_empty():
    assert highest([]) is None


def test_highest_all_equal():
    assert highest([70, 70, 70]) == 70


def test_lowest_basic():
    assert lowest(MARKS) == 40


def test_lowest_empty():
    assert lowest([]) is None


def test_pass_rate_all_pass():
    assert pass_rate(MARKS) == 100.0


def test_pass_rate_exactly_at_pass_mark():
    assert pass_rate([40]) == 100.0


def test_pass_rate_none_pass():
    assert pass_rate([10, 20, 30]) == 0.0


def test_pass_rate_mixed():
    assert pass_rate([88, 92, 79, 30]) == 75.0


def test_pass_rate_empty():
    assert pass_rate([]) == 0.0


def test_pass_rate_custom_pass_mark():
    assert pass_rate([50, 60], passing=55) == 50.0


def test_summarise_basic():
    assert summarise(MARKS) == {
        "count": 4,
        "average": 74.75,
        "highest": 92,
        "lowest": 40,
        "pass_rate": 100.0,
    }


def test_summarise_empty():
    assert summarise([]) == {
        "count": 0,
        "average": None,
        "highest": None,
        "lowest": None,
        "pass_rate": 0.0,
    }
