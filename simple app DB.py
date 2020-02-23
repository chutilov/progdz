#------------------------------------------
#   Program by Andrii C.
#
#
#
#   Version
#     0.1
#
#------------------------------------------
import mysql.connector

# Connecting into our DB, you need to provide your database information
DB = mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="",
                             database="")

# here cursor is a storage for requests that we send by functions below
my_cursor = DB.cursor(buffered=True)

# After From you need to provide the name of your database
my_cursor.execute("SELECT * From ...")


action = str(input("Enter phrase to choose the action: "))


# part for ADD
if action == "ADD":
    name_example = str(input("Please enter the name for adding: "))

    # after INTO you need to provide your name of the table from DB
    # and more : name means that you need to create the column in your empty DB named name
    my_cursor.execute("INSERT INTO ... (name) VALUES (%s)", name_example)

    # saving the information of DB changes:
    # if you have another name of your database you just need to provide it...
    DB.commit()


# part for ALL
elif action == "ALL":
    my_cursor.execute("SELECT name From ... where name")

    for names in my_cursor.fetchall():
        print(names, end=", ")
    print("END...")


# part for SEARCH
elif action == "SEARCH":
    name = str(input("Enter name to search into the DB: "))

    # again write an example of ur DB after phrase FROM
    my_cursor.execute("SELECT name_user FROM ... where name_user = name")

    for names in my_cursor.fetchall():
        # print(names, end="\n")
        names_inf = []

        names_inf.insert(names)
        for name_in in names_inf:
            print(name_in, end="\n")
        print("Completed!!!")



