import mysql.connector

# Step 1: Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Naveen@93"
)
cursor = conn.cursor()

# Step 2: Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS `10000coders`")
print("✅ Database '10000coders' created")

cursor.close()
conn.close()

# Step 3: Connect to the new database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Naveen@93",
    database="10000coders"
)
cursor = conn.cursor()

# Step 4: Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS `53Rbatch` (
    sno INT,
    sname VARCHAR(100),
    semail VARCHAR(90),
    sgender VARCHAR(90),
    smobile BIGINT
)
""")
print("✅ Table '53Rbatch' created")

# Step 5: Insert demo data
demo_data = [
    (1, "naveen", "naveen@gmail.com", "male", 964215)
    # (2, "ravi", "ravi@gmail.com", "male", 9876543210)
]

cursor.executemany(
    "INSERT INTO `53Rbatch` (sno, sname, semail, sgender, smobile) VALUES (%s, %s, %s, %s, %s)",
    demo_data
)
conn.commit()
print("✅ Demo data inserted")

# update

# Step 6: Fetch and display data
cursor.execute("SELECT * FROM `53Rbatch`")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()