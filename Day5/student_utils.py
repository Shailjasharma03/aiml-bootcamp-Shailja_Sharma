"""Provide small helpers for analysing a student's marks."""


def average(marks: list[float]) -> float | None:
    """Return the mean of a list of marks.

    Args:
        marks: A list of marks. May be empty.

    Returns:
        The mean mark, or None if the list is empty.
    """
    if not marks:
        return None
    return sum(marks) / len(marks)


def highest(marks: list[float]) -> float | None:
    """Return the highest mark in a list.

    Args:
        marks: A list of marks. May be empty.

    Returns:
        The highest mark, or None if the list is empty.
    """
    return max(marks, default=None)


def lowest(marks: list[float]) -> float | None:
    """Return the lowest mark in a list.

    Args:
        marks: A list of marks. May be empty.

    Returns:
        The lowest mark, or None if the list is empty.
    """
    return min(marks, default=None)


def pass_rate(marks: list[float], passing: float = 40) -> float:
    """Return the percentage of marks that reach the pass mark.

    A mark equal to the pass mark counts as a pass.

    Args:
        marks: A list of marks. May be empty.
        passing: The lowest mark that counts as a pass. Defaults to 40.

    Returns:
        The pass rate from 0.0 to 100.0, or 0.0 if the list is empty.
    """
    if not marks:
        return 0.0
    passed = sum(1 for mark in marks if mark >= passing)
    return passed / len(marks) * 100


def summarise(marks: list[float], passing: float = 40) -> dict[str, float | None]:
    """Return a summary of a list of marks.

    Args:
        marks: A list of marks. May be empty.
        passing: The lowest mark that counts as a pass. Defaults to 40.

    Returns:
        A dict with the keys count, average, highest, lowest and pass_rate.
        For an empty list, count is 0, pass_rate is 0.0 and the other
        values are None.
    """
    return {
        "count": len(marks),
        "average": average(marks),
        "highest": highest(marks),
        "lowest": lowest(marks),
        "pass_rate": pass_rate(marks, passing),
    }
