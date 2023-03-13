import mysql.connector
import random

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="repliq")

mycursor = db.cursor()
mycursor.execute("INSERT into company (com_name, dev_status, user_id_f) VALUES (%s, %s, %s)", ("GameDay Catering", "available", random.randint(1, 5)))
mycursor.execute("INSERT into company (com_name, dev_status, user_id_f) VALUES (%s, %s, %s)", ("Darwin Travel", "not available", random.randint(1, 5)))
mycursor.execute("INSERT into company (com_name, dev_status, user_id_f) VALUES (%s, %s, %s)", ("Acorn Crafts", "available", random.randint(1, 5)))
mycursor.execute("INSERT into company (com_name, dev_status, user_id_f) VALUES (%s, %s, %s)", ("Exploration Kids", "broken", random.randint(1, 5)))
mycursor.execute("INSERT into company (com_name, dev_status, user_id_f) VALUES (%s, %s, %s)", ("Games Stops", "avaible", random.randint(1, 5)))
db.commit()

print("Data has been inserted")