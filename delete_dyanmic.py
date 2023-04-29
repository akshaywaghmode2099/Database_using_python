#Write program to accept eno from user and delete that record

import mysql.connector
con=mysql.connector.connect(host="localhost",user='root',
                            password='',database='pythondb')
cur=con.cursor()
no=int(input("Enter emp no ti be deleted"))

cur.execute("delete from employee where eno={}".format(no))
cnt=cur.rowcount
if cnt>0:
    print(cnt," record is deleted ")
else:
    print("eno is not found")
