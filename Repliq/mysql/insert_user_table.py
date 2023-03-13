import mysql.connector
import random

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="repliq")

mycursor = db.cursor()
mycursor.execute("INSERT INTO user (user_name, dev_id_f) VALUES (%s, %s)", ("John", random.randint(1, 5)))
mycursor.execute("INSERT INTO user (user_name, dev_id_f) VALUES (%s, %s)", ("Bruce Wayne", random.randint(1, 5)))
mycursor.execute("INSERT INTO user (user_name, dev_id_f) VALUES (%s, %s)", ("Kal El", random.randint(1, 5)))
mycursor.execute("INSERT INTO user (user_name, dev_id_f) VALUES (%s, %s)", ("Ash Ketchum", random.randint(1, 5)))
mycursor.execute("INSERT INTO user (user_name, dev_id_f) VALUES (%s, %s)", ("Jon Jones", random.randint(1, 5)))
db.commit()

print("Data has been inserted")




