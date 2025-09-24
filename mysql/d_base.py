import mysql.connector
from db import info
try:
    conn=mysql.connector.connect(
    user='root',
    password='Naveen@93',
    host='localhost',
    port=3306
)
    print("connection successfully")
except:
    print("not")

#cursor is to execute in python 
cursor=conn.cursor()

#create database 
query="CREATE DATAbase if not exists 20k"
cursor.execute(query)

#using database/selecting database
cursor.execute("use 10k")

#create table

try:
    create_table="""create table if not exists students_new(
id int auto_increment primary key,name varchar(90),email varchar(90),course varchar(90),joined_date date
);""" 
    cursor.execute(create_table)
    print("table created successfully")
except mysql.connector.errors.ProgrammingError as e:
    print(e)

#insert single row of data
def insertsinglerow(data):
  try:
    # data=("raju","raju@gmail.com","pfs","2025-03-09")
    insertdata="""insert into students(name,email,course,joined_date) values (%s,%s,%s,%s)"""
    cursor.execute(insertdata,data)
    print("inserted values")
  except:
    print("something went wrong")
# insertsinglerow("raju","raju@gmail.com","pfs","2025-03-09")j
# insertsinglerow("akil","akil@gmail.com","pfs","2025-09-07")

# insertsinglerow((input("enter name:"),input("enter email:"),input("enter course:"),input("enter joindate")))


# #insert multiple row of data
# def insertmultiplerows(data):
#    try:
#        insertquery="""insert into students (name,email,course,joined_data) values(%s,%s,%s,%s)"""
#        cursor.executemany(insertquery,data)
#    except:
#        print("something will be wrong")
# insertmultiplerows ([("vinay","vinay@gmail.com","pfs","2025-08-03"),
#           ("geetha","geetha@gmail.com","jfs","2025-03-06"),
#           ("latha","latha@gmail.com","dsa","2025-09-07")])

# def getrecords():
#    try:
#        query="select*from students"
#        cursor.execute(query)
#        results=cursor.fetchall()
#        print(results)
#        for row in results:
#           print(row)
#    except:
#         print("error occured")
# getrecords()

# def getrecordsofstudentsofsamecourse():



def getlimitedrecords(limit):
   try:
      query="""select*from students order by bane asc limit %s"""
      cursor.execute(query,limit,)
      result=cursor.fetchall()
      print(result)
   except:
      print("something went wrong")
   finally:
       print("task completed")
getlimitedrecords(2)   

def updatecoursebyemail(course,email):
   try:
      query="""update students set course=%s where email=%s"""
      cursor.execute(query,(course,email))
      print("data updated successfully")
   except:
      print("something went wrong")

updatecoursebyemail('ml',"hari@gmail.com")



def deleterecordbyid(id):
   try:
      query="""delete from students where id=%s"""
      cursor.execute(query,(id,))
      print("something deleted")
   except:
      print("something wrong or not deleted")
deleterecordbyid(int(input("enter id:")))


conn.commit()
cursor.close()
conn.close()

