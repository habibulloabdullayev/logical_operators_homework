def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a//10<10 and a//10>0
print(main(3))
print(main(12))