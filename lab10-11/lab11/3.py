import psycopg2
from config import host, password, db_name, user
import json

'''
CREATE OR REPLACE FUNCTION insert_users(users_json json) RETURNS SETOF text AS $$
DECLARE
    user_record json;
    user_name text;
    user_phone text;
    invalid_phones text[] := '{}';
BEGIN
    FOR user_record IN SELECT * FROM json_array_elements(users_json)
    LOOP
        user_name := user_record->>'name';
        user_phone := user_record->>'phone';

        IF LENGTH(user_phone) = 11 AND user_phone ~ '^\d+$' THEN
            INSERT INTO MyPhoneBook (username, phonenumber) VALUES (user_name, user_phone);
        ELSE
            invalid_phones := array_append(invalid_phones, user_record::text);
        END IF;
    END LOOP;

    RETURN QUERY SELECT * FROM unnest(invalid_phones);
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
users = [
    {"name": "Alice", "phone": "87007204060"},
    {"name": "Ben", "phone": "9876543210"},
    {"name": "Charlie", "phone": "555-1234"},
    {"name": "Dave", "phone": "67890"},
]

cursor.execute("SELECT * FROM insert_users(%s);", (json.dumps(users),))
invalid_phones = cursor.fetchall()
print(invalid_phones)

cursor.close()
connection.close()