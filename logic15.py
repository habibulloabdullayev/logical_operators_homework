def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (a%100+a//100+(a//10)%10)%2==1
print(main(152))
print(main(335))