import math
from _ast import Del


def com(a,b=5,c=10):
    a=a+1
    return b

# '''print(com(10,10))'''
# print('We\'re going skiing this winter.')
#
# long_string = "This is a very long string that "\
#               "spans multiple lines using the \ncontinuation character."
# print(long_string)


# a = (1, 2)
# print(a[0:])
# b = [ ]
#
# b[0:] = a[0:]
#
# b.append(3)
#
# print(b)
#
# x = 'There are %s types of people in the world.' %10
#
# print(x)
#
# a = 'Bob'
#
# b = 'Smith'
#
# print("Hello %2s %s!" % (a, b))
#
# print("Hello %s, I see you are %05.2f years old" % ('Bob', 9))
#
# print("%08.2f" % 10.50)
#
#
# print("%2s" % 'Smith and Wesson')
#
# print('%x' %54)
#
# def my_function(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#
# data = {'name': 'Alice', 'age': 30}
# my_function(**data)
#
#
# def my_function(*args):
#     for arg in args:
#         print(arg)
#
# numbers = [1, 2, 3]
# my_function(*numbers)  # Equivalent to my_function(1, 2, 3)

f = open('file.txt', 'w')

f.write('foo')

f.write('bar')
f2 = open('file.txt', 'r')

print(f2.read())
