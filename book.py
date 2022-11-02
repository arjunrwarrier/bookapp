while True:
    print("Select an option from the menu ")
    print("1. Add a book")
    print("2. View all books")
    print("3. Search a book")
    print("4. Update a book")
    print("5. Delete a book")
    print("6.exit")

    choice = int(input("Enter an option: "))
    if(choice == 1):
        print("book enter selected")
        
    elif(choice == 2):
        print("View book")
 
    elif(choice == 3):
        print("Searching a book")

    elif (choice == 4):
        print("updating book")

    elif(choice == 5):
        print("delete a book")
       
    elif(choice==6):
        break