#CODE FOR BORROW FUNCTION OF THE COURSEWORK

import DateTime as dt #importing DateTime file of our code
import Splitted as sp #importing Splitted file of our code

#Borrow function is created to run the book borrowing part of the program
def Borrow(): 

    #showBooks function is created to display the available books in the stock of the library
    def showBooks(): 
        print("\n") 
        for i in range(len(sp.bookNames)): 
            print( i, "-" * 80, sp.bookNames[i], "\n") 

    #here first name of user is asked until and unless user gives appropriate alphabetical values
    while True:
        fname = input(" \nEnter your first name: ") 
        if fname.isalpha() == True:
            break
        else:
            print("\nPlease enter alphabetical values only!!") 

    #here last name of user is asked until and unless user gives appropriate alphabetical values        
    while True:
        lname = input(" \nEnter your last name: " )
        if lname.isalpha() == True:
            break
        else:
            print("\nPlease enter alphabetical values only!!")
            

    filename = fname + "borrow.txt"  #name of the borrow file which is generated
    fileBookBorrowed = fname + "bookBorrowed.txt" 
    
    #setup display of our borrow file is created here
    with open(filename, "w+") as files:
        files.write("                      Library Management System For Patan Library \n")
        files.write("                           Borrowed by: " + fname + " " + lname + "\n")
        files.write("                                Borrowed Date: " + str(dt.currentDateTime()) + "\n\n\n\n\n")
        files.write("S.N\t\t\t\tBookName\t\t\t\tAuthorName \n")

    showBooks() #showBooks function is called here
    count = 1 #no of books borrowed are counted to assign the S.N no to the borrow file
    books_already_chosen = [] #name of the books which are borrowed is stored here
    nameBookBorrowed = []  #name of the books which are borrowed
    TotalPriceForBorrw = 0
    while True:

        try:
            book_index = int(input('Enter the index of the book that you want to borrow ')) #asking the book number from user to borrow book

        except ValueError: #exception handling if user gives alphabetical values
            print('\nInvalid Literal.Please try again.\n')
            showBooks()
            continue
        
        if book_index < 0 or book_index >= len(sp.bookNames): #checking if the input given by user is within the range or not
            print(" \nBook Index out of range")
            showBooks()
            continue
        
        if sp.bookNames[book_index] in books_already_chosen: #if same book is borrowed twice, this is handeled here
            print(' \nYou cannot borrow same book twice \n')
            continue
        else:
            pass

        books_already_chosen.append(sp.bookNames[book_index]) #appending the bookname which was borrowed to books_already_chosen variable
        nameBookBorrowed.append(sp.bookNames[book_index]) #appending the bookname which was borrowed to nameBookBorrowed variable

        if sp.availableQuantity[book_index] > 0: #checking whether the book is in our stock or nor
            print(' \nThis book is available \n')
            TotalPriceForBorrw += sp.pricePerBorrow[book_index]

            #writing to previously created borrow file,writing the details about the book borrowed
            with open (filename, "a") as f:
                f.write(str(count) + "\t\t\t\t" + sp.bookNames[book_index] + "\t\t\t\t" +  sp.authorNames[book_index] + "\n")
                count += 1
            

            sp.availableQuantity[book_index] = sp.availableQuantity[book_index] - 1 #decreasing the quantity in stock of the book which was borrowed

            #rewriting the stock file with the updated values
            with open('Stock.txt' , 'w+') as f:
                for x in range(len(sp.bookNames)):
                    f.write(sp.bookNames[x]+','+ sp.authorNames[x]+','+ str(sp.availableQuantity[x])+','+'$'+ str(sp.pricePerBorrow[x]) + "\n") 
        else:
            print('This book stock is finished and unavailable for borrowing!!')
            print("Thankyou for using our library")
            break
        if set(books_already_chosen) == set(sp.bookNames): #program to exectue if you borrowed all the books available in the library
            print('\nOkay you are done.')
            print(' \nThis are all the books that you can borrow. we have no other books in stock\n')
            break

            
        #this loop asks whether user wants to borrow another book or not
        while True:
            print("Do you want to borrow another book, 'y' for Yes and 'n' for No. However you cannot borrow the previously borrowed book: ")
            choice = input(" \nEnter your choice: ")
            if choice.isalpha() == True:
                break
            else:
                print('\nOops! Your input is invalid')
                continue
            
        if choice.lower() == 'y' or choice.lower() == "yes": #if user wants to borrow another book, this part is run
            showBooks()
            continue 
        elif choice.lower() == 'n' or choice.lower() == 'no': #if user does not want to borrow another book, this part is run
            print("\nThankyou for using our library\n")
            break

        else: #if the user gives unwanted words, then user cannot borrow any other book and user is taken back to index page
            print("\nYou have entered invalid words \n")
            print("Thankyou for using our library\n")
            break
    with open(fileBookBorrowed, "w") as f:
        f.write(str(nameBookBorrowed))
    if TotalPriceForBorrw > 0:
        with open (filename, "a") as f:
             f.write("\n\n\n Total Price: " + str(TotalPriceForBorrw) + "\n\n\n")


        with open(filename, "r") as f:
            print("-" * 100)
            for lines in f:

                print(lines)
            print("-" * 100)
            print("\n\n")



        

        
        


