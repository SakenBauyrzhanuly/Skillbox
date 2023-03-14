

def isPalindrome(s):
    x = list(s)
    y = []
    y.extend(x)
    x.reverse()
    if (x == y):
        return True
    return False


    # Driver Code
text = input('Введите слово: ')
ans = isPalindrome(text)

if ans:
    print("Слово является палиндромом")

else:
    print("Слово не является палиндромом")