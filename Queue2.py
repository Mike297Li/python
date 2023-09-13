my_list=[]

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
def push(newElement):
    my_list.append(newElement)
def pop():
    my_list.pop(0)

push(5)
pop()
print(my_list)
