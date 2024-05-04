import psycopg2
from config import host, user, password, db_name

connection = psycopg2.connect(
    host = host,
    database = db_name,
    user = user,
    password = password,
)
connection.autocommit = True
cursor = connection.cursor()
cursor.execute(
'''
CREATE TABLE phonebook1 (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    number VARCHAR(11) NOT NULL,
    email VARCHAR(30) NOT NULL
);
'''
)  
cursor.close()
connection.close()