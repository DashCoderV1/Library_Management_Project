# INPUT Function
def intcheck(vr_name, vr_format, rangecheck=False, rng=()):
    while True:
        try:
            vr = int(raw_input(vr_name + ":" + " " * (40 - len(vr_name))))
            if rangecheck:
                if vr not in rng:
                    raise EOFError
            return vr
        except EOFError:
            print "Wrong Input Please Enter Values from ", rng[0], " To ", rng[len(rng) - 1]
            print
        except ValueError:
            print "Wrong Input Please Enter Values in " + vr_format
        except:
            print "Please Try Again"


def stgcheck(vr_name, vr_format, symcheck=True):
    while True:
        try:
            vr = raw_input(vr_name + ":" + " " * (40 - len(vr_name)))
            if symcheck:
                for i in vr:
                    if not (ord(i) in range(28,33) or ord(i) in range(65,91) or ord(i) in range(97,123)):
                        raise EOFError
            if len(vr) == 0:
                raise ZeroDivisionError
            return vr
        except ZeroDivisionError:
            print "Cannot Save A Empty Value Try Again"
        except TypeError:
            print "Wrong Input Enter Values in " + vr_format
        except EOFError:
            print "Enter without Symbols Or Numbers"
        except:
            print "Please Try Again"


def UInput(Books):
    bno = bno_random(Books)
    print "Book No. ", bno
    bn = stgcheck(Book.vr[1], "Alphabets (No Symbols) ")
    ban = stgcheck(Book.vr[2], "Alphabets (No Symbols) ")
    bpub = stgcheck(Book.vr[3], "Alphabets (No Symbols)")
    bgnr = stgcheck(Book.vr[4], "Alphabets (No Symbols)")
    bsub = stgcheck(Book.vr[5], "Alphabets (No Symbols) ")
    bprc = intcheck(Book.vr[6], "Integer")
    bilis = []
    return Book(bno, bn, ban, bpub, bgnr, bsub, bprc, bilis)


def UInput1(Members):
    mno = mno_random(Members)
    print "Members No. ", mno
    mn = stgcheck("Member Name", "Alphabets (No Symbols) ")
    madd = stgcheck("Member Address", "Alphabets", False)
    while True:
        mcno = raw_input("Member Contact No." + " "*(40-len("Member Contact No.")))
        try:
            int(mcno)
            if len(mcno) != 10:
                raise ZeroDivisionError
            break
        except:
            print "Wrong Input Please Try Again"
    return Member(mno, mn, madd, mcno, 0, False)


def Confirm_Check(vr):
    while True:
        cn = raw_input(vr + "Y/N :")
        if cn.lower() == "y":
            return True
        elif cn.lower() == "n":
            return False
        else:
            print "Wrong Input Please Try Again"


# KEY Creator
def KCreator():
    import random
    k = ""
    for g in range(4):
        k += chr(random.randint(65, 122))
    return k


# EKEY Or DKEY
def Encrptkey(key):
    Eky = ""
    for p in key:
        Eky += chr(ord(p) + 7)
    return Eky


def Decrytkey(key):
    Dky = ""
    for y in key:
        Dky += chr(ord(y) - 7)
    return Dky


# Book And Member Random Id
def bno_random(books):
    book_vr = []
    for k in books:
        book_vr.append(k.BNo)
    if book_vr == []:
        return 1
    return book_vr[-1]+1



def mno_random(members):
    member_vr = []
    for k in members:
        member_vr.append(k.MId)
    if member_vr == []:
        return 1
    return member_vr[-1]+1



# GET Data Book And Member
def get_string(bk):
    stg = ""
    for m in bk:
        stg += m.gstr() + "\n"
    return stg


# Encrypting And Decrypting
def encryptor(stg, key):
    c = 0
    est = ""
    for i in stg:
        est += chr(ord(i) + ord(key[c]))
        c += 1
        if c == len(key):
            c = 0
    return est


def decrptor(stg, key):
    c = 0
    dst = ""
    for i in stg:
        dst += chr(ord(i) - ord(key[c]))
        c += 1
        if c == len(key):
            c = 0
    return dst


# Data Structure
def dgtstring_members(stg):
    lis = stg.split("@")
    if lis[5]:
        a = True
    else:
        a = False
    return Member(int(lis[0]), lis[1], lis[2], lis[3], int(lis[4]), a)


