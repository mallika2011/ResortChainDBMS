import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate
# from datetime import datetime
import datetime


def addEmployee():
    global cur
    # print('lolol')
    row = {}
    print("Enter the new employee's details: ")

    row["Employee_ID"] = input("Employee ID: ")
    row["First_Name"] = input("First Name: ")
    row["Last_Name"] = input("Last Name: ")
    
    try:
        row["Salary"] = int(input("Salary: "))
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
    row["DOB"] = input("DOB (YYYY-MM-DD): ")
    row["Hotel_ID"] = input("Hotel ID: ")
    row["Email_ID"] = input("Email ID: ")

    row_add = []
    try:
        n = int(input("Enter the number of employee's addresses you want to input: "))
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
    for i in range(n):
        row_add.append(input("Address: "))

    row_phone = []
    try:
        m = int(input("Enter the number of employee's phone number you want to input: "))
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
    for i in range(m):
        row_phone.append(input("Phone Number : "))

    try:
        query = "INSERT INTO EMPLOYEE(Employee_ID, First_Name, Last_Name, Salary, DOB, Hotel_ID, Email_ID) VALUES('%s', '%s', '%s', '%d', '%s', '%s', '%s')" % (
            row["Employee_ID"], row["First_Name"], row["Last_Name"], row["Salary"], row["DOB"], row["Hotel_ID"], row["Email_ID"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return

    for i in range(n):
        try:
            query = "INSERT INTO EMPLOYEE_ADDRESS(Employee_ID, Address) VALUES('%s', '%s')" % (
                row["Employee_ID"], row_add[i])
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return

    for i in range(m):
        try:
            query = "INSERT INTO EMPLOYEE_PHONE(Employee_ID, Ph_No) VALUES('%s', '%s')" % (
                row["Employee_ID"], row_phone[i])
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return
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
    try:
        n = int(input("Enter the number of member's addresses you want to input: "))
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
    for i in range(n):
        row_add.append(input("Address: "))

    row_phone = []
    try:
        m = int(input("Enter the number of member's phone number you want to input: "))
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
    for i in range(m):
        row_phone.append(input("Phone Number : "))

    try:
        query = "INSERT INTO MEMBERS(Member_ID, First_Name, Last_Name, Date_of_Reg, DOB, Email_ID, Monthly_Fee) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%d')" % (
            row["Member_ID"], row["First_Name"], row["Last_Name"], row["Date_of_Reg"], row["DOB"], row["Email_ID"], row["Monthly_Fee"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return

    try:
        query = "INSERT INTO MEMBER_PACKAGE(Member_ID, Package) VALUES('%s', '%s')" % (
            row["Member_ID"], row["Package"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return

    for i in range(n):
        try:
            query = "INSERT INTO MEMBER_ADDRESS(Member_ID, Address) VALUES('%s', '%s')" % (
                row["Member_ID"], row_add[i])
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return

    for i in range(m):
        try:
            query = "INSERT INTO MEMBER_PHONE(Member_ID, Ph_No) VALUES('%s', '%s')" % (
                row["Member_ID"], row_phone[i])
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return
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

    try:
        query = "SELECT isOccupied FROM HOTEL_I WHERE HOTEL_ID=%s AND ROOM_NUMBER=%s" % (
            row["Hotel_ID"], row["Room_Number"])
        cur.execute(query)
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    x = cur.fetchone()
    con.commit()

    if x["isOccupied"] == 0:
        try:
            query = "INSERT INTO MEMBER_GUESTS(Hotel_ID, Room_No, Member_ID, Check_In_Date, Check_Out_Date,Cost_Of_Staying) VALUES('%s', '%s', '%s', '%s', '%s',0 )" % (
                row["Hotel_ID"], row["Room_Number"], row["Member_ID"], row["Check-In_Date"], row["Check-Out_Date"])
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return
        try:
            query = "UPDATE MEMBER_GUESTS M SET COST_OF_STAYING = (CHECK_OUT_DATE-CHECK_IN_DATE)*(SELECT PRICE_DAY FROM HOTEL_I WHERE HOTEL_ID = M.HOTEL_ID AND M.ROOM_NO=ROOM_NUMBER)"
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return

        try:
            query = "UPDATE HOTEL_I SET ISOCCUPIED=1,ISMEMBER=1 WHERE HOTEL_ID=%s AND ROOM_NUMBER=%s" % (
                row["Hotel_ID"], row["Room_Number"])
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return

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

    try:
        query = "SELECT isOccupied FROM HOTEL_I WHERE HOTEL_ID=%s AND ROOM_NUMBER=%s" % (
            row["Hotel_ID"], row["Room_Number"])
        cur.execute(query)
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    x = cur.fetchone()
    # print(x)
    con.commit()

    if x["isOccupied"] == 0:
        try:
            query = "INSERT INTO NON_MEMBER_GUESTS(Hotel_ID, Room_No, First_Name, Last_Name, Check_In_Date, Check_Out_Date, Phone_Number,Cost_Of_Staying) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s',0)" % (
                row["Hotel_ID"], row["Room_Number"], row["First_Name"], row["Last_Name"], row["Check-In_Date"], row["Check-Out_Date"], row["Phone_Number"])
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return

        try:
            query = "UPDATE NON_MEMBER_GUESTS M SET COST_OF_STAYING = (CHECK_OUT_DATE-CHECK_IN_DATE)*((SELECT PRICE_DAY FROM HOTEL_I WHERE HOTEL_ID = M.HOTEL_ID AND M.ROOM_NO=ROOM_NUMBER)+1000);"
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return

        try:
            query = "UPDATE HOTEL_I SET ISOCCUPIED=1,ISMEMBER=0 WHERE HOTEL_ID=%s AND ROOM_NUMBER=%s" % (
                row["Hotel_ID"], row["Room_Number"])
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return

    else:
        print("Room already occupied")

    return


def addPackage():
    global cur
    row = {}
    print("Enter the member_id and package you want to add: ")
    row["Member_ID"] = input("Member_ID: ")
    row["Package"] = input("Package: ")

    try:
        query = "INSERT INTO MEMBER_PACKAGE(Member_ID, Package) VALUES('%s', '%s')" % (
            row["Member_ID"], row["Package"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    return


def addFinance():
    global cur
    row = {}
    print("Enter Finance Details: ")

    row["Hotel_ID"] = input("Hotel_ID: ")
    row["Month"] = input("Month: ")
    try:
        row["Income"] = int(input("Income: "))
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
    try:    
        row["Expenditure"] = int(input("Expenditure: "))
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")

    try:
        query = "INSERT INTO FINANCE(Hotel_ID, Expenditure, Income, Month, Profit) VALUES('%s', '%d', '%d', '%s',0)" % (
            row["Hotel_ID"], row["Expenditure"], row["Income"], row["Month"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return

    try:
        query = "UPDATE FINANCE F SET PROFIT = (INCOME-EXPENDITURE) WHERE HOTEL_ID ='%s' AND MONTH='%s'" % (
            row["Hotel_ID"], row["Month"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return

    return


def addServiceProvider():
    global cur
    row = {}
    print("Enter Service Provider Details: ")

    row["Service_Provider"] = input("Service_Provider: ")
    row["Service_Description"] = input("Service_Description: ")
    try:
        row["Service_Price"] = int(input("Service_Price: "))
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")

    try:
        query = "INSERT INTO PROVIDERS_SERVICES(Service_Provider, Service_Description, Service_Price) VALUES('%s', '%s', '%d')" % (
            row["Service_Provider"], row["Service_Description"], row["Service_Price"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    return


def addRoom():
    global cur
    row = {}
    print("Enter the new room's details: ")

    row["Room_Type"] = input("Room_Type: ")
    row["Price_Day"] = input("Price Per Day: ")
    row["Room_Number"] = input("Room_Number: ")
    row["Hotel_ID"] = input("Hotel ID: ")

    try:
        query = "INSERT INTO HOTEL_I(isMember,isOccupied,Room_Type,Price_Day,Room_Number,Hotel_ID) VALUES(NULL,0,'%s', '%s', '%s', '%s')" % (
            row["Room_Type"], row["Price_Day"], row["Room_Number"], row["Hotel_ID"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    return


def addHotel():
    global cur
    row = {}
    print("Enter the new hotel's details: ")
    row["Hotel_ID"] = input("Hotel ID: ")
    row["Hotel_Name"] = input("Hotel_Name: ")
    row["Location"] = input("Location: ")
    row["Manager_ID"] = input("Manager_ID: ")

    # shift that employee to that hotel
    try:
        query = "UPDATE EMPLOYEE SET HOTEL_ID='%s' WHERE EMPLOYEE_ID=%s" % (
            row["Hotel_ID"], row["Manager_ID"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return

    try:
        query = "INSERT INTO DESTINATION(Hotel_ID,Hotel_Name,Location,Manager_ID) VALUES('%s', '%s', '%s', '%s')" % (
            row["Hotel_ID"], row["Hotel_Name"], row["Location"], row["Manager_ID"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return


    return


def addRecreation():
    global cur
    row = {}
    print("Enter the new recreations's details: ")
    row["Hotel_ID"] = input("Hotel ID: ")
    row["Service_Provider"] = input("Service Provider: ")
    row["Supervisor_ID"] = input("Supervisor ID: ")
    try:
        row["Profit"] = int(input("Profit Received: "))
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")

    try:
        query = "SELECT HOTEL_ID FROM EMPLOYEE WHERE EMPLOYEE_ID=%s" % (
            row["Supervisor_ID"])
        cur.execute(query)
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    x = cur.fetchone()
    con.commit()

    # Supervisor must exist in that hotel
    if x["HOTEL_ID"] == row["Hotel_ID"]:
        try:
            query = "INSERT INTO RECREATION(Hotel_ID,Service_Provider,Supervisor_ID,Profit) VALUES('%s', '%s', '%s', %d)" % (
                row["Hotel_ID"], row["Service_Provider"], row["Supervisor_ID"], row["Profit"])
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return

    else:
        print("Supervisor does not work in this hotel")
    return


def addFacilitiesAvailed():
    member_id = input("Enter Member ID: ")
    provider = input("Enter Service Provider: ")

    query="SELECT HOTEL_ID FROM MEMBER_GUESTS WHERE MEMBER_ID=%s" % (member_id)
    cur.execute(query)
    x=cur.fetchone()
    if x==None:
        print("----------------------------------------\nMember currently not staying in any hotel!\n----------------------------------------\n")
        return
    else:
        query="SELECT * FROM RECREATION WHERE SERVICE_PROVIDER='%s' AND HOTEL_ID='%s'" % (provider,x['HOTEL_ID'])
        cur.execute(query)
        x2=cur.fetchone()
        if x2==None:
            print("----------------------------------------\nThis service is not available in the hotel the member is staying in!\n----------------------------------------\n")
            return       

    try:
        query = "SELECT MEMBER_ID, SERVICE_PROVIDER FROM FACILITIES_AVAILED WHERE MEMBER_ID='%s' AND SERVICE_PROVIDER='%s'" % (
            member_id, provider)
        cur.execute(query)
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    x = cur.fetchone()

    if x == None:
        query = "INSERT INTO FACILITIES_AVAILED(MEMBER_ID, SERVICE_PROVIDER,NUMBER_OF_TIMES) VALUES('%s', '%s',1)" % (
            member_id, provider)
    else:
        query = "UPDATE FACILITIES_AVAILED SET NUMBER_OF_TIMES=NUMBER_OF_TIMES+1 WHERE MEMBER_ID='%s' AND SERVICE_PROVIDER='%s'" % (
            member_id, provider)

    cur.execute(query)
    con.commit()
    return


def getFinancialReport():
    global cur
    # query = "MONTH"
    print("Enter the MM from which you want to see the registered members: ")
    month = input("(01-12): ")
    if month == "01":
        m = "January"
    elif month == "02":
        m = "February"
    elif month == "03":
        m = "March"
    elif month == "04":
        m = "April"
    elif month == "05":
        m = "May"
    elif month == "06":
        m = "June"
    elif month == "07":
        m = "July"
    elif month == "08":
        m = "August"
    elif month == "09":
        m = "September"
    elif month == "10":
        m = "October"
    elif month == "11":
        m = "November"
    elif month == "12":
        m = "December"

    try:
        query = "SELECT * FROM FINANCE F WHERE F.MONTH=%s ORDER BY HOTEL_ID ASC;"
        no_of_rows = cur.execute(query, m)
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return

    rows = cur.fetchall()
    viewTable(rows)
    con.commit()


def changeStay():
    global cur
    row = {}
    print("Enter details:")
    row["Hotel_ID"] = input("Hotel ID: ")
    row["Room_Number"] = input("Room Number: ")
    print("Enter new Checkout Date(YYYY-MM-DD): ")
    newday = input()
    args = (newday.split("-"))
    try:
        pydy = datetime.datetime(int(args[0]), int(args[1]), int(args[2]))
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")

    if datetime.datetime.now() > pydy:
        print("Can't enter a date that has already passed")
    else:
        try:
            query="SELECT isMember, isOccupied FROM HOTEL_I WHERE HOTEL_ID=%s AND ROOM_NUMBER=%s" % (
                    row["Hotel_ID"], row["Room_Number"])
            cur.execute(query)
        except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
            return
        x=cur.fetchone()    
        con.commit()
        
        if x["isOccupied"]==0:
            print("ROOM IS NOT OCCUPIED\n")
            

        else:
            if x["isMember"]==1:
                query = "UPDATE MEMBER_GUESTS SET Check_Out_Date='%s' WHERE HOTEL_ID='%s' AND ROOM_NO='%s'" % (
                    newday, row["Hotel_ID"], row["Room_Number"])
            else:
                query = "UPDATE NON_MEMBER_GUESTS SET Check_Out_Date='%s' WHERE HOTEL_ID='%s' AND ROOM_NO='%s'" % (
                    newday, row["Hotel_ID"], row["Room_Number"])
            
            try:
                cur.execute(query)
                con.commit()
            except Exception as e:
                print(e)
                print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
                return


def updateManager():
    global cur
    row = {}
    print("Enter the new hotel's details: ")
    row["Hotel_ID"] = input("Hotel ID: ")
    row["Manager_ID"] = input("Manager_ID: ")
    try:
        query = "SELECT HOTEL_ID FROM EMPLOYEE WHERE EMPLOYEE_ID=%s" % (
            row["Manager_ID"])
        cur.execute(query)
    except Exception as e:
        print(e)
        print("Please try with different data")
        return
    x = cur.fetchone()
    con.commit()

    # Supervisor must exist in that hotel
    if x["HOTEL_ID"] == row["Hotel_ID"]:
        try:
            query = "UPDATE DESTINATION SET Manager_ID='%s' WHERE Hotel_ID=%s" % (
                row["Manager_ID"], row["Hotel_ID"])
            cur.execute(query)
            con.commit()
        except Exception as e:
            print(e)
            print("Please try with different data")
            return
    else:
        print("Employee does not work in this hotel")
    return


def viewTable(rows):

    a = []
    try:
        a.append(list(rows[0].keys()))
    except:
        print("\n-----------------\nEMPTY TABLE\n-----------------\n")   
        return
    for row in rows:
        b = []
        for k in row.keys():
            b.append(row[k])
        a.append(b)
    print(tabulate(a, tablefmt="psql", headers="firstrow"))
    print()
    return


def viewOptions():
    print("Choose a VIEW option\n\n")
    print("1.  DESTINATION")
    print("2.  MEMBERS")
    print("3.  MEMBER_PACKAGE")
    print("4.  MEMBER_ADDRESS")
    print("5.  MEMBER_PHONE")
    print("6.  FINANCE")
    print("7.  EMPLOYEE")
    print("8.  EMPLOYEE_ADDRESS")
    print("9.  EMPLOYEE_PHONE")
    print("10. MEMBER_GUESTS")
    print("11. NON_MEMBER_GUESTS")
    print("12. RECREATION")
    print("13. PROVIDERS_SERVICES")
    print("14. HOTEL_I")
    print("15. FACILITIES_AVAILED")
    print("16. MEMBER GUEST WHO?")
    print("17. NON MEMBER GUEST WHO?")
    print("18. LATEST MEMBERS")
    print("19. FINANCIAL REPORT")
    print("\n\n")
    n = input()

    if n == '1':
        query = "SELECT * FROM DESTINATION;"
    elif n == '2':
        query = "SELECT * FROM MEMBERS;"
    elif n == '3':
        query = "SELECT * FROM MEMBER_PACKAGE;"
    elif n == '4':
        query = "SELECT * FROM MEMBER_ADDRESS;"
    elif n == '5':
        query = "SELECT * FROM MEMBER_PHONE;"
    elif n == '6':
        query = "SELECT * FROM FINANCE;"
    elif n == '7':
        query = "SELECT * FROM EMPLOYEE;"
    elif n == '8':
        query = "SELECT * FROM EMPLOYEE_ADDRESS;"
    elif n == '9':
        query = "SELECT * FROM EMPLOYEE_PHONE;"
    elif n == '10':
        query = "SELECT * FROM MEMBER_GUESTS;"
    elif n == '11':
        query = "SELECT * FROM NON_MEMBER_GUESTS;"
    elif n == '12':
        query = "SELECT * FROM RECREATION;"
    elif n == '13':
        query = "SELECT * FROM PROVIDERS_SERVICES;"
    elif n == '14':
        query = "SELECT * FROM HOTEL_I;"
    elif n == '15':
        query = "SELECT * FROM FACILITIES_AVAILED"
    elif n == '16':
        x = input("Hotel ID: ")
        query = "SELECT M2.FIRST_NAME, M2.LAST_NAME, M.CHECK_IN_DATE, M.CHECK_OUT_DATE FROM MEMBER_GUESTS M, MEMBERS M2 WHERE M2.MEMBER_ID=M.MEMBER_ID AND M.HOTEL_ID=%s;" % (
            x)
    elif n == '17':
        x = input("Hotel ID: ")
        query = "SELECT FIRST_NAME, LAST_NAME, CHECK_IN_DATE, CHECK_OUT_DATE FROM NON_MEMBER_GUESTS M WHERE M.HOTEL_ID=%s;" % (
            x)
    elif n == '18':
        print("Enter the YYYY-MM from which you want to see the registered members")
        m = input() + "-01"
        query = "SELECT * FROM MEMBERS WHERE DATE_OF_REG >= '%s';" % (m)
    elif n == '19':
        getFinancialReport()
        return

    try:
        no_of_rows = cur.execute(query)
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return

    rows = cur.fetchall()
    viewTable(rows)
    con.commit()


def addOptions():

    print("Choose an ADDITION option\n\n")
    print("1. DESTINATION")
    print("2. MEMBERS")
    print("3. MEMBER_PACKAGE")
    print("4. FINANCE")
    print("5. EMPLOYEE")
    print("6. MEMBER_GUESTS")
    print("7. NON_MEMBER_GUESTS")
    print("8. RECREATION")
    print("9. PROVIDERS_SERVICES")
    print("10. ROOMS")
    print("11. FACILITIES AVAILED")
    print("\n\n")
    n = input()

    if n == '1':
        addHotel()
    elif n == '2':
        addMember()
    elif n == '3':
        addPackage()
    elif n == '4':
        addFinance()
    elif n == '5':
        addEmployee()
    elif n == '6':
        addMemberGuest()
    elif n == '7':
        addNonMemberGuest()
    elif n == '8':
        addRecreation()
    elif n == '9':
        addServiceProvider()
    elif n == '10':
        addRoom()
    elif n == '11':
        addFacilitiesAvailed()


def deleteOptions():
    print("Choose a DELETION option\n\n")
    print("1.  DESTINATION")
    print("2.  MEMBERS")
    print("3.  MEMBER_PACKAGE")
    print("4.  MEMBER_ADDRESS")
    print("5.  MEMBER_PHONE")
    print("6.  FINANCE")
    print("7.  EMPLOYEE")
    print("8.  EMPLOYEE_ADDRESS")
    print("9.  EMPLOYEE_PHONE")
    # print("10. MEMBER_GUESTS")
    # print("11. NON_MEMBER_GUESTS")
    print("10. RECREATION")
    print("11. PROVIDERS_SERVICES")
    # print("12. HOTEL_I")
    # print("12. FACILITIES AVAILED")
    print("\n\n")
    n = input()

    if n == '1':
        x = input("Enter Hotel ID: ")
        query = "DELETE FROM DESTINATION WHERE HOTEL_ID='%s';" % (x)
    elif n == '2':
        x = input("Enter Member ID: ")
        query = "DELETE FROM MEMBERS WHERE MEMBER_ID='%s';" % (x)
    elif n == '3':
        x1 = input("Enter Member ID: ")
        x2 = input("Enter Member Package: ")
        query = "DELETE FROM MEMBERS M WHERE M.MEMBER_ID='%s' AND M.PACKAGE='%s';" % (
            x1, x2)
    elif n == '4':
        x1 = input("Enter Member ID: ")
        x2 = input("Enter Member Address: ")
        query = "DELETE FROM MEMBERS M WHERE M.MEMBER_ID='%s' AND M.ADDRESS='%s';" % (
            x1, x2)
    elif n == '5':
        x1 = input("Enter Member ID: ")
        x2 = input("Enter Member Phone: ")
        query = "DELETE FROM MEMBERS M WHERE M.MEMBER_ID='%s' AND M.PH_NO='%s';" % (
            x1, x2)
    elif n == '6':
        x1 = input("Enter Hotel ID: ")
        x2 = input("Enter Month: ")
        query = "DELETE FROM FINANCE F WHERE F.HOTEL_ID='%s' AND F.MONTH='%s';" % (
            x1, x2)
    elif n == '7':
        x = input("Enter Employee ID: ")
        query = "DELETE FROM EMPLOYEE WHERE EMPLOYEE_ID='%s';" % (x)
    elif n == '8':
        x1 = input("Enter Employee ID: ")
        x2 = input("Enter Address: ")
        query = "DELETE FROM EMPLOYEE E WHERE E.EMPLOYEE_ID='%s' AND E.ADDRESS='%s';" % (
            x1, x2)
    elif n == '9':
        x1 = input("Enter Hotel ID: ")
        x2 = input("Enter Phone: ")
        query = "DELETE FROM EMPLOYEE E WHERE E.HOTEL_ID='%s' AND E.Ph_No='%s';" % (
            x1, x2)
    elif n == '10':
        x1 = input("Enter Hotel ID: ")
        x2 = input("Enter Service_Provider: ")
        query = "DELETE FROM RECREATION R WHERE R.HOTEL_ID='%s' AND R.SERVICE_PROVIDER='%s';" % (
            x1, x2)
    elif n == '11':
        x= input("Enter Service Provider: ")
        query = "DELETE FROM PROVIDERS_SERVICES WHERE SERVICE_PROVIDER='%s';" % (x)

    try:
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return


def updateOptions():
    print("Choose an UPDATE option\n\n")
    print("1.  EMPLOYEE SALARY")
    print("2.  CHECK OUT DATE")
    print("3.  UPDATE MANAGER")
    print("\n\n")
    n =input()

    if n == '1':
        id = input("Enter the Employee_ID for which you want to update salary: ")
        try:
            salary = int(input("Enter the new salary: "))
        except Exception as e:
            print(e)
            print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")

        query = "UPDATE EMPLOYEE SET SALARY = %d WHERE Employee_ID = %s;" % (
            salary, id)
    elif n == '2':
        changeStay()
        return
    elif n=='3' :
        updateManager()
        return

    try:
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
    return


def refreshDatabase():
    global cur

    # Deleting incorrectly entered data in insert function
    try:
        query="UPDATE HOTEL_I H,MEMBER_GUESTS M SET ISOCCUPIED=0,ISMEMBER=NULL WHERE M.Room_No=H.Room_Number AND M.Hotel_ID=H.Hotel_ID AND Check_In_Date>=CURRENT_DATE"
        cur.execute(query)
        con.commit()
        query="DELETE FROM FACILITIES_AVAILED WHERE MEMBER_ID IN(SELECT MEMBER_ID FROM MEMBER_GUESTS WHERE Check_In_Date>=CURRENT_DATE)"
        cur.execute(query)
        con.commit()
        query="DELETE FROM MEMBER_GUESTS WHERE Check_In_Date>=CURRENT_DATE"
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
    
    try:
        query="UPDATE HOTEL_I H,NON_MEMBER_GUESTS M SET ISOCCUPIED=0,ISMEMBER=NULL WHERE M.Room_No=H.Room_Number AND M.Hotel_ID=H.Hotel_ID AND Check_In_Date>=CURRENT_DATE"
        cur.execute(query)
        con.commit()
        query="DELETE FROM NON_MEMBER_GUESTS WHERE Check_In_Date>=CURRENT_DATE"
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)

    #Deleting Cheked out Guests
    try:
        query="UPDATE HOTEL_I H,MEMBER_GUESTS M SET ISOCCUPIED=0,ISMEMBER=NULL WHERE M.Room_No=H.Room_Number AND M.Hotel_ID=H.Hotel_ID AND Check_Out_Date<CURRENT_DATE"
        cur.execute(query)
        con.commit()
        query="DELETE FROM FACILITIES_AVAILED WHERE MEMBER_ID IN(SELECT MEMBER_ID FROM MEMBER_GUESTS WHERE Check_Out_Date<CURRENT_DATE)"
        cur.execute(query)
        con.commit()
        query="DELETE FROM MEMBER_GUESTS WHERE Check_Out_Date<CURRENT_DATE"
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)

    try: 
        query="UPDATE HOTEL_I H,NON_MEMBER_GUESTS M SET ISOCCUPIED=0,ISMEMBER=NULL WHERE M.Room_No=H.Room_Number AND M.Hotel_ID=H.Hotel_ID AND Check_Out_Date<CURRENT_DATE"
        cur.execute(query)
        con.commit()
        query="DELETE FROM NON_MEMBER_GUESTS WHERE Check_Out_Date<CURRENT_DATE"
        cur.execute(query)
        con.commit() 
    except Exception as e:
        print(e)

while(1):
    tmp = sp.call('clear', shell=True)
    # username = input("Username: ")
    # password = input("Password: ")
    username="tanvi"
    password="password"

    try:
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='RESORT',
                              cursorclass=pymysql.cursors.DictCursor)
    except Exception as e:
        print(e)
        #tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
        continue

    with con:
        cur = con.cursor()
        exitflag = 0
        while(1):
            # tmp = sp.call('clear', shell=True)
            refreshDatabase()
            print("CHOOSE AN OPTION\n")
            print("1.View Options")
            print("2.Addition Options")
            print("3.Deletion Options")
            print("4.Modify Options")
            print("5.Quit")
            inp = input("\nCHOICE ? ")
            if(inp == '1'):
                viewOptions()
            elif(inp == '2'):
                addOptions()
            elif(inp == '3'):
                deleteOptions()
            elif(inp == '4'):
                updateOptions()
            elif(inp == '5'):
                    exitflag = 1
                    print("Bye")
                    break

    if exitflag == 1:
        break
