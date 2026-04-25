import mysql.connector
from db import info

try:
    conn = mysql.connector.connect(
        user='root',
        password='Naveen@93',
        host='localhost',
        port=3306
    )
    print("Connection successful")
except Exception as e:
    print("No connection:", e)




# import mysql.connector
# from db import info
# try:
#     mysql.connector.connect(**info)
#     print("connection succesful")
# except:
#     print("no connection")