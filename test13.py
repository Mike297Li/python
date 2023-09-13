def find_unique_marks(array):
    unique_marks = []
    for mark in array:
        if mark not in unique_marks:
            unique_marks.append(mark)
    return unique_marks

def rank(array, mark):
    unique_marks = find_unique_marks(array)
    rank = 1
    for unique_mark in unique_marks:
        if unique_mark > mark:
            rank += 1
    return rank

array = []
for _ in range(5):
    mark = int(input("please enter mark: "))
    array.append(mark)

for mark in array:
    result = rank(array, mark)
    print(f"{mark} ==rank== {result}")
