# import random
#
# f = open('file.txt', 'w')
#
# f.write('foo')
#
# f.write('bar')
#
# f = open("file.txt","r")
# lines = f.read()
# print(lines)
#
# def change(num):
#     num+=1
#     print(f"inner :{num}")
#
# num=5.0
# change(num)
# print(random.randint(1,10))
# print(random.randrange(1,10))
#
# dic={"a":1,"c":2}
# dic.__delitem__("a")
# print(dic)
#
#
# def my_str_to_upper(a_str):
#     a_str = a_str.upper()
#     return a_str
# print(my_str_to_upper('aaa'))
#
# def f(x, y):
#     return(x + y, x - y)
# print(type(f(200, 100)))
# x, y = f(200, 100)
# x,y=(1,2)
# print(x,y)
#
# s = "Preparing for the midterm"
# s[5:8] = "min"
# print(s[5:8])
#

# def target(nums1, nums2):
#     if not nums1 or not nums2:
#         return
#     if len(nums1) < 3 or len(nums2) < 3:
#         nums1[0], nums2[0] = nums2[0], nums1[0]
#         nums1[1], nums2[1] = nums2[1], nums1[1]
#         return
#
# a = [0, 0]
# b = [1, 1]
# target(a, b)
# print(a, b)

a = 11
b = 7
a, b = b, a

print(a)  # Output: 7
print(b)

