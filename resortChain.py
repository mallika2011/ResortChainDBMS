import subprocess as sp
import pymysql
import pymysql.cursors


def addEmployee():
    global cur
    print('lolol')
    row = {}
    print("Enter the new employee's details: ")

    row["Employee_ID"] = input("Employee ID: ")
    row["First_Name"] = input("First Name: ")
    row["Last_Name"] = input("Last Name: ")
    row["Salary"] = int(input("Salary: "))
    row["DOB"] = input("DOB (YYYY-MM-DD): ")
    row["Hotel_ID"] = input("Hotel ID: ")
    row["Email_ID"] = input("Email ID: ")

    row_add = []
    n = int(input("Enter the number of employee's addresses you want to input: "))
    for i in range(n):
        row_add.append(input("Address: "))

    row_phone = []
    m = int(input("Enter the number of employee's phone number you want to input: "))
    for i in range(m):
        row_phone.append(input("Phone Number : "))

    query = "INSERT INTO EMPLOYEE(Employee_ID, First_Name, Last_Name, Salary, DOB, Hotel_ID, Email_ID) VALUES('%s', '%s', '%s', '%d', '%s', '%s', '%s')" % (
        row["Employee_ID"], row["First_Name"], row["Last_Name"], row["Salary"], row["DOB"], row["Hotel_ID"], row["Email_ID"])
    cur.execute(query)
    con.commit()

    for i in range(n):
        query = "INSERT INTO EMPLOYEE_ADDRESS(Employee_ID, Address) VALUES('%s', '%s')" % (
            row["Employee_ID"], row_add[i])
        cur.execute(query)
        con.commit()

    for i in range(m):
        query = "INSERT INTO EMPLOYEE_PHONE(Employee_ID, Ph_No) VALUES('%s', '%s')" % (
            row["Employee_ID"], row_phone[i])
        cur.execute(query)
        con.commit()
    return


def addMember():
    global cur
    row = {}
    print("Enter the new member's details: ")

    row["Member_ID"] = input("Member_ID: ")
    name = (input("Name (First_Name Last_Name): ")).split(' ')
    row["First_Name"] = name[0]
    row["Last_Name"] = name[1]
    row["Date_of_Reg"] = input("Date_of_Reg (DD/MM/YYYY): ")
    row["DOB"] = input("DOB (DD/MM/YYYY): ")
    row["Email_ID"] = input("Email ID: ")

    row["Package"] = "Red"  # By default we are giving red

    row_add = {}
    n = input("Enter the number of member's addresses you want to input: ")
    for i in range(n):
        row_add[i] = input("Address: ")

    row_phone = {}
    m = input("Enter the number of member's phone number you want to input: ")
    for i in range(m):
        row_phone[i] = input("Phone Number : ")

    query = "INSERT INTO MEMBERS(Member_ID, First_Name, Last_Name, Date_of_Reg, DOB, Email_ID, Monthly_Fee) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%d')" % (
        row["Member_ID"], row["First_Name"], row["Last_Name"], row["Date_of_Reg"], row["DOB"], row["Email_ID"], row["Monthly_Fee"])
    cur.execute(query)
    con.commit()

    query = "INSERT INTO MEMBER_PACKAGE(Member_ID, Package) VALUES('%s', '%s')" % (
        row["Member_ID"], row["Package"])
    for i in range(n):
        query = "INSERT INTO MEMBER_ADDRESS(Member_ID, Address) VALUES('%s', '%s')" % (
            row_add["Member_ID"], row_add["Address"])
        cur.execute(query)
        con.commit()

    for i in range(m):
        query = "INSERT INTO MEMBER_PHONE(Member_ID, Phone_number) VALUES('%s', '%s')" % (
            row_phone["Employee_ID"], row_phone["Phone_Number"])
        cur.execute(query)
        con.commit()
    return


def addMemberGuest():
    global cur
    row = {}
    print("Enter the member guest details: ")

    row["Hotel_ID"] = input("Hotel_ID: ")
    row["Room_Number"] = input("Room_Number")
    row["Member_ID"] = input("Member_ID")
    row["Check-In_Date"] = input("Check-In_Date(DD/MM/YYYY): ")
    row["Check-Out_Date"] = input("Check-Out_Date(DD/MM/YYYY): ")

    # Not doing anything for cost of staying
    query = "INSERT INTO MEMBER_GUESTS(Hotel_ID, Room_Number, Member_ID, Check-In_Date, Check-Out_Date) VALUES('%s', '%s', '%s', '%s', '%s')" % (
        row["Hotel_ID"], row["Room_Number"], row["Member_ID"], row["Check-In_Date"], row["Check-Out_Date"])
    cur.execute(query)
    con.commit()
    return


def addNonMemberGuest():
    global cur
    row = {}
    print("Enter the non-member guest details: ")
    row["Hotel_ID"] = input("Hotel_ID: ")
    row["Room_Number"] = input("Room_Number")
    name = (input("Name (First_Name Last_Name): ")).split(' ')
    row["First_Name"] = name[0]
    row["Last_Name"] = name[1]
    row["Check-In_Date"] = input("Check-In_Date(DD/MM/YYYY): ")
    row["Check-Out_Date"] = input("Check-Out_Date(DD/MM/YYYY): ")
    # Left the cost of staying
    row["Phone_Number"] = input("Phone_Number")

    query = "INSERT INTO NON-MEMBER_GUESTS(Hotel_ID, Room_Number, First_Name, Last_Name, Check-In_Date, Check-Out_Date, Phone_Number) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
        row["Hotel_ID"], row["Room_Number"], row["First_Name"], row["Last_Name"], row["Check-In_Date"], row["Check-Out_Date"], row["Phone_Number"])
    cur.execute(query)
    con.commit()
    return
# modify package for a member (basically adding a package)


def addPackage():
    global cur
    row = {}
    print("Enter the member_id and package you want to add: ")
    row["Member_ID"] = input("Member_ID: ")
    row["Package"] = input("Package")
    query = "INSERT INTO MEMBER_PACKAGE(Member_ID, Package) VALUES('%s', '%s')" % (
        row["Member_ID"], row["Package"])
    cur.execute(query)
    con.commit()
    return


optionFunctionMapping = {
    1: addEmployee,
    2: addMember,
    3: addMemberGuest,
    4: addNonMemberGuest
    # 5: addFinance,
    # 6: addServiceProvider,
    # 7: addRoom
}

while(1):
    tmp = sp.call('clear', shell=True)
    # username = input("Username: ")
    # password = input("Password: ")

    # try:
    con = pymysql.connect(host='localhost',
                          user='mallika',
                          password='Aaaa1234%',
                          db='RESORT',
                          cursorclass=pymysql.cursors.DictCursor)
    with con:
        cur = con.cursor()
            # while(1):
            #     tmp = sp.call('clear', shell=True)
            #     print("1. Hire a new employee")
            #     print("2. Fire an employee")
            #     print("3. Promote an employee")
            #     print("4. Reward a department")
            #     c = int(input("Enter choice> "))
            #     tmp = sp.call('clear', shell=True)
            #     if c == 9:
            #         break
            #     else:
            #         send(optionFunctionMapping[c]())
        addEmployee()

    # except:
    #     #tmp = sp.call('clear', shell=True)
    #     print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
    #     tmp = input("Enter any key to CONTINUE>")
