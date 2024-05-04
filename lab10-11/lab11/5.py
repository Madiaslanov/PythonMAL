import psycopg2
from config import host, user, password, db_name

'''
CREATE OR REPLACE PROCEDURE delete_data(name varchar)
AS $$
BEGIN
DELETE FROM MyPhoneBook WHERE username = name;
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
username = input('Enter username: ')
cursor.execute('call delete_data(%s)', (username,))
cursor.close()
connection.close()