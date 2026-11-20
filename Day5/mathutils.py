"""Provide small math helpers: average, biggest and is_prime."""


def average(nums: list[float]) -> float:
    """Return the mean of a list of numbers.

    Args:
        nums: A list of numbers. May be empty.

    Returns:
        The mean of the numbers, or 0 if the list is empty.
    """
    if not nums:
        return 0
    return sum(nums) / len(nums)


def biggest(nums: list[int]) -> int | None:
    """Return the largest number in a list.

    Args:
        nums: A list of numbers. May be empty.

    Returns:
        The largest number, or None if the list is empty.
    """
    if not nums:
        return None
    return max(nums)


def is_prime(n: int) -> bool:
    """Return whether a number is prime.

    Args:
        n: The whole number to check.

    Returns:
        True if n is prime, otherwise False. Numbers below 2 (0, 1 and
        negatives) are never prime, so they return False.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
