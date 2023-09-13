def length_of_longest_substring(input):
    dict={}
    size=0
    i = 0
    for j in range(len(input)):
        if input[j] in dict:
            i=max(i,dict.get(input[j]))
        dict[input[j]]=j+1
        size=max(size,j-i+1)
    return size

result = length_of_longest_substring("abcdababbcbb")
print(result)