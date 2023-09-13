start=int(input("Please enter one positive integers, start:"))
end=int(input("Please enter another positive integers, end:"))
sum=0
for i in range(start,end+1):
    if(i %2 !=0):
        sum+=i
print(f"the sum of all the odd numbers from start up to and including end : {sum}")