def dgtstring_book(stg):
    import datetime
    bilist = []
    brec1 = stg.split(",")
    if brec1[7]:
        brec2 = brec1[7].split("<")
        brec2 = brec2[0:-1]
        for h in brec2:
            brec3 = h.split(":")
            d1 = brec3[1].split("/")
            d2 = brec3[2].split("/")
            bilist.append(BIssue(int(brec3[0]), datetime.date(int(d1[0]), int(d1[1]), int(d1[2])),
                                 datetime.date(int(d2[0]), int(d2[1]), int(d2[2])), int(brec3[3])))
    return int(brec1[0]), brec1[1], brec1[2], brec1[3], brec1[4], brec1[5], int(brec1[6]), bilist

def DeleteMID(books, ky, MId):
    for i in books:
        if i.BIsueList:
            for j in range(len(i.BIsueList)):
                if i.BIsueList[j].MId == MId:
                    i.BIsueList.pop(j)
    writebook(books, ky)


# WRITING DATA
def new_write_book(k):
    try:
        file_handle = open("Books.dat", "wb")
        file_handle.write(Encrptkey(k))
        file_handle.close()
    except:
        print "Error File Cannot Be Created "
        raw_input("Enter To Exit")
        exit()

def new_write_members(k):
    try:
        file_handle = open("Members.dat", "wb")
        file_handle.write(Encrptkey(k))
        file_handle.close()
    except:
        print "Error File Cannot Be Created "
        raw_input("Enter To Exit")
        exit()


def writebook(bks, key):
    if not bks:
        new_write_book(key)
    estg = encryptor(get_string(bks), key)
    try:
        file_handle = open("Books.dat", "wb")
        file_handle.write(Encrptkey(key) + "%" + estg)
        file_handle.close()
    except:
        print "Error File Not Responding"
        raw_input("Enter To Exit")
        exit()


def writemembers(members, key):
    if not members:
        new_write_members(key)
    estg = encryptor(get_string(members), key)
    try:
        file_handle = open("Members.dat", "wb")
        file_handle.write(Encrptkey(key) + "%" + estg)
        file_handle.close()
    except:
        print "Error File Not Responding"
        raw_input("Enter To Exit")
        exit()


# USER DISPLAYS
def user_idis(books, cidis):
    count = False
    if cidis:
        print "Issued Books"
        print "Book No.\tBook Name"
        for i in books:
            if len(i.BIsueList) != 0:
                if i.BIsueList[len(i.BIsueList) - 1].issue_check():
                    count = True
                    print i.BNo, i.BName
        print
        
    else:
        print "UnIssued Books"
        print "Book No.\tBook Name"
        for i in books:
            if len(i.BIsueList) != 0:
                if not i.BIsueList[len(i.BIsueList) - 1].issue_check():
                    print i.BNo, i.BName
                    count = True
            else:
                print i.BNo, i.BName
                count = True
        print
    return count


def user_mdis(members, vr='nis'):
    if vr == 'all':
        print "All Members "
        print "Member No.\tMember Name"
        for i in members:
            print i.MId, i.MName
        print
    elif vr == 'nis':
        print "Members That Have not Issued"
        print "Member No.\tMember Name"
        for i in members:
            if i.MIssued is False:
                print i.MId, i.MName
        print


def user_dis(array, vr):
    print vr + " No.", vr + " Name"
    if vr.lower() == "member":
        for i in array:
            print i.MId, i.MName
        print
    else:
        for i in array:
            print i.BNo, i.BName
        print


# Members Function
def Msearch(members, Mno):
    for i in members:
        if i.MId == Mno:
            return i
    else:
        print "Member Id Does not Exists Try Again"
        mno = intcheck("Member Id", "Integers")
        return Msearch(members, mno)



def Mcheck_issue(members, mno):
    for i in members:
        if i.MId == mno:
            if i.MIssued == False:
                return mno
    else:
        print "Member Id Does Not Exists Or Member has already Issued A Book"
        mnop = intcheck("Members ID", "Integers")
        return Mcheck_issue(members, mnop)



