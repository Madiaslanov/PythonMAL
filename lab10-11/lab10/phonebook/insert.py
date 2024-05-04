import psycopg2
import csv
from config import host, user, password, db_name

connection = psycopg2.connect(
    host=host,
    database=db_name,
    user=user,
    password=password
)
connection.autocommit = True
cursor = connection.cursor()

sql = '''
INSERT INTO phonebook1 (username, number, email)
VALUES (%s, %s, %s);    
'''

try:
    with open(r'C:/Users/madia/OneDrive/Рабочий стол/PythonMAL/lastlab/lab10-11/lab10/phonebook/a.cs') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # Пропускаем заголовок
        for row in reader:
            username = row[0]
            number = row[1]
            email = row[2]
            cursor.execute(sql, (username, number, email))
except Exception as e:
    print("Error:", e)
    username = input('Username: ')
    number = input('Phone number: ')
    email = input('E-mail: ')
    cursor.execute(sql, (username, number, email))

cursor.close()
connection.close()