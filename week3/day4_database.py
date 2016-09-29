# BOILER-PLATE

import psycopg2

connection = psycopg2.connect("dbname=my_first_user")
cursor = connection.cursor()
name = input("What is the first name you want to search for? ")
password = input("Password? ")

cursor.execute("SELECT * FROM person_data WHERE first_name = %s AND last_name = s%;", (name, password))

results = cursor.fetchall()
print(results)

cursor.close()
connection.close()

# BOILER-PLATE
