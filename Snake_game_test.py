import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', passwd='Admin123', database='python_prac')

mycursor = mydb.cursor()            #point toward perticular databases
mycursor.execute('select * from student')  #cursor is like box where it store the data

result = mycursor.fetchone()
print(result)

for i in mycursor:
    print(i)