# Classes
class Book:
    vr = ["Book No", "Book Name", "Aurthor's Name", "Publisher Name", "Book Genre", "Subject", "Price "]

    def __init__(self, bn, bnm, ban, bpub, bgrn, bsub, bprc, bilis):
        self.BNo = bn
        self.BName = bnm
        self.BAurthor = ban
        self.BPublisher = bpub
        self.BGenre = bgrn
        self.BSubject = bsub
        self.BPrice = bprc
        self.BIsueList = bilis

    def display(self):
        print Book.vr[0] + " " * (40 - len(Book.vr[0])), self.BNo
        print Book.vr[1] + " " * (40 - len(Book.vr[1])), self.BName
        print Book.vr[2] + " " * (40 - len(Book.vr[2])), self.BAurthor
        print Book.vr[3] + " " * (40 - len(Book.vr[3])), self.BPublisher
        print Book.vr[4] + " " * (40 - len(Book.vr[4])), self.BGenre
        print Book.vr[5] + " " * (40 - len(Book.vr[5])), self.BSubject
        print Book.vr[6] + " " * (40 - len(Book.vr[6])), self.BPrice

    def modify(self):
        import os
        while True:
            os.system('cls')
            print "\t\t\t\t\t Library Management"
            print "\t\t\t\t\t Book Menu"
            print "\t\t\t\t\t Modify Menu"
            for i in range(1, len(Book.vr)):
                print i, Book.vr[i]
            print "7 Go Back"
            ch_m = intcheck("Choice", "Integers", True, range(1, 8))
            if ch_m == 1:
                print "\n", Book.vr[1], self.BName
                self.BName = stgcheck("New " + Book.vr[1], "Alphabets (No Symbols) ")
            elif ch_m == 2:
                print "\n", Book.vr[2], self.BAurthor
                self.BAurthor = stgcheck("New " + Book.vr[2], "Alphabets (No Symbols) ")
            elif ch_m == 3:
                print "\n", Book.vr[3], self.BPublisher
                self.BPublisher = stgcheck("New " + Book.vr[3], "Alphabets (No Symbols) ")
            elif ch_m == 4:
                print "\n", Book.vr[4], self.BGenre
                self.BGenre = stgcheck("New " + Book.vr[4], "Alphabets ", False)
            elif ch_m == 5:
                print "\n", Book.vr[5], self.BSubject
                self.BSubject = stgcheck("New " + Book.vr[5], "Alphabets (No Symbols) ")
            elif ch_m == 6:
                print "\n", Book.vr[6], self.BPrice
                self.BPrice = intcheck("New " + Book.vr[6], "Integer ")
            else:
                print "Going Back To Menu"
                break

    def bissue(self, members):
        import datetime
        if not self.BIsueList:
            studentid = Mcheck_issue(members, intcheck("Member ID", "Integers "))
            self.BIsueList.append(BIssue(studentid,
                                         BIssue.tdate(),
                                         "1111-11-11",
                                         -1))
            print "Issue Date:", BIssue.tdate()
            print "Returning Dae", BIssue.tdate() + datetime.timedelta(days=7)
            print "Book Due After Returning Date Rs5"
            for i in members:
                if i.MId ==studentid:
                    i.edit("missued")
        else:
            last_rec = self.BIsueList[len(self.BIsueList) - 1]
            if last_rec.issue_check():
                print "This Book is Already Issued Try Another Book"
            else:
                studentid = Mcheck_issue(members, intcheck("Member ID", "Integers "))
                self.BIsueList.append(BIssue(studentid,
                                             BIssue.tdate(),
                                             "1111-11-11",
                                             -1))
                for i in members:
                    if i.MId == studentid:
                        i.edit("missued")
                print "Issue Date:", BIssue.tdate()
                print "Returning Date", BIssue.tdate() + datetime.timedelta(days=7)
                print "Book Due After Returning Date Rs5"
            print

    def breturn(self, members):
        if not self.BIsueList:
            print "Book is Not Issued"
        else:
            last_rec = self.BIsueList[len(self.BIsueList) - 1]
            if not last_rec.issue_check():
                print "This Book is Not Issued "
            else:
                last_rec.rbook(members)
                self.BIsueList[len(self.BIsueList) - 1] = last_rec
            print

    def gstr(self):
        stg = ""
        stg += str(self.BNo) + "," + self.BName + "," + \
               self.BAurthor + "," + self.BPublisher + "," + self.BGenre + "," + \
               self.BSubject + "," + str(self.BPrice) + ","
        for l in self.BIsueList:
            stg += str(l.MId) + ":" + str(l.BIDate).replace("-", "/") + ":" + str(l.BRDate).replace(
                "-", "/") + ":" + str(l.BDue) + "<"
        return stg


class BIssue:
    def __init__(self, mid, bid, brd, bdue):
        self.MId = mid
        self.BIDate = bid
        self.BRDate = brd
        self.BDue = bdue

    def idisplay(self):
        import datetime
        print "\tMember's Id " + " " * (30 - len("Member's Id ")), self.MId
        print "\tBook's Issue Date" + " " * (30 - len("Book's Issue Date")), self.BIDate
        if str(self.BRDate) == "1111-11-11":
            print "\tBook Returning Date" + " " * (30 - len("Book Returning Date")), self.BIDate + datetime.timedelta(
                days=7)
        else:
            print "\tBook's Return Date " + " " * (30 - len("Book's Return Date ")), self.BRDate

    def rbook(self, members):
        self.BRDate = BIssue.tdate()
        print "Returning Date:", BIssue.tdate()
        Msearch(members, self.MId).edit("missued")
        tday = (self.BRDate - self.BIDate).days
        if tday > 7:
            print "Member have to pay Late Due"
            self.BDue = (tday - 7) * 5
            print "Member Late Fees is ", self.BDue
            Msearch(members, self.MId).edit("due_add", self.BDue)
            print "Book Returned"
        else:
            print "Book Returned"

    def issue_check(self):
        if str(self.BRDate) == "1111-11-11":
            return True
        else:
            return False

    @staticmethod
    def tdate():
        import datetime
        while True:
            try:
                return datetime.date.today()
            except:
                print


