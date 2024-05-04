import psycopg2
from config import host, user, password, db_name
'''
CREATE OR REPLACE FUNCTION ins_or_upd(name VARCHAR(20),phone VARCHAR(11))
RETURNS VOID AS
$$
BEGIN
IF EXISTS (SELECT 1 FROM phonebook1 WHERE phonebook1.username = $1) THEN
UPDATE phonebook1 SET number = $2 WHERE username = $1;
ELSE
INSERT INTO phonebook1 (username,number) VALUES ($1,$2);
END IF;
END;
$$
LANGUAGE plpgsql;
'''
connection = psycopg2.connect(
    host = host,
    user = user,
    password = password,
    database = db_name
)
connection.autocommit = True
cursor = connection.cursor()
name = input('Enter name: ')
phone = input('Enter number: ')
cursor.callproc('ins_or_upd',(name,phone))
cursor.close()
connection.close()