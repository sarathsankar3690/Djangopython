import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password",
    database="college"
)

cursor=db.cursor()
sql="select * from employee"
cursor.execute(sql)
result=cursor.fetchall()
for x in result:
    print(x)