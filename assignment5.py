from datetime import date

dateInput=input("please enter the name of the month as a string, followed by a space and the day within the month as an integer")
monthList=['January','February','March','April','May','June','July','August','September','October','November','December']
list=dateInput.split(" ")
for i in range(len(monthList)):
    if monthList[i] == list[0]:
        month=(i+1)
monthInt=int(month)
dayInt=int(list[1])
today = date.today()
year=today.year
if date(year,monthInt,dayInt)>=date(year,3,20) and date(year,monthInt,dayInt)<date(year,6,21):
    print("Spring")
elif date(year,monthInt,dayInt)>=date(year,6,21) and date(year,monthInt,dayInt)<date(year,9,22):
    print("Summer")
elif date(year,monthInt,dayInt)>=date(year,9,22) and date(year,monthInt,dayInt)<date(year,12,21):
    print("Fall")
elif date(year,monthInt,dayInt)>=date(year,12,21) or date(year,monthInt,dayInt)<date(year,3,20):
    print("Winter")
else:
    print("wrong value")
