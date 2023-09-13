# Define an empty list called my_list.
mylist=[]
# Prompt the user to enter five numbers, one at a time, and append each number to my_list.
for i in range (0,5):
    mylist.append(int(input("enter one numbers(five times):")))
# Print my_list.
print(mylist)
# Print the second element in my_list.
print(mylist[1])
# Print the last element in my_list
print(mylist[-1])
# Print the third to fifth elements in my_list using list slicing.
print(mylist[2:])
# Create another list called new_list with the elements [7, 8, 9, 10].
new_list=[7, 8, 9, 10]
# Concatenate my_list and new_list into a new list called combined_list.
combined_list=mylist+new_list
print(combined_list)
# Use the len() function to print the length of combined_list.
print(len(combined_list))
#  Append the number 11 to combined_list.
combined_list.append(11)
# Sort combined_list in ascending order.
combined_list.sort()
print(combined_list)
#  Count the number of occurrences of the number 7 in combined_list.
print(combined_list.count(7))
# Remove the first occurrence of the number 7 from combined_list.
combined_list.remove(7)
print(combined_list)
# using list comprehension to create a new list called squared_list,the square of an element from combined_list.
squared_list = [x**2 for x in combined_list]

print(squared_list)
