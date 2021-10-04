#this is the main page of our program, where all the functions are called and this page is run in terminal

import Borrow as b #importing borrow file of our code
import Return as r #importing return file of our code

#welcome line of the program
print("-" * 100)
print("\n\nWELCOME TO PATAN LIBRARY PORTAL\n\n")
print("-" * 100)

#showDetails function is created, this function tells user to whether to borrow or return book or exit the program
def showDetails():

    print("1  " + "-"*40 +  " Borrow Book \n") 
    print("2  " + "-"*40 +  " Return Book \n")
    print("3  " +"-"*40 + " Exit\n")

print("\n Please Follow the following instructions given below, to do that specific task  \n")

showDetails() #show details function is called here

#this loop runs until and unless user exits from the program
while True:

    #this loop ask the input from user and runs until and unless user gives appropriate input
    while True:
        try: #exception handling is done, if user gives inaapropriate input
            choice = int(input("\n\nEnter the numbers shown above to do that task:  "))
            break
        except:
            print("please enter numerical values only! ")
            showDetails()
            continue

    #if user gives 1 as input, borrow book function is called and user is taken to borrow file
    if choice == 1:
        b.Borrow()
        showDetails()
        continue

    #if user gives 2 as input, return book function is called and user is taken to return file
    elif choice == 2:
        r.Return()
        showDetails()
        continue

    #if user gives 3 as input, user is taken out of the program
    elif choice == 3:
        print("\nThankyou for using our library portal\n")
        break
    
    #if user gives any other numbers then suggested, then user is again asked for the number
    else:
        print("\nPlease only enter the numbers shown above!!\n")
        showDetails()
        continue
       



    
        




  