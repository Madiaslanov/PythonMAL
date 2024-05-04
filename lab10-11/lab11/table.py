import psycopg2
from config import host, user, password,db_name

connection = psycopg2.connect(
    host = host,
    database = db_name,
    password = password,
    user = user
)
connection.autocommit = True
cursor = connection.cursor()
sql = '''
CREATE TABLE MyPhoneBook(
id BIGSERIAL PRIMARY KEY,
username VARCHAR(20) UNIQUE NOT NULL,
phonenumber VARCHAR(11) UNIQUE NOT NULL
);
'''
cursor.execute(sql)
cursor.close()
connection.close()