#Accept desg from user and update the sal of by 5%

import mysql.connector
con=mysql.connector.connect(host="localhost",user='root',
                            password='',database='pythondb')
cur=con.cursor()
d=input("Enter desg ")
cur.execute("update employee set sal=sal+sal*0.05 where desg='{}'".format(d))
cnt=(cur.rowcount)
if (cur.rowcount)>0:    
        print(cnt,"records updated")
        cur.execute("select * from employee where desg='{}'".format(d))
        l=cur.fetchall()
        for rec in l:
            print(rec)
else:
    print("desg not found")
