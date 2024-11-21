import psycopg2
import json
import requests
import random

def link():
    try:
        connection = psycopg2.connect(database = 'postgres',
                                    user = 'postgres',
                                    password = '1234',
                                    host = 'localhost',
                                    port = '5432'

        )
        connection.autocommit = True
        cursor = connection.cursor()
        return connection, cursor   
    except psycopg2.Error:
        print(f'CONNECTION ERROR {psycopg2.Error}')
        return None, None
    
def create_table():
    connection, cursor =  link()
    if connection is None or cursor is None:
        print("Unable to create the table, connection failed.")
        return
    cursor.execute('DROP TABLE IF EXISTS random_countries')
    create_table_query = f'''CREATE TABLE random_countries (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        capital VARCHAR(100) NOT NULL,
                        flag_code VARCHAR(100),
                        population INTEGER)'''

    cursor.execute(create_table_query)
    cursor.close()
    connection.close()
    print('the table has been created succesfuly !')


    
def main():
    create_table()
    connecion, cursor = link()
    response = requests.get('https://restcountries.com/v3.1/all')
    data = response.json()
    try:
        for _ in range(10):
            index = random.randint(1, len(data) - 1)
            try:
                name = data[index]['name']['official']
            except:
                name = data[index]['name']['official'][0]
                
            name = name.replace('\'', '`')
            capital = data[index]['capital'][0]
            flag_code = data[index]['flag']
            population = data[index]['population']

            query = '''INSERT INTO random_countries (name, capital, flag_code, population)
            VALUES (%s,%s,%s,%s)'''
            cursor.execute(query, (name, capital, flag_code, population))
    finally:
        cursor.close()
        connecion.close()
    print('Sucessfully added to db')

main()
   


















