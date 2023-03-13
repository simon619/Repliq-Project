import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="repliq")

mycursor = db.cursor()
mycursor.execute("CREATE TABLE company (com_name varchar(50), com_id int PRIMARY KEY AUTO_INCREMENT, dev_status varchar(15), user_id_f int, FOREIGN KEY (user_id_f) REFERENCES user(user_id))")
print("Table has been created")