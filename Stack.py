my_list=[]

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append("6")
def push(newElement):
    my_list.append(newElement)

def pop():
    my_list.pop(-1)

push(5)
print(my_list)
pop()
pop()
print(my_list)


