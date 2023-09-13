def transfer(roman:str):
    dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    # dict["I"]=1
    # dict["V"] = 5
    # dict["X"] = 10
    # dict["L"] = 50
    # dict["C"] = 100
    # dict["D"] = 500
    # dict["M"] = 1000
    # list_a=list(roman)
    num=0
    i = 0
    while i < len(roman):
     for _ in range(len(roman)):
        if(i>=len(roman)):
             return num
        if(i+1>=len(roman)):
            num += dict[roman[i]]
            return num
        elif( dict[roman[i]]>= dict[roman[i+1]]):
            num +=  dict[roman[i]]
            i+=1

        elif ( dict[roman[i]] <  dict[roman[i+1]]):
            num += ( dict[roman[i+1]]- dict[roman[i]])
            i+=2
    return num

print(transfer("LVIII"))