def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """

    return 9 < x < 100 and x == x % 10 * 10 + x // 10 or 99 < x < 1000 and x == x % 10 * 100 + x % 100 // 10 * 10 + x // 100


print(main(10))
