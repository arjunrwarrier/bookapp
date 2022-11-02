import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'librarydb')

mycursor = mydb.cursor()

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
        bname = input("Enter book name: ")
        bauthor = input("Enter author: ")
        blanguage = input("Enter the book language: ")
        bcategory = input("Enter the book category: ")
        bcharge = input("Enter the bookcharge/day: ")
         

        sql = 'INSERT INTO `books`(`bookname`, `author`, `language`, `category`, `charge/day`) VALUES (%s,%s,%s,%s,%s)'
        data = (bname,bauthor,blanguage,bcategory,bcharge)
        mycursor.execute(sql,data)
        mydb.commit()
        print("book data inserted successfully.")
        
    elif(choice == 2):
        print("View books")
        sql = "SELECT * FROM `books`"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
 
    elif(choice == 3):
        print("Searching a book")

    elif (choice == 4):
        print("updating book")

    elif(choice == 5):
        print("delete a book")
       
    elif(choice==6):
        break