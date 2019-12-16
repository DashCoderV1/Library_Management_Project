from Book_Modules import *
import os
import time
import getpass

# Welcome Screen
lis = ["1F", "3B", "0F"]
print '\t\t\t\t\tLibrary Management'
scroll = "\n\n\n\n\n\n\n\n\n\n\n\t\t\t"
convey = ["Welcome To Our Project ", "\t\t\t\tOn Library Management", "\t\t\t\t\tMade By Rishi And Krishna"]
for i in range(3):
    os.system("color " + lis[i])
    print scroll[i:],
    for i in convey[:(i + 1)]:
        print i
    time.sleep(1.5)
    os.system("cls")
    print '\t\t\t\t\tLibrary Management'

os.system("color 5f")
for i in range(3):
    os.system("cls")
    print '\t\t\t\t\tLibrary Management'
    print "\n\n\n\n\n\t\t", "UserName",
    user = raw_input()
    print "\n\t\t",
    password = getpass.getpass()

    if user == "Admin" and password == "Admin":
        os.system("cls")
        print '\t\t\t\t\tLibrary Management'
        print "Welcome Admin"
        break

    else:
        raw_input("Wrong Username or Password Try Again")

else:
    raw_input("Exceeded Login Attempt Try Again Later")
    exit()

ky = ""
ky1 = ""
Books = []
Members = []
try:
    fil_handle = open("Books.dat", "r")
    Estring = fil_handle.read()
    ky = Decrytkey(Estring.split("%")[0])
    if not Estring.split("%")[1]:
        raise ZeroDivisionError
    Dstring = decrptor(Estring.split("%")[1], ky)
    Brec = Dstring.split("\n")
    Brec = Brec[0:-1]
    for i in Brec:
        Dat = dgtstring_book(i)
        Books.append(Book(Dat[0], Dat[1], Dat[2], Dat[3], Dat[4], Dat[5], Dat[6], Dat[7]))
    fil_handle.close()

except IOError:
    print "File Not Found"
    print "Creating A Books File"
    raw_input("Enter To Continue")
    ky = KCreator()
    writebook(Books, ky)
except ZeroDivisionError:
    print "No Data In File "

try:
    fil_handle1 = open("Members.dat", "r")
    Estring1 = fil_handle1.read()
    ky1 = Decrytkey(Estring1.split("%")[0])
    if not Estring1.split("%")[1]:
        raise ZeroDivisionError
    Dstring1 = decrptor(Estring1.split("%")[1], ky1)
    Brec1 = Dstring1.split("\n")
    Brec1 = Brec1[0:-1]
    for i in Brec1:
        Dat1 = dgtstring_members(i)
        Members.append(Dat1)
    fil_handle1.close()

except IOError:
    print "File Not Found"
    print "Creating A Members File"
    raw_input("Enter To Continue")
    ky1 = KCreator()
    writemembers(Members, ky1)
except ZeroDivisionError:
    print "No Data In File "

while True:
    os.system("cls")
    print '\t\t\t\t\tLibrary Management'
    print "Enter 1 for Book Menu"
    print "Enter 2 for Issue Menu"
    print "Enter 3 for Member Menu"
    print "Enter 4 for Exiting Program"
    ch = intcheck("Choice", "Integers", True, range(1, 5))
    if ch == 1:
        book_menu(Books, ky)
    elif ch == 2:
        if Books == []:
            raw_input("No Books Added ")
            continue
        if Members == []:
            raw_input("No Members Added")
            continue
        book_issue_menu(Books, Members, ky, ky1)
    elif ch == 3:
        member_menu(Books, Members, ky, ky1)
    elif ch == 4:
        raw_input("Enter To Continue")
        exit()
