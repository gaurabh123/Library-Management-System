#code for return module of our program, here is the code that executes while returning the book

import DateTime as dt #importing datetime module
import Splitted as sp #importing splitted module


def Return(): #creating the main return function, where all the codes of return are written
    totalCost = 0 #initializing totoal cost as 0
    fine = 0 #initializing fine as 0
    SnCount = 0 #initailizing sn count as 0
    borrower_name = input("\nEnter the name of the borrower: ") #asking the name from the user
    fileBorrowName = borrower_name + "Return.txt" #writing the name of the file
    
    #checking whether the name given is in correct format or not
    if borrower_name.isalpha() == True: 
        #using try and except for handling the exception

        try: 
            filename = borrower_name + "bookBorrowed.txt"
            with open(filename, "r") as f:
                for line in f:
                    line = line.replace("[","")
                    line = line.replace("]","")
                    line = line.replace("'","")
                    line = line.split(", ")                 
        except: #if the file does not exixsts this code is run
            print("Your file name is invalid!!") 
            return
            

    else: #if user doesnot give alphabetical values this code runs
        print("Please enter alphabetical values!!")
        Return()

    #Creating the strucuture of return file
    with open(fileBorrowName, "w") as files:
        files.write("                      Library Management System For Patan Library \n")
        files.write("                           Returned by: " + borrower_name + "\n")
        files.write("                                Borrowed Date: " + str(dt.currentDateTime()) + "\n\n\n\n\n")
        files.write("S.N                BookName                        AuthorName\n")

    #running the while loop for displaying the books user had borrowed and which the user can return
    while True:
        SnCount += 1
        if len(line) != 0 and line != ['']:
            for index, word in enumerate(line):
                print(index, "-" * 80 , word ,"\n")
                
            print("\n These are all the books you have borrowed and you can return back!! \n")

        #asking number from user for returning book
            while True:
                try:
                    book_to_return_index = int(input('\nEnter the number of the book that you want to return ')) #asking from user which book to return
                    book_name = line[book_to_return_index] #pulling the name of that book
                    break
                except ValueError: #if invalid input is given this code runs
                    print("Please enter only numerical values!! ")
                    continue
                except IndexError: #if invalid index is given this code runs
                    print("Please enter the number within the index!! ")
                    continue
            line.remove(book_name) #book name is removed from the file
            with open(filename, "w") as f: #file is written once again
                f.write(str(line))


            index = sp.bookNames.index(book_name) 
            sp.availableQuantity[index] = sp.availableQuantity[index] + 1 #since book is returned back, the no of books is increased in stock

            with open(fileBorrowName, "a") as f: #book returned details is written in the file
                f.write(str(SnCount) + "                   " + sp.bookNames[index] + "                            " + sp.authorNames[index] + "\n")

            with open("Stock.txt", "w") as f: #stock file is updated
                for x in range(len(sp.bookNames)):
                    f.write(sp.bookNames[x]+','+ sp.authorNames[x]+','+ str(sp.availableQuantity[x])+','+'$'+ str(sp.pricePerBorrow[x]) + "\n")


            print("\n Is the book return date expired \n")  #it is asked to user, whether the book is returned late
            
            while True: #checking whether the user provides appropriate input 
                choice = str(input("\nPress 'Y' for yes and other for no "))
                if choice.isalpha() == True:
                    break
                else:
                    print("Please enter only alphabetical values!! ")
                    continue

            if choice.lower() == "y" or choice.lower() == "yes": #if the user says yes
                while True: #no of days the book was returned late was asked with the user
                    try:
                        day = int(input("\nHow many days was the book returned late? "))
                        break
                    except ValueError:
                        print("Please enter numerical values only!! ")
                        continue

                fine = day * 1  #fine is calculated
                print("Your fine amount for this book is: $", fine)
                totalCost += sp.pricePerBorrow[index] + fine #total cost of users, book borrow and fine is calculated
 
            else:
                totalCost += sp.pricePerBorrow[index] 


            print('\nReturning.........Your book is returned\n')
            print("-" * 100)



            print("\n Do you want to return more books? ") #user is asked whether user user wants to return another book or not

            while True: #it is checked whether appropriate input is provided or not
                choice = input("\nPress 'Y' for yes and 'N' for no: ")
                if choice.isalpha() == True: 
                    break
                else:
                    print("Please enter alphabetical values only!! \n")
                    continue

            if choice.lower() == "y" or choice.lower() == "yes":    #if users wants to return another book, they are returned to top, for following the same process
                continue
        
            elif choice.lower() == "n" or choice.lower() == "no": #if no, user is taken out of the program
                print("\nThankyou for using our Library!! \n")
                break
                

            else:
                print("\nYou have entered invalid words \n") #invalid inputs are handled here
                print("\nThankyou for using our library \n")
                break
            
        else: 
            print(" \nYou don't have anymore books to return. You have returned all the books!! \n") #if user has returned all the books, they have borrowed, then this code runs
            print("\nThankyou for using our library \n")
            break

    if totalCost > 0: #if the user has total cost then their total cost is returned in the file and this code runs
        with open(fileBorrowName, "a") as files:
            files.write("\n Total Cost Including Fine: " + str(totalCost))

        


