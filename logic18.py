def main(a):
    """Given a five-digit integer a, check the following statement "All digits of the number are in descending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x1 = a % 10
    a //= 10

    x2 = a % 10
    a //= 10

    x3 = a % 10
    a //= 10

    x4 = a % 10
    a //= 10

    x5 = a % 10
    a //= 10
    return x1 > x2 > x3 > x4 > x5
