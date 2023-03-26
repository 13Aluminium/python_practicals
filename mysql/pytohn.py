import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user="21dce052",
    password="asdf1234",
    database ="luffy"
)
# print(conn)
# mycursor = conn.cursor()
# import mysql.connector
# conn=mysql.connector.connect(
#     host="localhost",
#     user="vatsal",
#     password="vatsal2003",
#     database="pythondb"
# )
# print(conn)
mycursor=conn.cursor()
# mycursor.execute("create database naruto")
# mycursor.execute("create table employee (emp_name int,emp_sal int)")
# sql="insert into employee(emp_name,emp_sal) values ('vatsal',500)"


# sql="update employee set emp_sal=109990 where emp_name='0'"
# mycursor.execute(sql)
sql="select * from employee"
mycursor.execute(sql)


# sql="create table employee (emp_name char(20),emp_sal int)"
# print(mycursor.fetchall())
conn.commit()
print(conn)

