m=[1,2,3]
n=[2,3,1]
print(id(m[0]))
print(id(m[1]))
print(id(m[2]))
print(id(n[0]))
print(id(n[1]))
print(id(n[2]))
# print(type(n[2]))
# class Car:
#     def __init__(self,name):
#         self.name=name
#
#
# car1=Car("bmw")
# car2=Car("bmw")
# print(id(car1)==id(car2))

# # Create two integers
# a = 42
# b = 42
#
#
# # Check the IDs of the integers
# print(id(a))
# a=a+1;
# print(id(a))
#
# # Create a list and store the integers in it
# num_list = [a, b]
#
# # Check the IDs of the elements in the list
# print(id(num_list[0]))
# print(id(num_list[1]))

dict={"1":[1,2,3],"2":"3"}
print(dict.get("2"))