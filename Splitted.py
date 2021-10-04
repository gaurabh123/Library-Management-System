#list is used as data structure in our code, and we have created 4 lists to store 4 different values of our stock file

bookNames = [] #bookNames list to store all the book's name of our stock
authorNames = [] #authorNames list to store all the author name of the books in our stock
availableQuantity = [] #availableQuantity to store all the book's available quantity 
pricePerBorrow = [] #pricePerBorrow to store the prices of borrowing each book in the library

#stock file is opened and approrpriate values are inserted in the corresponding lists
with open ("Stock.txt", "r") as files:
    for lines in files:
        lines = lines.split(",")
        bookNames.append(lines[0])
        authorNames.append(lines[1])
        availableQuantity.append(int(lines[2]))
        pricePerBorrow.append(float(lines[3].strip("$ \n")))