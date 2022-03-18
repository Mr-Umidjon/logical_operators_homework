def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    s = 0
    n1 = n
    x1 = n % 10
    n //= 10
    s += x1

    x2 = n % 10
    n //= 10
    s += x2

    x3 = n % 10
    n //= 10
    s += x3

    x4 = n % 10
    n //= 10
    s += x4

    x5 = n % 10
    n //= 10
    s += x5

    return 10000 <= n1 <= 99999 and s >= 3 or 1000 <= n1 <= 9999 and s >= 3 or 100 <= n1 <= 999 and s >= 2 or 10 <= n1 <= 99 and s >= 2 or s == 1 and 1 <= n1 <= 9


print(main(110))
