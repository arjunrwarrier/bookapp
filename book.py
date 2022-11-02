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
    print("6. Search book starting with a specific letter")
    print("7. Display total books in each cateogory")
    print("8. View books from a specific category")
    print("9. Display the totalamount for a book on return date")
    print("10.exit")


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
        bname = input("Enter the bookname to search: ")
        sql = "SELECT `bookname`, `author`, `language`, `category`, `charge/day` FROM `books` WHERE `bookname`='"+bname+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)

    elif (choice == 4):
        print("updating book")
        bname = input("Enter book name: ")
        bauthor = input("Enter author to update: ")
        blanguage = input("Enter the book language to update: ")
        bcategory = input("Enter the book category to update: ")
        bcharge = input("Enter the bookcharge/day to update: ")

        sql = "UPDATE `books` SET `author`='"+bauthor+"',`language`='"+blanguage+"',`category`='"+bcategory+"',`charge/day`='"+bcharge+"' WHERE `bookname`='"+bname+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("Book data updated successfully.")


    elif(choice == 5):
        print("delete a book")
        bname = input("Enter the book name to delete: ")
        sql = "DELETE FROM `books` WHERE `bookname`='"+bname+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("Book data deleted successfully.")

    elif(choice == 6):
        print("Search a book by letter")
        bletter = input("Enter the letter to search: ")
        sql = "SELECT `bookname`, `author`, `language`, `category`, `charge/day` FROM `books` WHERE `bookname` LIKE '"+bletter+"%'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)

    elif(choice ==7):
        print("Total number of books in each category")
        sql = "SELECT COUNT(*)AS total, category FROM books GROUP BY category"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    
    elif(choice == 8):
        print("View book from a specific category")
        bcategory = input("Enter the category to view books:")
        sql = "SELECT * FROM `books` WHERE `category` = '"+bcategory+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice ==9):
        print("Display the totalamount for a book on return date")
        sql = "SELECT i.userid,i.bookid,i.issuedate,i.returndate,DATEDIFF(i.returndate,i.issuedate) AS datediff,DATEDIFF(i.returndate,i.issuedate)*b.`charge/day` AS amount from issue i JOIN books b ON i.bookid = b.id"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i) 
            
    elif(choice==10):
        break