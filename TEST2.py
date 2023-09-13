my_str='Boston'
print(id(my_str))
his_str='Boston'
print(my_str==his_str)
print(id(his_str)==id(my_str))
age=63
city='Mississauga'
#print((not age>=65 and city=='NY') OR age>67)

print(f"0: {bool('1')}, 1 {bool(-1)}")


my_array=[2]
if my_array:
    print("888")
else:
    print("999")
print("7777")