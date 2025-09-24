import mysql .connector 
from data import info;

try:
    mysql.connector.connect(**info)
    print("connection succesful")
except:
    print("no")