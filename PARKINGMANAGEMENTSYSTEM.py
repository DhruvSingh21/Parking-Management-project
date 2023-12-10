import os
import platform
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="mysql") 
mycursor=mydb.cursor()


#CREATING DATABASE AND TABLE

mycursor.execute("create database if not exists parking")
mycursor.execute("use parking")

print(" Creating Parkmaster12 table")
sql = "CREATE TABLE if not exists parkmaster12 (\
        pid int(8) primary key,\
	pnm varchar(30) not null,\
	level varchar(30) not null,\
	freespace varchar(30) not null,\
	vehicleno varchar(30) not null,\
	nod varchar(30) not null,\
	payment int(5) not null)";

mycursor.execute(sql)
print(" parkmaster12 table created")


print(" Creating Vehicle table")
sql = "CREATE TABLE if not exists vehicle (\
	vid int(8) primary key,\
	vnm varchar(30) not null,\
	dateofpur date)";

mycursor.execute(sql)
print(" Vehicle table created")


def Add_Record():
    L=[]
    id1=int(input("Enter the parking number : "))
    L.append(id1)
    pname1=input("Enter the Parking Name: ")
    L.append(pname1)
    level1=input("Enter level of parking : ")
    L.append(level1)
    freespace1=input("Is there any freespace or not :YES/NO ")
    L.append(freespace1)
    vehicleno1=input("Enter the Vehicle Number : ")
    L.append(vehicleno1)
    nod1=int(input("Enter total number of days for parking: "))
    L.append(nod1)
    if nod1==1:
        Payment1=20
    elif nod1==2:
         Payment1=40
    elif nod1==3:
         Payment1=60
    elif nod1==4:
          Payment1=80
    elif nod1==5:
          Payment1=100
    elif nod1==6:
           Payment1=6969
    
    L.append(Payment1)
    stud=(L)
    sql='insert into parkmaster12(pid,pnm,level,freespace,vehicleno,nod,payment) values(%s,%s,%s,%s,%s,%s,%s)'
    mycursor.execute(sql,stud)
    mydb.commit()
def Rec_View():
    print("Select the search criteria : ")
    print("1. Parking Number")
    print("2. Parking Name")
    print("3. Level No")
    print("4. All")
    ch=int(input("Enter the choice : "))
    if ch==1:
       s=int(input("Enter Parking no : "))
       rl=(s,)
       sql="select * from parkmaster12 where pid=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==2:
       s=input("Enter Parking Name : ")
       rl=(s,)
       sql="select * from parkmaster12 where pnm=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==3:
       s=int(input("Enter Level of Parking : "))
       rl=(s,)
       sql="select * from parkmaster12 where level=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==4:
       sql="select * from parkmaster12"
       mycursor.execute(sql)
       res=mycursor.fetchall()
       print("Details about Parking are as follows : ")
       print("(Parking Id,Parking Name,Level,FreeSpace(Y/N),Vehicle No,No of days for parking,Payment)")
    for x in res:
        print(x)
    print('Task completed')
def Vehicle_Detail():
    L=[]
    vid1=int(input("Enter Vehicle No : "))
    L.append(vid1)
    vnm1=input("Enter Vehicle Name/Model Name : ")
    L.append(vnm1)
    dateofpur1=input("Enter Year-Month-date of purchase : ")
    L.append(dateofpur1)
    vdt=(L)
    sql="insert into vehicle(vid,vnm,dateofpur) values(%s,%s,%s)"
    mycursor.execute(sql,vdt)
    mydb.commit()
def Vehicle_View():   
    print("Select the search criteria : ")
    print("1. vehicle Number")
    print("2. vehicle Name")
    print("3. Enter Year-Month-date of purchase")
    print("4. All")
    ch=int(input("Enter the choice : "))
    if ch==1:
       s=int(input("Enter vehicle no : "))
       rl=(s,)
       sql="select * from vehicle where vid=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==2:
       s=input("Enter vehicle Name : ")
       rl=(s,)
       sql="select * from vehicle where vnm=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==3:
       s=int(input("Enter Enter Year-Month-date of purchase : "))
       rl=(s,)
       sql="select * from vehicle where dateofpur=%s"
       mycursor.execute(sql,rl)
       res=mycursor.fetchall()
    elif ch==4:
       sql="select * from vehicle"
       mycursor.execute(sql)
       res=mycursor.fetchall()
       print("Details about vehicle are as follows : ")
    for x in res:
        print(x)
    print('Task completed')
def remove():
    vid1=int(input("Enter the vehicle number of the vehicle to be deleted : "))
    rl=(vid1,)
    sql="Delete from vehicle where vid=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
    print('Removed as per the command')
def Menu():
    print("Enter 1 : To Add Parking Detail")
    print("Enter 2 : To View Parking Detail ")
    print("Enter 3 : To Add Vehicle Detail ")
    print("Enter 4 : To Remove Vehicle Record")
    print("Enter 5 : To see the details of Vehicle")
    input_dt = int(input("Please Select An Above Option: "))
    if(input_dt== 1):
       Add_Record()
    elif (input_dt==2):
        Rec_View()
    elif (input_dt==3):
        Vehicle_Detail()
    elif (input_dt==4):
        remove()
    elif (input_dt==5):
        Vehicle_View()
    else:
       print("Enter correct choice....")
Menu()
def runAgain():
    runAgn=input('\nwant to run Again Y/n:')
    while(runAgn.lower()=='y'):
        if(platform.system()=='Windows'):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        Menu()
runAgain()
