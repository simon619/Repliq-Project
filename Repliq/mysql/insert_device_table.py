import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="repliq")

mycursor = db.cursor()
mycursor.execute("INSERT INTO device (device_name) VALUES (%s)", ("camera", ))
mycursor.execute("INSERT INTO device (device_name) VALUES (%s)", ("laptop", ))
mycursor.execute("INSERT INTO device (device_name) VALUES (%s)", ("mobile", ))
mycursor.execute("INSERT INTO device (device_name) VALUES (%s)", ("laptop", ))
mycursor.execute("INSERT INTO device (device_name) VALUES (%s)", ("laptop", ))
db.commit()

print("Data has been inserted")