class Member:
    def __init__(self, mid, mnm, mad, mcn, md, misd):
        self.MId = mid
        self.MName = mnm
        self.MAddress = mad
        self.MCno = mcn
        self.MDue = md
        self.MIssued = misd

    def display(self):
        print "Member's Id" + " " * (40 - len("Member's Id")), self.MId
        print "Member's Name" + " " * (40 - len("Member's Name")), self.MName
        print "Member's Address" + " " * (40 - len("Member's Address")), self.MAddress
        print "Member's Contact No." + " " * (40 - len("Member's Contact No.")), self.MCno
        print "Member's Due" + " " * (40 - len("Member's Due")), self.MDue

    def modify(self):
        import os
        while True:
            os.system('cls')
            print "\t\t\t\t\t Library Management"
            print "\t\t\t\t\t Member Menu"
            print "\t\t\t\t\t Modify Menu"
            print "1 Member's Name"
            print "2 Member's Address"
            print "3 Member's Contact No."
            print "4 Go Back"
            ch = intcheck("Choice", "Integers", True, range(1, 5))
            if ch == 1:
                self.MName = stgcheck("New Member's Name", "Alphabets (No Symbols)")
            elif ch == 2:
                self.MAddress = stgcheck("New Member's Address", "Alphabets", False)
            elif ch == 3:
                while True:
                    self.MCno = raw_input("Member Contact No." + " "*(40-len("Member Contact No.")))
                    try:
                        int(self.MCno)
                        if len(self.MCno) != 10:
                            raise ZeroDivisionError
                        break
                    except:
                        print "Wrong Input Please Try Again"

            elif ch == 4:
                print "Going Back"
                raw_input("Enter To Continue")
                break

    def Pay_Due(self):
        if self.MDue == 0:
            print "Member has No Due "
            raw_input("Enter To Continue")
        else:
            print "Member's Due is ",self.MDue
            amount = intcheck("Amount", "Integers", True, range(0, (self.MDue + 1)))
            self.MDue = self.MDue - amount
            print "Amount Paid"
            print "Member's Due ", self.MDue
            raw_input("Enter To Continue")

    def edit(self, vr, vr1=0):
        if vr == "missued":
            self.MIssued = (not self.MIssued)
        elif vr == "due_add":
            self.MDue += vr1

    def gstr(self):
        stg = ""
        stg += str(self.MId) + "@" + self.MName + "@" + self.MAddress + "@" + str(self.MCno) + "@" + str(
            self.MDue) + "@"
        if self.MIssued is True:
            stg += "1" + "@"
        else:
            stg += "0" + "@"
        return stg


