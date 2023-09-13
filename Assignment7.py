# the search_book_by_author function
def searchBookByAuthor(booksList:[],authorName:str):
    bookTitleList=[]
    for book in booksList:
        if book.get("bookAuthor")==authorName:
            bookTitleList.append(book.get("bookTitle"))
    return bookTitleList


# the remove_book function
def removeBook(booksList,bookId):
    listBookId=[]
    for book in booksList:
        listBookId.append(book.get("bookId"))
    if bookId not in listBookId:
        print("the provided ID does not exist")
        return booksList
    for book in booksList:
        if book.get("bookId")==bookId:
            booksList.remove(book)
    return booksList

# the add_book function
def addBook(booksList,bookTitle,bookAuthor,bookId):
    bookIdList=[]
    for book in booksList:
        bookIdList.append(book.get("bookId"))
    if bookId in bookIdList:
        print("bookId has already exist")
        return booksList
    dictBook={"bookId":bookId,"bookTitle":bookTitle,"bookAuthor":bookAuthor}
    booksList.append(dictBook)
    return booksList

booksList=[]
addBook(booksList,"title1","author1","bookId1")
addBook(booksList,"title2","author2","bookId2")
addBook(booksList,"title3","author1","bookId3")
print(searchBookByAuthor(booksList,"author2"))







