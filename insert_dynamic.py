#Employee(id,name,sal,desg,city)

import mysql.connector
con=mysql.connector.connect(host="localhost",user='root',
                            password='',database='pythondb')
cur=con.cursor()

n=int(input("Enter how many record"))
for i in range(0,n):
    id=int(input("Enter id "))
    nm=input("Enter name ")
    sal=int(input("enter salary"))
    d=input("Enter desg")
    ct=input("Enter city ")

    cur.execute("insert into employee values({},'{}',{},'{}','{}')".format(id,nm,sal,d,ct))

print("record inserted")
print()
cur.execute("select * from employee")
l=cur.fetchall()
for rec in l:
    print(rec[0],rec[1],rec[2],rec[3],rec[4])

