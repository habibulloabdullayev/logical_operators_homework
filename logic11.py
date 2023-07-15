def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a//100<10 and a//100>0
print(main(3))
print(main(12))
print(main(123))