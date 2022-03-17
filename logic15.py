def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd""All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    sum = 0
    sum += a % 10
    a /= 10

    sum += a % 10
    a /= 10

    return sum % 2 == 1
