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

sql_to_create_countries_table = '''CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL
)'''

def insert_countries(connection, countries):
    sql = '''INSERT INTO countries (title) 
    VALUES (?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, countries)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

sql_to_create_cities_table = '''CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL,
    area FLOAT(10,2) NOT NULL DEFAULT 0.0,
    country_id INTEGER DEFAULT NULL
REFERENCES countries (id) ON DELETE NO ACTION
)'''

def insert_cities(connection, cities):
    sql = '''INSERT INTO cities (title, area, country_id) 
    VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, cities)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

sql_to_create_students_table = '''CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(200) NOT NULL,
    last_name VARCHAR(200) NOT NULL,
    city_id INTEGER DEFAULT NULL
REFERENCES cities (id) ON DELETE NO ACTION
)'''

def insert_students(connection, students):
    sql = '''INSERT INTO students (first_name, last_name, city_id) 
    VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, students)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def select_show_cities(connection):
    sql = '''SELECT id, title FROM cities'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, )

        rows = cursor.fetchall()
        print('Список городов:')
        for row in rows:
            print(f'{row[0]} - {row[1]}')
    except sqlite3.Error as e:
        print(e)

def select_students_by_city(connection, city_id):
    sql = '''SELECT s.first_name, s.last_name,
co.title as 'country', c.title as 'city', c.area FROM students s
inner join cities c on s.city_id = c.id
inner join countries co on co.id = c.country_id WHERE c.id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (city_id,))

        rows = cursor.fetchall()
        print(f'\nУченики в выбранном городе под ID: {city_id}')
        for row in rows:
            print(f'студент: {row[0]} {row[1]}, страна: {row[2]}, '
                  f'город: {row[3]}, площадь города: {row[4]} км.кв')
    except sqlite3.Error as e:
        print(e)

my_connection = create_connection('hw.db')
if my_connection is not None:
    print('Successfully connected!')
    # create_table(my_connection, sql_to_create_countries_table)
    # insert_countries(my_connection, ("Кыргызстан",))
    # insert_countries(my_connection,("Казакстан",))
    # insert_countries(my_connection,("Россия",))
    # create_table(my_connection, sql_to_create_cities_table)
    # insert_cities(my_connection, ("Бишкек", 129, 1))
    # insert_cities(my_connection, ("Ош", 182, 1))
    # insert_cities(my_connection, ("Алмата", 682, 2))
    # insert_cities(my_connection, ("Астана", 722, 2))
    # insert_cities(my_connection, ("Москва", 2511, 3))
    # insert_cities(my_connection, ("Санк-Петербург", 1439, 3))
    # insert_cities(my_connection, ("Сочи", 176.8, 3))
    # create_table(my_connection, sql_to_create_students_table)
    # insert_students(my_connection, ("Мирбек", "Сапаров", 1))
    # insert_students(my_connection, ("Асан", "Асанов", 1))
    # insert_students(my_connection, ("Усон", "Усенов", 2))
    # insert_students(my_connection, ("Темир", "Темиров", 2))
    # insert_students(my_connection, ("Кайрат", "Кайратов", 3))
    # insert_students(my_connection, ("Нурбек", "Нуров", 3))
    # insert_students(my_connection, ("Эсен", "Эсенов", 4))
    # insert_students(my_connection, ("Тимур", "Кайратов", 4))
    # insert_students(my_connection, ("Кирилл", "Миронов", 5))
    # insert_students(my_connection, ("Владимир", "Перевалов", 5))
    # insert_students(my_connection, ("Елизавета", "Пшеничная", 6))
    # insert_students(my_connection, ("Елена", "Редькина", 6))
    # insert_students(my_connection, ("Андрей", "Савельев", 7))
    # insert_students(my_connection, ("Александр", "Самсанов", 7))
    # insert_students(my_connection, ("Анастасия", "Стасюк", 7))

    while True:
        print('\nВы можете отобразить список учеников по выбранному '
              'id города из перечня городов ниже, для выхода из программы '
              'введите 0:')
        select_show_cities(my_connection)
        city_id = input('Введите ID города: ')

        if city_id == '0':
            break
        try:
            city_id = int(city_id)
            select_students_by_city(my_connection, city_id)
        except ValueError:
            print("Ошибка: Введите корректный id города (целое число).")

    my_connection.close()