'''Write a program to
Accept city from user and no of emp live in that city'''


import mysql.connector
con=mysql.connector.connect(host="localhost",user='root',
                            password='',database='pythondb')
cur=con.cursor()
d=input("Enter desg ")
cur.execute("select count(eno) from employee where desg='{}'".format(d))
l=cur.fetchall()
for rec in l:
    print(rec[0])
    
