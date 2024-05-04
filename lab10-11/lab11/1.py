import psycopg2
from config import host, user, password, db_name
'''
CREATE FUNCTION get_by(p_id INTEGER)
RETURNS TABLE(id INTEGER, username VARCHAR, phonenumber VARCHAR)
AS $$
BEGIN
RETURN QUERY SELECT MyPhoneBook.id, MyPhoneBook.username, MyPhoneBook.phonenumber FROM MyPhoneBook WHERE MyPhoneBook.id = p_id;
END;
$$ LANGUAGE plpgsql;
'''
connection = psycopg2.connect(
    host = host,
    password = password,
    database = db_name,
    user = user
)
connection.autocommit = True
cursor = connection.cursor()
id = input("Enter ID: ")
cursor.callproc('get_by6', id)
row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()
    cursor.close()
connection.close()