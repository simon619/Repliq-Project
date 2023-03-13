import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="repliq")

mycursor = db.cursor()
mycursor.execute("CREATE TABLE device (device_name varchar(50), dev_id int PRIMARY KEY AUTO_INCREMENT)")
print("Table has been created")