import csv
import mysql.connector as sql
mycon = sql.connect(host='localhost', user='root', passwd='', database='bank')
cursor = mycon.cursor()


def pr(listinp):
    global logdoc
    with open(logdoc, 'a', newline='') as csvfile:
        csvw = csv.writer(csvfile, delimiter=',')
        csvw.writerows(listinp)
    csvfile.close()


def datime():
    global logdoc
    from datetime import datetime
    now = datetime.now()
    x = now.strftime("%m/%d/%Y %H:%M:%S")
    listdt = [[x]]
    date_time = [['date and time']]
    with open(logdoc, 'a', newline='') as csvfile:
        csvw = csv.writer(csvfile, delimiter=',')
        csvw.writerows(date_time)
        csvw.writerows(listdt)
    csvfile.close()


def create():
    print("**Creating Your Bank Account**")
    print()
    sel = "Select max(AccountNO) from customer"
    cursor.execute(sel)
    ac = cursor.fetchall()
    accno = int(ac[0][0])+1
    accname = input('Enter your Name:')
    print()
    phno = int(input('Enter your Phone Number:'))
    if len(str(phno)) == 10:
        print()
    else:
        while True:
            print("Phone No should have 10 digits")
            print()
            phno = int(input('Enter your Phone Number:'))
            print()
            if len(str(phno)) == 10:
                break
    mailid = input("Enter your EmailID:")
    print()
    addrs = input("Enter your Address:")
    print()
    adhno = input("Enter Aadhar Number:")
    if len(adhno) == 12:
        print()
    else:
        print()
        print("Aadhaar NO should be 12 digits")
        adhno = input("Enter Aadhar Number:")
    Insert = "Insert into customer values ('%s','%s','%s','%s','%s','%s')" % (
        accno, accname, phno, mailid, addrs, adhno)
    cursor.execute(Insert)
    mycon.commit()
    from datetime import datetime
    now = datetime.now()
    y = now.strftime("%m/%d/%Y ")
    print()
    print("Your account No :", accno)
    print()
    prints = '**Account Created Succesfully**'
    print(prints)
    print()
    listinp = [[prints]]
    pr(listinp)
    datime()
    Insert1 = "Insert into transaction values ('%s','%s','%s',%s,%s,%s)" % (
        accno, accname, y, 0, 0, 0)
    cursor.execute(Insert1)
    mycon.commit()


def trans():
    accno = input('Enter Your Account Number=')
    print()
    sel = "select * from customer where AccountNo=%s " % (accno)
    cursor.execute(sel)
    data = cursor.fetchall()
    count = cursor.rowcount
    mycon.commit()
    print()
    if count == 0:
        print('**!!Invalid Account Number!!**')
        print()
        print("**Try Again**")
        print()
        trans()
    else:
        print('1.Withdraw Amount')
        print()
        print('2.Deposit Amount')
        print()
        x = int(input('Enter your choice:'))
        print()
        if x == 1:
            wamt = int(input('Enter withdrawl amount='))
            sel = "select currentbalance from transaction where AccountNo=%s" % (
                accno)
            cursor.execute(sel)
            x = cursor.fetchone()
            if x[0] >= wamt:
                print()
            else:
                print("Out of balance")
                while True:
                    print()
                    wamt = int(input('Enter withdrawl amount='))
                    print()
                    if x[0] >= wamt:
                        break
            cramt = x[0]-wamt
            change = "update transaction set currentbalance=%s,withdrawalAmount=%s where AccountNo=%s" % (
                cramt, wamt, accno)
            cursor.execute(change)
            mycon.commit()
            print()
            prints1 = '**', wamt, "withdrawn Succesfully**"
            print('**', wamt, "withdrawn Succesfully**")
            listinp = [[prints1]]
            datime()
            pr(listinp)
            print()
            prints2 = "**Account Updated Succesfully**"
            listinp = [[prints2]]
            datime()
            pr(listinp)
            print("**Account Updated Succesfully**")
            print()

        if x == 2:
            damt = int(input('Enter amount to be deposited:'))
            sel = "select currentbalance from transaction where AccountNo=%s" % (
                accno)
            cursor.execute(sel)
            x = cursor.fetchone()
            cramt = x[0]+damt
            change = 'update transaction set currentbalance=%s,depositedAmount=%s where AccountNo=%s' % (
                cramt, damt, accno)
            cursor.execute(change)
            mycon.commit()
            print()
            prints = '**Account Updated Succesfully**'
            listinp = [[prints]]
            datime()
            pr(listinp)
            print(prints)


