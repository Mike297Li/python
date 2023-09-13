

def isValid(number,num):
    flag=False
    if num==1:
        if(number>=7.5 and number <=18.25):
            flag=True
    if num==2:
        if(number >=0 and number <=40):
            flag=True
    return flag

hourlyPayRate=float(input("please enter hourlyPayRate"))


while isValid(hourlyPayRate,1)==False:
      print("error hourlyPayRate")
      hourlyPayRate =float( input("please enter hourlyPayRate"))


numberOfHour=float(input("an employee’s the number of hours worked"))
while isValid(numberOfHour,2)==False:
      print("error the number of hours worked")
      numberOfHour =float( input("please enter the number of hours worked"))

grossPay= numberOfHour* hourlyPayRate
print(f"grossPay====={grossPay}")