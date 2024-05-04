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

try:
    id = input('Enter ID: ')
    change = input('What do you want to change?: ')
    data = input('To what value set the old value?: ')
    change = change.lower()
    sql = '''
    UPDATE phonebook1 SET %s = %%s WHERE id = %%s;
    '''
    cursor.execute(sql % change, [data, id])
except Exception as e:
    pass

cursor.close()
connection.close()