from filecmp import cmp

import pandas as pd

# mylist = [10, 20, 30, 40, 50]
#
# print(pd.Series(mylist))

# Create a Pandas Series from the list
# series = pd.Series(mylist)
#
# print(series)
#
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 28],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# }
#
# df = pd.DataFrame(data)
# first_and_second_rows = df.loc[[0, 1]]
# print(df.to_string())
# print(df.tail(1))
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 28],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# }
#
# # Create a Pandas DataFrame from the dictionary
# df2 = pd.DataFrame(data)
#
# print(df2.tail())


# import pandas as pd
#
# # Create a sample DataFrame with missing values
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'Age': [28, None, 28, 35, 22]  # Note the missing value (None)
# }
#
# df = pd.DataFrame(data)
#
# # Remove rows with empty cells
# df_cleaned = df.dropna(inplace=True)
# df_filled = df.fillna(0)
#
# #print(df_cleaned)
# print(df["Age"].mode())


#Create a sample DataFrame
# data = {
#     'Category': ['A', 'B', 'A', 'C', 'B', 'A'],
#     'Value': [10, 20, 10, 30, 20, 20]
# }
#
# df = pd.DataFrame(data)
#
# # Find the mode of the 'Category' column
# #mode_result = df['Category'].mode()
#
# #print(df.drop_duplicates())
#
# correlation_matrix = df.corr()
# print(correlation_matrix)


import pandas as pd

# Create a sample DataFrame
# data = {
#     'Age': [25, 30, 28, 35, 22],
#     'Income': [50000, 60000, 55000, 75000, 45000],
#     'Experience': [3, 5, 4, 7, 2]
# }
#
# df = pd.DataFrame(data)
#
# # Calculate the correlation matrix
# correlation_matrix = df.corr()
#
# # Display the correlation matrix
# print(correlation_matrix)
my_list = [1, 2, 3]
another_list = [4, 5, 6]

my_list.extend(another_list)
my_list.insert(0,1)
my_list.remove(1)
my_list.pop()
#cmp(my_list, another_list)
print(my_list)

s1 = set(['a', 'b', 'c', 'd'])
print(s1)
myList = [1, 2, 3, 1, 2, 3, 4 ,4 ,4]
s2 = set(myList)
print(s2)