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



names_file = open('words.txt', 'r', encoding='utf')
count_pal = 0
for i_line in names_file:
    try:
        word = i_line.strip()
        print(word)
        print(isPalindrome(word))
        if isPalindrome(word) is True and not word.isalpha():
            count_pal += 1
    except ValueError:
        with open("errors.log", "a") as file:
            file.write("Ошибка ValueError: строка содержит число\n")
print(count_pal)

names_file.close()
