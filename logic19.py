def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    y1 = x % 10
    x //= 10

    y2 = x % 10
    x //= 10

    y3 = x % 10
    x //= 10
    return (y1 * 100 + y2 * 10 + y3 == y3 * 100 + y2 * 10 + y1) or (
            y2 * 10 + y1 == y1 * 10 + y2)

print(main(11))
