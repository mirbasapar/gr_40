import sqlite3

def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

sql_to_create_table = '''CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL, 
    price FLOAT(10,2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)'''

def insert_products(connection, products):
    sql = '''INSERT INTO products (product_title, price, quantity) 
    VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_products_q(connection, product):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_products_p(connection, product):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def delete_products(connection, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(connection):
    sql = '''SELECT * FROM products'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_limit(connection, price_limit, quantity_limit):
    sql = '''SELECT * FROM products WHERE price < ? and quantity > ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (price_limit, quantity_limit))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_like(connection, title):
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, ('%' + title + '%',))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


my_connection = create_connection('hw.db')
if my_connection is not None:
    print('Successfully connected!')
    # create_table(my_connection, sql_to_create_table)
    # insert_products(my_connection, ("Детское мыло", 30.0, 50))
    # insert_products(my_connection,("Молоко", 50.0, 10))
    # insert_products(my_connection,("Хлеб", 30.0, 20))
    # insert_products(my_connection,("Яблоки", 70.0, 15))
    # insert_products(my_connection,("Картофель", 20.0, 30))
    # insert_products(my_connection,("Мясо говядины", 300.0, 5))
    # insert_products(my_connection,("Рис", 40.0, 10))
    # insert_products(my_connection,("Помидоры", 60.0, 12))
    # insert_products(my_connection,("Йогурт", 40.0, 8))
    # insert_products(my_connection,("Паста", 25.0, 15))
    # insert_products(my_connection,("Куриные яйца", 50.0, 20))
    # insert_products(my_connection,("Макароны", 35.0, 10))
    # insert_products(my_connection,("Сок апельсиновый", 80.0, 6))
    # insert_products(my_connection,("Чай черный", 100.0, 5))
    # insert_products(my_connection,("Колбаса", 200.0, 3))
    # insert_products(my_connection,("Мыло с запахом малины", 50.0, 7))
    # update_products_q(my_connection, (250, 6))
    # update_products_p(my_connection, (280, 6))
    # delete_products(my_connection, 15)
    # select_all_products(my_connection)
    # select_products_by_limit
    select_products_by_like(my_connection, 'мыло')

    my_connection.close()
