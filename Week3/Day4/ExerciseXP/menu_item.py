
import psycopg2

def link():
    try:
        connection = psycopg2.connect(database = 'menu',
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
    cursor.execute('DROP TABLE IF EXISTS menu_items')
    create_table_query = f'''CREATE TABLE menu_items (
                            item_id SERIAL PRIMARY KEY,
                            item_name VARCHAR(100) NOT NULL,
                            item_price SMALLINT DEFAULT 0
                            )'''
    cursor.execute(create_table_query)
    cursor.close()
    connection.close()
    

class MenuItem:
    def __init__(self, name = None, price = None):
       self.name = name
       self.price = price

    def save(self):
        connection, cursor = link()
        if connection is None or cursor is None:
            print("Unable to insert into the the table, connection failed.")
            return
        query = '''insert into menu_items (item_name, item_price)
          values (%s, %s)'''
        cursor.execute(query, (self.name, self.price))
        print(f"{self.name} a ete ajoute au menu au prix de {self.price}")
        cursor.close()
        connection.close()
        

    def delete(self):
        connection, cursor = link()
        if connection is None or cursor is None:
            return
        query =  '''delete from menu_items where item_name = %s'''
        cursor.execute(query, (self.name,))
        print(f"L'item {self.name} a ete suprimme.")
        cursor.close()
        connection.close()
        
        
    def update(self, new_name, new_price):
        connection, cursor = link()
        if connection is None:
            return
        query = '''
        UPDATE menu_items
        SET item_name = %s, item_price = %s
        WHERE item_name = %s;
        '''
        cursor.execute(query, (new_name, new_price, self.name))
        self.name = new_name
        self.price = new_price
        print("l'item a bien ete updater")
        cursor.close()
        connection.close()

    def show(self):
        connection, cursor = link()
        if connection is None:
            return
        query = '''Select * from menu_items'''
        cursor.execute(query)
        result = cursor.fetchall()
        for row in range(len(result)):
            print(row)
            break
        cursor.close() 
        connection.close()



if __name__=='__main__':
    create_table()
    item = MenuItem('Pizza', 55)
    item.save()
    item.update('Shakshuka', 65)
    item.show()