# Menu
def member_menu(books, members, ky, ky1):
    import os
    while True:
        writemembers(members, ky1)
        os.system("cls")
        os.system("color 1F")
        print "\t\t\t\t\t Library Management"
        print "\t\t\t\t\t Member Menu"
        print "1 Add  Members"
        print "2 Display Members"
        print "3 Modify Members"
        print "4 Delete Members"
        print "5 Go Back"
        print "6 Exit"
        choice = intcheck("Choice ", " Integers ", True, range(1, 7))
        # Change Member Append Encrypt

        if choice == 1:
            while True:
                os.system("cls")
                print "\t\t\t\t\t Library Management"
                print "\t\t\t\t\t Member Menu"
                print "\t\t\t\t\t Add Menu"
                os.system("color 2F")
                obj = UInput1(members)
                members.append(obj)
                if not Confirm_Check("Add Another Member"):
                    raw_input("Going Back Enter to continue")
                    break
                print
            writemembers(members, ky1)

        elif choice == 2:

            os.system("color 3F")
            os.system("cls")
            print "\t\t\t\t\t Library Management"
            print "\t\t\t\t\t Member Menu"
            print "\t\t\t\t\t Display Menu"
            if not members:
                raw_input("No Members Present Enter to Go Back")
                continue
            print "1 Display A Member"
            print "2 Display All Members "
            print "3 Go Back "
            ch_dis = intcheck("Choice ", "Integers ", True, range(1, 4))
            if ch_dis == 1:
                while True:
                    os.system("cls")
                    print "\t\t\t\t\t Library Management"
                    print "\t\t\t\t\t Member Menu"
                    print "\t\t\t\t\t Display Menu"
                    user_dis(members, "Member")
                    dis_srhd = False
                    dis_srh = intcheck("Member No. ", "Integers ")
                    for i in members:
                        if i.MId == dis_srh:
                            i.display()
                            raw_input("Enter To Continue")
                            dis_srhd = True
                            break
                    if dis_srhd:
                        break
                    else:
                        "Member Not Found Try Again"
            elif ch_dis == 2:
                os.system("cls")
                print "\t\t\t\t\t Library Management"
                print "\t\t\t\t\t Member Menu"
                print "\t\t\t\t\t Display Menu"
                print "All Members "
                cdis = 1
                for i in members:
                    print "Member ", cdis
                    i.display()
                    print
                    print
                    cdis += 1
                raw_input("Enter To go to Main Menu")
            elif ch_dis == 3:
                os.system("cls")
                print "\t\t\t\t\t Library Management"
                print "\t\t\t\t\t Member Menu"
                print "\t\t\t\t\t Display Menu"
                raw_input("Going Back Enter To Continue")

        elif choice == 3:
            os.system("color 4F")
            os.system("cls")
            print "\t\t\t\t\t Library Management"
            print "\t\t\t\t\t Member Menu"
            print "\t\t\t\t\t Modify Menu"
            if not members:
                raw_input("No Members Present Enter to Go Back")
                continue
            print "1 Modify  Member"
            print "2 Return Back "
            ch_mod = intcheck("Choice ", "Integers ", True, range(1, 3))
            if ch_mod == 1:
                while True:
                    os.system("cls")
                    user_dis(members, "Member")
                    mod_srhd = False
                    mod_srh = intcheck("Member No. ", "Integers ")
                    for i in members:
                        if i.MId == mod_srh:
                            i.modify()
                            raw_input("Enter To Continue")
                            mod_srhd = True
                            break
                    if mod_srhd:
                        writemembers(members, ky1)
                        break
                    else:
                        "Member Not Found Try Again"
            elif ch_mod == 2:
                os.system("cls")
                print "\t\t\t\t\t Library Management"
                print "\t\t\t\t\t Member Menu"
                print "\t\t\t\t\t Modify Menu"
                raw_input("Going Back Enter To Continue")

        elif choice == 4:
            os.system("cls")
            print "\t\t\t\t\t Library Management"
            print "\t\t\t\t\t Member Menu"
            print "\t\t\t\t\t Delete Menu"
            os.system("color 5F")
            if not members:
                raw_input("No Members Present Enter to Go Back")
                continue
            print "1 Delete A Member"
            print "2 Delete All Members"
            print "3 Return Back"
            ch_del = intcheck("Choice ", "Integers ", True, range(1, 4))
            if ch_del == 1:
                while True:
                    os.system("cls")
                    print "\t\t\t\t\t Library Management"
                    print "\t\t\t\t\t Member Menu"
                    print "\t\t\t\t\t Delete Menu"
                    user_dis(members, "Member")
                    del_srhd = False
                    Del_srh = intcheck("Member No. ", "Integers ")
                    Cdel = 0
                    for i in members:
                        if i.MId == Del_srh:
                            if i.MDue !=0:
                                print "Member Has not Payed The Due"
                                print "Deletion Deletes Member As well As his Issue Data"
                            if Confirm_Check("Delete Member "):
                                DeleteMID(books, ky, i.MId)
                                members.pop(Cdel)
                                raw_input("Member Deleted")
                            else:
                                raw_input("Member Not Deleted")
                            del_srhd = True
                            break
                        Cdel += 1
                    if del_srhd:
                        writemembers(members, ky1)
                        break
                    else:
                        "Member Not Found Try Again"
            elif ch_del == 2:
                os.system("cls")
                print "\t\t\t\t\t Library Management"
                print "\t\t\t\t\t Member Menu"
                print "\t\t\t\t\t Delete Menu"
                print "Unpaid Dues and all Issue list will also be Deleted"
                print "Unpaid Dues"
                print "Member No.\tMember Name"
                for i in members:
                    if i.MDue != 0:
                        print i.MId, i.MName
                if Confirm_Check("Delete All members"):
                    for j in range(len(members)):
                        members.pop()
                    for k in books:
                        k.BIsueList = []
                    writemembers(members, ky1)
                    writebook(books,ky)
                    print "Deleted All members And There Issue Data"
                else:
                    print "Going Back"
                raw_input("Enter To Continue")
            elif ch_del == 3:
                os.system("cls")
                print "\t\t\t\t\t Library Management"
                print "\t\t\t\t\t Member Menu"
                print "\t\t\t\t\t Delete Menu"
                raw_input("Going Back Enter To Continue")

        elif choice == 5:
            os.system("cls")
            print "\t\t\t\t\t Library Management"
            print "\t\t\t\t\t Member Menu"
            raw_input("Enter To Continue")
            break

        elif choice == 6:
            os.system("cls")
            print "\t\t\t\t\t Library Management"
            print "\t\t\t\t\t Member Menu"
            raw_input("Enter Go Back")
            exit()

        else:
            print "Wrong Input Try Again"
        print
        print


