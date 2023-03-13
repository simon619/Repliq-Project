import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="repliq")

mycursor = db.cursor()
mycursor.execute("CREATE TABLE user (user_name varchar(50), user_id int PRIMARY KEY AUTO_INCREMENT, dev_id_f int, FOREIGN KEY (dev_id_f) REFERENCES device(dev_id))")
print("Table has been created")