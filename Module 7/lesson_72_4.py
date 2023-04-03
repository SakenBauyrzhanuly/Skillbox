def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    front_side = []
    back_side = []
    x = str(x)
    length = len(x) // 2
    for i in range(length):
        front_side.append(x[i])
    for i in range(len(x) - 1, length, -1):
        back_side.append(x[i])

    if back_side == front_side:
        return True
    else:
        return False


print(isPalindrome(1001))
