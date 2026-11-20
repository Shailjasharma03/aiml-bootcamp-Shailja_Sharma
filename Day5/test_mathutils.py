from mathutils import average, biggest, is_prime


def test_average_basic():
    assert average([2, 4, 6]) == 4.0


def test_average_empty():
    assert average([]) == 0


def test_average_single():
    assert average([5]) == 5.0


def test_biggest_basic():
    assert biggest([3, 9, 2]) == 9


def test_biggest_empty():
    assert biggest([]) is None


def test_biggest_negatives():
    assert biggest([-5, -2, -9]) == -2


def test_is_prime_two():
    assert is_prime(2) is True


def test_is_prime_seven():
    assert is_prime(7) is True


def test_is_prime_composite():
    assert is_prime(9) is False


def test_is_prime_one():
    assert is_prime(1) is False


def test_is_prime_zero():
    assert is_prime(0) is False


def test_is_prime_negative():
    assert is_prime(-3) is False
