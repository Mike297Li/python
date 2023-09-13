from random import random, randint

randomNum=randint(1,100);
print(randomNum)
yourNum=int(input("please enter"))
while randomNum!=yourNum:
    if(yourNum>randomNum):
        print("greater than")
    else:
        print("less than")
    yourNum = int(input("please enter"))
print("congratulations")

