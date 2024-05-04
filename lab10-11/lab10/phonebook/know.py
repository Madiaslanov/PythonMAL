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

data = input('What do you want to know?: ')
id = input('ID of this person?: ')
sql = '''
SELECT %s FROM phonebook1 WHERE id = %%s; 
'''
cursor.execute(sql % data, [id])
print(cursor.fetchone())
cursor.close()
connection.close()
