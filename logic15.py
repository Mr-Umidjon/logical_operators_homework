def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """

    return (a % 10 + a // 100 + a % 100 // 10) % 2 == 1
