# Solution

def isPalindrome(x):
    string = str(x)
    check = string[::-1]

    if string == check:
        return True
    else:
        return False

print(isPalindrome(121))