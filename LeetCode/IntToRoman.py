def intToRoman(input:int):

    dict={"M":1000,"CM": 900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL": 40,"X":10,"IX": 9,"V":5,"IV":4,"I":1}
    roman = ''
    for x in dict:
        count=0
        count=int(input/dict[x])
        while count>0:
              roman=roman+x
              count-=1
              input=input-dict[x]
    return roman
print(intToRoman(3))