def book_menu(books, ky):
    import os
    while True:
        writebook(books, ky)
        os.system("cls")
        os.system("color 1F")
        print "\t\t\t\t\t Library Management"
        print "\t\t\t\t\t Book Menu"
        print "1 Add  Books"
        print "2 Display Books"
        print "3 Modify Books"
        print "4 Delete Books"
        print "5 Go Back Menu"
        print "6 Exit "
        choice = intcheck("Choice ", " Integers ", True, range(1, 7))
        # Change Book Append Encrypt

        if choice == 1:
            while True:
                os.system("cls")
                os.system("color 2F")
                print "\t\t\t\t\t Library Management"
                print "\t\t\t\t\t Book Menu"
                print "\t\t\t\t\t Add Menu"
                obj = UInput(books)
                books.append(obj)
                if not Confirm_Check("Add Another Book"):
                    raw_input("Going Back Enter to continue")
                    break
                print
            writebook(books, ky)

        elif choice == 2:
            os.system("color 3F")
            os.system("cls")
            print "\t\t\t\t\t Library Management"
            print "\t\t\t\t\t Book Menu"
            print "\t\t\t\t\t Display Menu"
            if not books:
                raw_input("No Books Present Enter to Go Back")
                continue
            print "1 Display A Book "
            print "2 Display All Book "
            print "3 Return Back to Menu "
            ch_dis = intcheck("Choice ", "Integers ", True, range(1, 4))
            if ch_dis == 1:
                while True:
                    os.system("cls")
                    print "\t\t\t\t\t Library Management"
                    print "\t\t\t\t\t Book Menu"
                    print "\t\t\t\t\t Display Menu"
                    user_dis(books, "Book")
                    dis_srhd = False
                    dis_srh = intcheck("Book No. ", "Integers ")
                    for i in books:
                        if i.BNo == dis_srh:
                            i.display()
                            raw_input("Enter To Continue")
                            dis_srhd = True
                            break
                    if dis_srhd:
                        break
                    else:
                        "Book Not Found Try Again"
            elif ch_dis == 2:
                os.system("cls")
                print "\t\t\t\t\t Library Management"
                print "\t\t\t\t\t Book Menu"
                print "\t\t\t\t\t Display Menu"
                print "All Books "
                cdis = 1
                for i in books:
                    print "Book ", cdis
                    i.display()
                    print
                    print
                    cdis += 1
                raw_input("Enter To go to Main Menu")
            elif ch_dis == 3:
                os.system("cls")
                print "\t\t\t\t\t Library Management"
                print "\t\t\t\t\t Book Menu"
                print "\t\t\t\t\t Display Menu"
                raw_input("Going Back Enter To Continue")

        elif choice == 3:
            os.system("color 4F")
            os.system("cls")
            print "\t\t\t\t\t Library Management"
            print "\t\t\t\t\t Book Menu"
            print "\t\t\t\t\t Modify Menu"
            if not books:
                raw_input("No Books Present Enter to Go Back")
                continue
            print "1 Modify A Book "
            print "2 Return Back to Menu "
            ch_mod = intcheck("Choice ", "Integers ", True, range(1, 3))
            if ch_mod == 1:
                while True:
                    os.system("cls")
                    print "\t\t\t\t\t Library Management"
                    print "\t\t\t\t\t Book Menu"
                    print "\t\t\t\t\t Modify Menu"
                    user_dis(books, "Book")
                    mod_srhd = False
                    mod_srh = intcheck("Book No. ", "Integers ")
                    for i in books:
                        if i.BNo == mod_srh:
                            i.modify()
                            raw_input("Enter To Continue")
                            mod_srhd = True
                            break
                    if mod_srhd:
                        writebook(books, ky)
                        break
                    else:
                        "Book Not Found Try Again"
            elif ch_mod == 2:
                os.system("cls")
                print "\t\t\t\t\t Library Management"
                print "\t\t\t\t\t Book Menu"
                print "\t\t\t\t\t Modify Menu"
                raw_input("Going Back Enter To Continue")

        elif choice == 4:
            os.system("cls")
            os.system("color 5F")
            print "\t\t\t\t\t Library Management"
            print "\t\t\t\t\t Book Menu"
            print "\t\t\t\t\t Delete Menu"
            if not books:
                raw_input("No books Present Enter to Go Back")
                continue
            print "1 Delete A Book "
            print "2 Delete All Books "
            print "3 Return Back "
            ch_del = intcheck("Choice ", "Integers ", True, range(1, 4))
            if ch_del == 1:
                while True:
                    os.system("cls")
                    print "\t\t\t\t\t Library Management"
                    print "\t\t\t\t\t Book Menu"
                    print "\t\t\t\t\t Delete Menu"
                    user_dis(books, "Book")
                    del_srhd = False
                    Del_srh = intcheck("Book No. ", "Integers ")
                    Cdel = 0
                    for i in books:
                        if i.BNo == Del_srh:
                            if Confirm_Check("Delete Book "):
                                books.pop(Cdel)
                                writebook(books, ky)
                                raw_input("Book Deleted")
                            else:
                                raw_input("Book Not Deleted")
                            del_srhd = True
                            break
                        Cdel += 1
                    if del_srhd:
                        break
                    else:
                        "Book Not Found Try Again"
            elif ch_del == 2:
                os.system("cls")
                print "\t\t\t\t\t Library Management"
                print "\t\t\t\t\t Book Menu"
                print "\t\t\t\t\t Delete Menu"
                if Confirm_Check("Delete All Books"):
                    for i in range(len(books)):
                        books.pop()
                    writebook(books, ky)
                    print "Deleted All Books"
                else:
                    print "Going Back"
                raw_input("Enter To Continue")
            elif ch_del == 3:
                os.system("cls")
                print "\t\t\t\t\t Library Management"
                print "\t\t\t\t\t Book Menu"
                print "\t\t\t\t\t Delete Menu"
                raw_input("Going Back Enter To Continue")

        elif choice == 5:
            raw_input("Enter To Continue")
            break

        elif choice == 6:
            os.system("cls")
            print "\t\t\t\t\t Library Management"
            print "\t\t\t\t\t Book Menu"
            raw_input("Enter To Exit")
            exit()

        else:
            print "Wrong Input Try Again"
        print
        print


