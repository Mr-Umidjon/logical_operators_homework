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
    return (y1 * 1000 + y2 * 10 + y3 == y3 * 1000 + y2 * 10 + y1) and y1 > 0 or (
            y1 * 10 + y2 == y2 * 10 + y1)



