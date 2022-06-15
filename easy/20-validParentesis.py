def isValid(s):
    for x in range(len(s)//2):
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
    return len(s) == 0

print(isValid("()[]{}"))