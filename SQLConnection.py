import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="root" )  #we can also pass database name here.

mycursor = mydb.cursor()  #points to database

mycursor.execute("show databases")

for i in mycursor:
    print(i)


mycursor.execute("use practice")

mycursor.execute("select * from student")

result = mycursor.fetchall()    #fetch all the data

for i in result:
    print(i)

mycursor.execute("select * from student")
result = mycursor.fetchmany(3)    #fetch number of data specified in argument
for i in result:
    print(i)


#mycursor.execute("select * from student")

result = mycursor.fetchone()    #fetch 1st data
print(result)
