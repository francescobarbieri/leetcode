# First solution

numDict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

specialDict = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}   

output = 0

def romanToIntFirst(s):
    global output
    if len(s) == 1:
        output += numDict[s]
    elif len(s) < 1:
        return output
    else:
        check = s[0] + s[1]
        if check in specialDict:
            output += specialDict[check]
            romanToIntFirst(s[2:])
        else:
            output += numDict[s[0]]
            romanToIntFirst(s[1:])
    return output

#print(romanToIntFirst("LVIII"))

# Second soluton:

def romanToIntSecond(s):
    index = 0
    output = 0

    for i in range(len(s)):
        if i + 1 < len(s) and numDict[s[i]] < numDict[s[i+1]]:
            output -= numDict[s[i]]
        else:
            output += numDict[s[i]]

    return output

#print(romanToIntSecond("MCMXCIV"))