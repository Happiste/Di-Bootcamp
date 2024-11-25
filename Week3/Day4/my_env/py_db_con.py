import psycopg2
import requests

# HOSTNAME = 'localhost'
# USERNAME = 'postgres'
# PASSWORD = '1234'
# DATABASE = 'dvdrental'

# connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )

# cursor = connection.cursor()

# query = "SELECT * FROM customer LIMIT 20;"

# cursor.execute(query)

# results = cursor.fetchall()

# connection.close()

# for item in results:
#         print(item) 


connection = psycopg2.connect(database = 'postgres',
                              user = 'postgres',
                              password = '1234',
                              host='localhost',
                              port='5432')
connection.autocommit = True
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS random_countries')
create_table_query = f'''CREATE TABLE random_countries (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        capital VARCHAR(100) NOT NULL,
                        flag_code VARCHAR(100),
                        population INTEGER)'''




if __name__:'__main__':
