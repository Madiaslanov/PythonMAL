import psycopg2
from config import host, user, password,db_name

connection = psycopg2.connect(
    host = host,
    database = db_name,
    user = user,
    password = password
)
connection.autocommit = True
cursor = connection.cursor()

sql = ''' 
DELETE FROM phonebook1 WHERE username = %s;
'''
username = input('Which user you want to delete from this table?: ')
cursor.execute(sql % username)
cursor.close()
connection.close()
