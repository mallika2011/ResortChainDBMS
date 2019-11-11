import subprocess as sp
import pymysql
import pymysql.cursors


def addEmployee():
    global cur
    # print('lolol')
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
    row["First_Name"] = input("First Name: ")
    row["Last_Name"] = input("Last Name: ")
    row["Date_of_Reg"] = input("Date_of_Reg (YYYY-MM-DD): ")
    row["DOB"] = input("DOB (YYYY-MM-DD): ")
    row["Email_ID"] = input("Email ID: ")

    row["Package"] = "Red"  # By default we are giving red
    row['Monthly_Fee'] = 500
    row_add = []
    n = int(input("Enter the number of member's addresses you want to input: "))
    for i in range(n):
        row_add.append(input("Address: "))

    row_phone = []
    m = int(input("Enter the number of member's phone number you want to input: "))
    for i in range(m):
        row_phone.append(input("Phone Number : "))

    query = "INSERT INTO MEMBERS(Member_ID, First_Name, Last_Name, Date_of_Reg, DOB, Email_ID, Monthly_Fee) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%d')" % (
        row["Member_ID"], row["First_Name"], row["Last_Name"], row["Date_of_Reg"], row["DOB"], row["Email_ID"], row["Monthly_Fee"])
    cur.execute(query)
    con.commit()

    query = "INSERT INTO MEMBER_PACKAGE(Member_ID, Package) VALUES('%s', '%s')" % (
        row["Member_ID"], row["Package"])

    for i in range(n):
        query = "INSERT INTO MEMBER_ADDRESS(Member_ID, Address) VALUES('%s', '%s')" % (
            row["Member_ID"], row_add[i])
        cur.execute(query)
        con.commit()

    for i in range(m):
        query = "INSERT INTO MEMBER_PHONE(Member_ID, Ph_No) VALUES('%s', '%s')" % (
            row["Member_ID"], row_phone[i])
        cur.execute(query)
        con.commit()
    return


def addMemberGuest():
    global cur
    row = {}
    print("Enter the member guest details: ")

    row["Hotel_ID"] = input("Hotel_ID: ")
    row["Room_Number"] = input("Room_Number: ")
    row["Member_ID"] = input("Member_ID: ")
    row["Check-In_Date"] = input("Check-In_Date(YYYY-MM-DD): ")
    row["Check-Out_Date"] = input("Check-Out_Date(YYYY-MM-DD): ")

    # Not doing anything for cost of staying

    query = "SELECT isOccupied FROM HOTEL_I WHERE HOTEL_ID=%s AND ROOM_NUMBER=%s" % (
        row["Hotel_ID"], row["Room_Number"])
    cur.execute(query)
    x = cur.fetchone()
    con.commit()

    if x["isOccupied"] == 0:
        query = "INSERT INTO MEMBER_GUESTS(Hotel_ID, Room_No, Member_ID, Check_In_Date, Check_Out_Date,Cost_Of_Staying) VALUES('%s', '%s', '%s', '%s', '%s',0 )" % (
            row["Hotel_ID"], row["Room_Number"], row["Member_ID"], row["Check-In_Date"], row["Check-Out_Date"])
        cur.execute(query)
        con.commit()

        query = "UPDATE MEMBER_GUESTS M SET COST_OF_STAYING = (CHECK_OUT_DATE-CHECK_IN_DATE)*(SELECT PRICE_DAY FROM HOTEL_I WHERE HOTEL_ID = M.HOTEL_ID AND M.ROOM_NO=ROOM_NUMBER)"
        cur.execute(query)
        con.commit()

        query = "UPDATE HOTEL_I SET ISOCCUPIED=1,ISMEMBER=1 WHERE HOTEL_ID=%s AND ROOM_NUMBER=%s" % (
            row["Hotel_ID"], row["Room_Number"])
        cur.execute(query)
        con.commit()
    else:
        print("Room already occupied")

    return


def addNonMemberGuest():
    global cur
    row = {}
    print("Enter the non-member guest details: ")
    row["Hotel_ID"] = input("Hotel_ID: ")
    row["Room_Number"] = input("Room_Number: ")
    row["First_Name"] = input("First Name: ")
    row["Last_Name"] = input("Last Name: ")
    row["Check-In_Date"] = input("Check-In_Date(YYYY-MM-DD): ")
    row["Check-Out_Date"] = input("Check-Out_Date(YYYY-MM-DD): ")
    row["Phone_Number"] = input("Phone Number: ")

    query = "SELECT isOccupied FROM HOTEL_I WHERE HOTEL_ID=%s AND ROOM_NUMBER=%s" % (
        row["Hotel_ID"], row["Room_Number"])
    cur.execute(query)
    x = cur.fetchone()
    # print(x)
    con.commit()

    if x["isOccupied"] == 0:
        query = "INSERT INTO NON_MEMBER_GUESTS(Hotel_ID, Room_No, First_Name, Last_Name, Check_In_Date, Check_Out_Date, Phone_Number,Cost_Of_Staying) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s',0)" % (
            row["Hotel_ID"], row["Room_Number"], row["First_Name"], row["Last_Name"], row["Check-In_Date"], row["Check-Out_Date"], row["Phone_Number"])
        cur.execute(query)
        con.commit()

        query = "UPDATE NON_MEMBER_GUESTS M SET COST_OF_STAYING = (CHECK_OUT_DATE-CHECK_IN_DATE)*((SELECT PRICE_DAY FROM HOTEL_I WHERE HOTEL_ID = M.HOTEL_ID AND M.ROOM_NO=ROOM_NUMBER)+1000);"
        cur.execute(query)
        con.commit()

        query = "UPDATE HOTEL_I SET ISOCCUPIED=1,ISMEMBER=0 WHERE HOTEL_ID=%s AND ROOM_NUMBER=%s" % (
            row["Hotel_ID"], row["Room_Number"])
        cur.execute(query)
        con.commit()
    else:
        print("Room already occupied")

    return


