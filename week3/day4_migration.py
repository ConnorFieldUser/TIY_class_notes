# drop table if it exists

# create table

# loads all your data for you

# think of a databsase for emergency file restore...

# BOILER-PLATE

import psycopg2

connection = psycopg2.connect("dbname=my_first_user user=my_first_user")
cursor = connection.cursor()


cursor.execute("DROP TABLE IF EXISTS person_data;")

create_table_command = """
CREATE TABLE person_data (
    id serial PRIMARY KEY,
    first_name VARCHAR(20),
    password VARCHAR(20),
    birthyear NUMERIC(4),
    bestie VARCHAR(20)
);
"""

cursor.execute(create_table_command)
cursor.execute("INSERT INTO person_data VALUES (1, 'joel', 'safety', 1983, 'big j');")


connection.commit()

cursor.close()
connection.close()

# BOILER-PLATE
