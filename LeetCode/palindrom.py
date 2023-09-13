def isPalindrom(input):
    original=input
    inputList=[]
    if input<0:
        return False
    for i in range(len(str(input))):
        count=int(input / 10 ** (len(str(original)) - (i+1)))
        inputList.append(count)
        input-=  count* (10 ** (len(str(original))- (i+1)))

    palindomNum=0
    for i in range(len(inputList)):
        palindomNum+=(10 ** (len(str(original)) - (i + 1)))*(inputList[len(inputList)-(i+1)])

    return palindomNum-original==0

print(isPalindrom(1211))