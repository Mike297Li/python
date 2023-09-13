import string
def readFile(fileName):
    try:
      str=open(fileName, "r").read()
      return str
    except Exception:
     print("no such file")
def wordCount(str):
    for i in str:
        if i not in dict:
           dict[i]=0

    for x in dict:
        count=0
        for i in str:
            if x==i:
               count+=1
        dict[x]=count
    return dict

dict={}
fileName=input("enter the name of a text file they want to analyze.").lower()
wordStr=readFile(fileName)
if wordStr==None:
    print("no such file,please check your input")
else:
    translator = str.maketrans('', '', string.punctuation)
    # Use translate() to remove punctuation marks
    wordStr = wordStr.translate(translator)
    # Ignore the case sensitivity
    list = wordStr.lower().split()
    # sorted alphabetically
    list.sort()
    dict=wordCount(list)
    totalCount=0
    print("Word frequencies：")
    print("-------------------------------")
    for x in dict:
        print(f"{x} : {dict[x]}")
        totalCount+=dict[x]
    print(f"the total words in the file :{totalCount}")

