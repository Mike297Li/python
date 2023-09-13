def rank(array,mark):
     rank=1
     for i in array:
         if i>mark:
             rank=rank+1
     return rank
array=[]
for i in range(5):
    mark = int(input("please enter mark"))
    array.append(mark)

for i in array:
    result=rank(array,i)
    print(f"{i}==rank=={result}")

# def existInArray(array,mark):
#     for i in array:
#         if i==mark:
#             return True
#     return False
#
# def distinctArray(array,size,arrayForDistinct):
#     for i in array:
#         for index in range(size):
#             if i==array[index] and not(existInArray(array,i)):
#                 count=0
#                 distinctArray[count]=i
#                 count=count+1
#
#     return distinctArray
#
# array=[]
# for i in range(5):
#     mark = int(input("please enter mark"))
#     array.append(mark)
#
# arrayForDistinct=[]
# distinctArray(array,5,arrayForDistinct)
#
# for i in arrayForDistinct:
#     print(i)
#
# for i in array:
#     result=rank(array,i)
#     print(f"{i}==rank=={result}")
#


