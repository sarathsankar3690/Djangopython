import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password",
    database="college"
)
cursor=db.cursor()
f=open("employee","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    # print(lst)
    sql="insert into employee values(%s,%s,%s,%s)"
    cursor.execute(sql,data)
    db.commit()


