def isPalindrom(input):
    strInput=str(input)
    reverseStr = strInput[::-1]
    if reverseStr==strInput:
        return True
    else:
        return False

print(isPalindrom(-10))