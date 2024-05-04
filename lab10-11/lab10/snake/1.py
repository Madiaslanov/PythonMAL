from config import host, user, password, db_name
import psycopg2

config = psycopg2.connect(
    host=host,
    database=db_name,
    user=user,
    password=password
)
current = config.cursor()

current.execute(
    '''
    CREATE TABLE users_snake2(
        username VARCHAR(20) PRIMARY KEY,
        score INTEGER,
        highscore INTEGER,
        level INTEGER
    )
    '''
)

config.commit()
current.close()
config.close()