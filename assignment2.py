C0901297_month=int(input("Enter a month between 1 and 12:"))
if C0901297_month>0 and C0901297_month<=3:
    print(f"Month {C0901297_month} is in the first quarter.")
elif C0901297_month>3 and C0901297_month<=6:
    print(f"Month {C0901297_month} is in the second quarter.")
elif C0901297_month>6 and C0901297_month<=9:
    print(f"Month {C0901297_month} is in the third quarter.")
elif C0901297_month>9 and C0901297_month<=12:
    print(f"Month {C0901297_month} is in the fourth quarter.")
else:
    print("Error. Month must be between 1 and 12. \nRerun program and try again.")