def book_issue_menu(books, members, ky, ky1):
    import os
    while True:
        writebook(books, ky)
        writemembers(members, ky1)
        os.system("cls")
        os.system("color F0")
        print "\t\t\t\t\t Library Management"
        print "\t\t\t\t\t Book Issue Menu"
        print "1 Issue A Book "
        print "2 Return A Book  "
        print "3 Display Books Issue Details "
        print "4 Paying Due "
        print "5 Go Back To Menu "
        print "6 Close "
        ichoice = intcheck("Choice ", " Integers ", True, range(1, 7))

        if ichoice == 1:
            while True:
                os.system("cls")
                os.system("color F1")
                print "\t\t\t\t\t Library Management"
                print "\t\t\t\t\t Book Issue Menu"
                print "\t\t\t\t\t Issue Menu"
                CISSUE = user_idis(books, False)
                if not CISSUE:
                    raw_input("All Books Are Issued")
                    break
                i_srhd = False
                i_srh = intcheck("Book No. ", "Integers ")
                for i in books:
                    if i.BNo == i_srh:
                        if Confirm_Check("Issue Book"):
                            user_mdis(members)
                            i.bissue(members)
                        else:
                            print "Book is not Issued"
                        raw_input("Enter To Continue")
                        i_srhd = True
                        break
                if i_srhd:
                    break
                else:
                    "Book Not Found Try Again"

        elif ichoice == 2:
            while True:
                os.system("cls")
                print "\t\t\t\t\t Library Management"
                print "\t\t\t\t\t Book Issue Menu"
                print "\t\t\t\t\t Return Menu"
                os.system("color F2")
                CRETURN = user_idis(books, True)
                if not CRETURN:
                    raw_input("No Books Are Issued")
                    break
                r_srhd = False
                r_srh = intcheck("Book No. ", "Integers ")
                for i in books:
                    if i.BNo == r_srh:
                        if Confirm_Check("Return Book"):
                            i.breturn(members)
                        else:
                            print "Book is not Returned"
                        raw_input("Enter To Continue")
                        r_srhd = True
                        break
                if r_srhd:
                    break
                else:
                    "Book Not Found Try Again"

        elif ichoice == 3:
            os.system("color F3")
            os.system("cls")
            print "\t\t\t\t\t Library Management"
            print "\t\t\t\t\t Book Issue Menu"
            print "\t\t\t\t\t Display Menu"
            print "1 Display Records of Issues Of A Book "
            print "2 Display All Books Issued "
            print "3 Display All Books Returned "
            print "4 Display All Books Issue Details "
            print "5 Go Back To Issue Menu "
            idis_choice = intcheck("Choice", "Integer", True, range(1, 6))
            if idis_choice == 1:
                while True:
                    os.system("cls")
                    print "\t\t\t\t\t Library Management"
                    print "\t\t\t\t\t Book Issue Menu"
                    print "\t\t\t\t\t Display Menu"
                    user_dis(books, "Books")
                    idis_srhd = False
                    idis_srh = intcheck("Book No. ", "Integers ")
                    for i in books:
                        if i.BNo == idis_srh:
                            idis_srhd = True
                            print "Book No " + " " * (40 - len("Book No ")) + str(i.BNo)
                            print "Book Name" + " " * (40 - len("Book Name")) + str(i.BName)
                            if not i.BIsueList:
                                print "Book is Not Yet Issued"
                                raw_input("Enter To Continue")
                                break
                            else:
                                for j in i.BIsueList:
                                    j.idisplay()
                                    raw_input("Enter To Continue")
                                    break
                    if idis_srhd:
                        break
                    else:
                        "Book Not Found Try Again"
            elif idis_choice == 2:
                os.system("cls")
                print "\t\t\t\t\t Library Management"
                print "\t\t\t\t\t Book Issue Menu"
                print "\t\t\t\t\t Display Menu"
                cidis = 1
                for i in books:
                    if len(i.BIsueList) != 0:
                        if i.BIsueList[len(i.BIsueList) - 1].issue_check():
                            print "Book " + " " * (20 - len("Book ")), cidis
                            print "Book No " + " " * (20 - len("Book No ")), i.BNo
                            print "Book Name" + " " * (20 - len("Book Name")), i.BName
                            i.BIsueList[len(i.BIsueList) - 1].idisplay()
                            print
                            cidis += 1
                else:
                    if cidis == 1:
                        print "No Books Are Issued"
                raw_input("Enter To go to Main Menu")
            elif idis_choice == 3:
                os.system("cls")
                print "\t\t\t\t\t Library Management"
                print "\t\t\t\t\t Book Issue Menu"
                print "\t\t\t\t\t Display Menu"
                crdis = 1
                for i in books:
                    if len(i.BIsueList) != 0:
                        if not i.BIsueList[len(i.BIsueList) - 1].issue_check():
                            print "Book " + " " * (20 - len("Book ")), crdis
                            print "Book No " + " " * (20 - len("Book No ")), i.BNo
                            print "Book Name" + " " * (20 - len("Book Name")), i.BName
                            i.BIsueList[len(i.BIsueList) - 1].idisplay()
                            crdis += 1
                            print
                if crdis == 1:
                    print "All Books Are Issued"
                raw_input("Enter To go to Main Menu")
            elif idis_choice == 4:
                cnt_dis_all = 1
                os.system("cls")
                print "\t\t\t\t\t Library Management"
                print "\t\t\t\t\t Book Issue Menu"
                print "\t\t\t\t\t Display Menu"
                for i in books:
                    print "Book " + " " * (20 - len("Book ")), cnt_dis_all
                    print "Book No " + " " * (20 - len("Book No ")),  i.BNo
                    print "Book Name" + " " * (20 - len("Book Name")), i.BName
                    for j in i.BIsueList:
                        j.idisplay()
                        print
                    cnt_dis_all += 1
                    print
                raw_input("Enter To go to Main Menu")
            elif idis_choice == 5:
                os.system("cls")
                print "\t\t\t\t\t Library Management"
                print "\t\t\t\t\t Book Issue Menu"
                print "\t\t\t\t\t Display Menu"
                raw_input("Enter To Go Back To Issue Menu")

        elif ichoice == 4:
            os.system("cls")
            print "\t\t\t\t\t Library Management"
            print "\t\t\t\t\t Book Issue Menu"
            print "\t\t\t\t\t Due Menu"
            os.system("color F4")
            CMDue=0
            print "Member No.\tMember Name"
            for i in members:
                if i.MDue != 0:
                    print i.MId, i.MName
                    CMDue+=1
            if CMDue == 0:                    
                raw_input("No Dues Go Back")
                continue
            sid_pay = intcheck("Member's Id", "Integers")
            Msearch(members, sid_pay).Pay_Due()

        elif ichoice == 5:
            os.system("cls")
            print "\t\t\t\t\t Library Management"
            print "\t\t\t\t\t Book Issue Menu"
            raw_input("Enter To Go Back")
            break

        elif ichoice == 6:
            os.system("cls")
            print "\t\t\t\t\t Library Management"
            print "\t\t\t\t\t Book Issue Menu"
            raw_input("Enter To Exit")
            exit()