def password():
    accno = input('Enter Your Account Number:')
    print()
    passwd = input('Enter Old Password:')
    Sel = "select * from user where password='%s' and username= '%s'; " % (
        passwd, name)
    cursor.execute(Sel)
    if cursor.fetchone() is None:
        print('!!Incorrect username/Password!!')
    else:
        print()
        passwd = input("Enter new password:")
        change = "update user set Password='%s' where username='%s'" % (
            passwd, name)
        cursor.execute(change)
        mycon.commit()
        prints = "!!**Password Updated successfully**!!"
        listinp = [[prints]]
        datime()
        pr(listinp)
        print("!!**Password Updated successfully**!!")


def transdetails():
    with open(logdoc, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for i in csvreader:
            print(i[0])
            print()


def Delete():
    username = input("Enter your Username:")
    print()
    psswd = input("Enter password")
    print()
    accno = int(input("Enter Your Account No:"))
    Sel = "select * from user where password='%s' and username= '%s' " % (
        psswd, username)
    cursor.execute(Sel)
    if cursor.fetchone() is None:
        print()
        print('!!Invalid User name or Password!!')
    else:
        while True:
            x = input("Do you want to delete your account?(Y/N):")
            if x == "Y" or 'y':
                Delcust = "Delete from customer where AccountNo=%s" % (accno)
                deluser = "Delete from user where Username='%s'" % (username)
                prints = 'Account deleted successfully!!'
                cursor.execute(Delcust)
                cursor.execute(deluser)
                mycon.commit()
                listinp = [[prints]]
                datime()
                pr(listinp)
                print('Account deleted successfully!!')
                break
            elif x == "N" or "n":
                print()
                menu()
            else:
                print("Invalid code")
                print()
                print("Try again")


def menu():
    c = "y"
    while c == "y" or "Y":
        print()
        print('1.Transaction')
        print()
        print('2.Change password')
        print()
        print('3.View History/Activities/Transactions')
        print()
        print('4.Delete account')
        print()
        print('5.Exit')
        print()
        x = int(input('Enter your choice:'))
        print()
        if x == 1:
            trans()
        elif x == 2:
            password()
        elif x == 3:
            transdetails()
        elif x == 4:
            Delete()
        elif x == 5:
            datime()
            prints = "**Thankyou ,Please Visit Again **"
            listinp = [[prints]]
            pr(listinp)
            print(prints)
            break
        else:
            print("***!!Invalid choice!!***")
            print()
            print("***Please try again***")


print("                             Welcome to Citizens Bank Of India     ")
print()
while True:
    print('1.Register')
    print()
    print('2.Login')
    print()
    n = int(input('Enter your choice(1/2):'))
    print()

    if n == 1:
        try:
            name = input('Enter Username:')
            print()
            passwd = input('Enter Password:')
            print()
            Data = ("INSERT  INTO user values ('%s','%s')") % (name, passwd)
            cursor.execute(Data)
            mycon.commit()
        except:
            print()
            print("!!Error encountered!!")
            print()
            print(
                "Use another username and password.Another user has already taken same username/password")
            print()
            print("Try again")
            print()
            continue
        print()
        prints = '**User created successfully**'
        print(prints)
        print()
        logdoc = name+".csv"
        listinp = [[prints]]
        pr(listinp)
        datime()
        create()
        menu()
        break

    elif n == 2:
        name = input('Enter Username:')
        print()
        passwd = input('Enter Password:')
        print()
        logdoc = name+".csv"
        Sel = "select * from user where password='%s' and username= '%s'; " % (
            passwd, name)
        cursor.execute(Sel)
        if cursor.fetchone() is None:
            print('!!User Does not exist!!')
        else:
            prints = "**Login successful**"
            print(prints)
            listinp = [[prints]]
            pr(listinp)
            logdoc = name+".csv"
            datime()
            menu()
            break
    else:
        print("** !! Invalid code entered !! **")
        print()
        print("  !!Try Again!!  ")
        print()
        continue