def addPackage():
    global cur
    row = {}
    print("Enter the member_id and package you want to add: ")
    row["Member_ID"] = input("Member_ID: ")
    row["Package"] = input("Package: ")
    query = "INSERT INTO MEMBER_PACKAGE(Member_ID, Package) VALUES('%s', '%s')" % (
        row["Member_ID"], row["Package"])
    cur.execute(query)
    con.commit()
    return


def addFinance():
    global cur
    row = {}
    print("Enter Finance Details: ")

    row["Hotel_ID"] = input("Hotel_ID: ")
    row["Month"] = input("Month: ")
    row["Income"] = int(input("Income: "))
    row["Expenditure"] = int(input("Expenditure: "))

    query = "INSERT INTO FINANCE(Hotel_ID, Expenditure, Income, Month, Profit) VALUES('%s', '%d', '%d', '%s',0)" % (
        row["Hotel_ID"], row["Expenditure"], row["Income"], row["Month"])
    cur.execute(query)
    con.commit()

    query = "UPDATE FINANCE F SET PROFIT = (INCOME-EXPENDITURE) WHERE HOTEL_ID ='%s' AND MONTH='%s'" % (
        row["Hotel_ID"], row["Month"])
    cur.execute(query)
    con.commit()

    return


def addServiceProvider():
    global cur
    row = {}
    print("Enter Service Provider Details: ")

    row["Service_Provider"] = input("Service_Provider: ")
    row["Service_Description"] = input("Service_Description: ")
    row["Service_Price"] = int(input("Service_Price: "))

    query = "INSERT INTO PROVIDERS_SERVICES(Service_Provider, Service_Description, Service_Price) VALUES('%s', '%s', '%d')" % (
        row["Service_Provider"], row["Service_Description"], row["Service_Price"])
    cur.execute(query)
    con.commit()
    return


def addRoom():
    global cur
    row = {}
    print("Enter the new room's details: ")

    row["Room_Type"] = input("Room_Type: ")
    row["Price_Day"] = input("Price Per Day: ")
    row["Room_Number"] = input("Room_Number: ")
    row["Hotel_ID"] = input("Hotel ID: ")

    query = "INSERT INTO HOTEL_I(isMember,isOccupied,Room_Type,Price_Day,Room_Number,Hotel_ID) VALUES(NULL,0,'%s', '%s', '%s', '%s')" % (
        row["Room_Type"], row["Price_Day"], row["Room_Number"], row["Hotel_ID"])
    cur.execute(query)
    con.commit()
    return


def addHotel():
    global cur
    row = {}
    print("Enter the new hotel's details: ")
    row["Hotel_ID"] = input("Hotel ID: ")
    row["Hotel_Name"] = input("Hotel_Name: ")
    row["Location"] = input("Location: ")
    row["Manager_ID"] = input("Manager_ID: ")

    query = "INSERT INTO DESTINATION(Hotel_ID,Hotel_Name,Location,Manager_ID) VALUES('%s', '%s', '%s', '%s')" % (
        row["Hotel_ID"], row["Hotel_Name"], row["Location"], row["Manager_ID"])
    cur.execute(query)
    con.commit()

    query = "UPDATE EMPLOYEE SET HOTEL_ID='%s' WHERE EMPLOYEE_ID=%s" % (
        row["Hotel_ID"], row["Manager_ID"])
    cur.execute(query)
    con.commit()

    return


optionFunctionMapping = {
    1: addEmployee,
    2: addMember,
    3: addMemberGuest,
    4: addNonMemberGuest,
    5: addPackage,
    6: addFinance,
    7: addServiceProvider,
    8: addRoom,
    9: addHotel
}

while(1):
    # tmp = sp.call('clear', shell=True)
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
        #     print("2. mem guest")
        #     print("3. Promote an employee")
        #     print("4. Reward a department")
        #     c = int(input("Enter choice> "))
        #     tmp = sp.call('clear', shell=True)
        #     if c==9:
        #         break
        #     else:
        #         send(optionFunctionMapping[c]())
        # addEmployee()
        # addMember()
        # addNonMemberGuest()
        # addServiceProvider()
        # addFinance()
        addRoom()

    # except:
    #     #tmp = sp.call('clear', shell=True)
    #     print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
    #     tmp = input("Enter any key to CONTINUE>")
