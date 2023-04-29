#Accept desg from user and display name of emp for given desg

import mysql.connector
con=mysql.connector.connect(host="localhost",user='root',
                            password='',database='pythondb')
cur=con.cursor()

d=input("Enter desgnation ")
cur.execute("select name from employee where desg='{}'".format(d))
l=cur.fetchall()
cnt=(cur.rowcount)
if cnt>0:
    for rec in l:
        print(rec[0])
else:
    print("given desg not found")
