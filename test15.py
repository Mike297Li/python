# str="hello"
# print(13 // 2)
# def example(a):
#
#   a = a + '2'
#   a = a*2
#   return a
# print(float(4+int(2.39)%2))
#
# i = 1
# while True:
#   if i%3 == 0:
#     break
#   print(i)
#   i+= 1
#
# string = "my name is x"
# str=string.split()
# for i in string.split():
#      print (i, end=", ")
#
# names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
# names2 = names1
# names3 = names1[:]
# names2[0] = 'Alice'
# names3[1] = 'Bob'

# sum = 0
# for ls in (names1, names2, names3):
#     if ls[0] == 'Alice':
#         sum += 1
#     if ls[1] == 'Bob':
#         sum += 10
# print(sum)
#
# list1 = [13, 3, 23]
# list2 = [13, 3]
# print(list1 < list2)
#
# listExample=[3, 4, 5, 20, 5, 25, 1, 3]
# listExample.pop()
# print(listExample)
#
#
# def increment_items(L, increment):
#     i = 0
#     while i < len(L):
#         L[i] = L[i] + increment
#         i = i + 1
#     return L

# values = [1, 2, 3]
# print(increment_items(values, 2))
# print(values)

# data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
#
# def ttt(m):
#    v = m[0][0]
#    for row in m:
#       for element in row:
#           if v < element: v = element
#    return v
#
# print(ttt(data[0]))

# a= [1, 2, 3, 4, 5]
# for i in range(1, 5):
#     a[i-1] = a[i]
#     for i in range(0, 5):
#         print(a[i])

# def get_values():
#     return 1, 2, 3
#
# a, b, c = get_values()
# print(get_values())
#
# def get_coordinates():
#     x = 10
#     y = 20
#     return x, y
#
# result = get_coordinates()
# print(result)

# var = 10
# for i in range(10):
#     for j in range(2, 10, 1):
#         if var % 2 == 0:
#             continue
#             var += 1
#             var+=1
#         else:
#             var+=1
# print(var)
#
# x = 0
# for i in range(10):
#     for j in range(-1, -10, -1):
#         x += 1
# print(x)
#
# for num in range(10, 14):
#     for i in range(2, num):
#         if num%i == 1:
#             print(num)
#             break

x = 50  # Global variable 'x' with initial value 50

# def sum(*args):
#     '''Function returns the sum
#     of all values'''
#     r = 0
#     for i in args:
#         r += i
#     return r
# print(sum.__doc__)
# print(sum(1, 2, 3))
# print(list("hello"))

# m = [[x, y] for x in range(0, 4) for y in range(0, 4)]
# print(m)

# num = ['One', 'Two', 'Three']
# for i, x in enumerate(num):
#     print(format(i, x))
#
# a='what if a life'
# a.split("a")
# print(a.split("a"))
# list=[1,2,3]
# print(tuple(list))

# dict={1:2,"1":2,"dd":2}
# d = {1: "one", 2: "three"}
# d1 = {2: "two"}
#
# # updates the value of key 2
# d.update(d1)
#
# print(d)
# d1 = {3: "three"}
# # adds element with key 3
# d.update(d1)
# print(d)

# string='lambton'
#
# for i in range(len(string)):
#     print(string[i])
#     string='a'


# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
# # Example usage
# string_list = ["banana", "apple", "grape", "cherry", "date"]
# bubble_sort(string_list)
# print(string_list)
arr=['a','b',3]
for i in range(len(arr)):
    print(f"i===={i}")
    print(arr[i])
    arr.pop(i)
