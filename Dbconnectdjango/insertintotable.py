import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    auth_plugin="mysql_native_password",
    database="college"
)

cursor=db.cursor()

sql="insert into employee values('1009','Vijay','developer','34000')"
cursor.execute(sql)
db.commit()
db.close()
