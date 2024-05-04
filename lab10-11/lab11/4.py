import psycopg2
from config import host, user, password,db_name

'''
CREATE OR REPLACE FUNCTION get_phonebook(_limit integer, _offset integer)
RETURNS TABLE(id bigint, username text, phonenumber text) AS $$
BEGIN
  RETURN QUERY SELECT MyPhoneBook.id, MyPhoneBook.username, MyPhoneBook.phonenumber FROM MyPhoneBook ORDER BY id LIMIT _limit OFFSET _offset;
END;
$$ LANGUAGE plpgsql;
'''

connection = psycopg2.connect(
    host = host,
    password = password,
    user = user,
    database = db_name
)
connection.autocommit = True
cursor = connection.cursor()
limit = input("Enter limit: ")
offset = input("Enter offset: ")
cursor.execute("SELECT * FROM get_phonebook1(%s,%s)",(limit,offset))
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
connection.close()