import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Создает подключение к SQLite базе данных"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Połączono z bazą: {db_file}, SQLite version: {sqlite3.version}")
        return conn   # <-- вот это главное изменение!
    except Error as e:
        print(e)
        return None


def create_connection_in_memory():
   """ create a database connection to a SQLite database """
   conn = None
   try:
       conn = sqlite3.connect(":memory:")
       print(f"Connected, sqlite version: {sqlite3.version}")
   except Error as e:
       print(e)
   finally:
       if conn:
           conn.close()
import sqlite3
from sqlite3 import Error
import sqlite3

import sqlite3

def add_task(conn, task):
    """
    Добавляет новую задачу в таблицу zadanie.
    :param conn: объект соединения с базой данных
    :param task: кортеж (project_id, nazwa, opis, status, start_date, end_date)
    """
    sql = '''INSERT INTO zadanie(project_id, nazwa, opis, status, start_date, end_date)
             VALUES(?, ?, ?, ?, ?, ?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, task)
        conn.commit()
        print(f"✅ Zadanie '{task[1]}' dodane pomyślnie (ID: {cursor.lastrowid})")
    except sqlite3.Error as e:
        print(f"❌ Błąd podczas dodawania zadania: {e}")


def create_connection(db_file):
    """ create a database connection to SQLite """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
    return None

def execute_sql(conn, sql):
    """ execute SQL script """
    try:
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
    except Error as e:
        print(e)
        
def execute_query(sql):
    """Execute SQL query using context manager"""
    import sqlite3
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

def main():
    database = "database.db"

    sql_create_projects_table = """
    CREATE TABLE IF NOT EXISTS projekt (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nazwa TEXT NOT NULL,
        start_date TEXT,
        end_date TEXT
    );
    """

    sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS zadanie (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER NOT NULL,
        nazwa TEXT NOT NULL,
        opis TEXT,
        status TEXT,
        start_date TEXT,
        end_date TEXT,
        FOREIGN KEY (project_id) REFERENCES projekt (id)
    );
    """

    conn = create_connection(database)
    if conn is not None:
        execute_sql(conn, sql_create_projects_table)
        execute_sql(conn, sql_create_tasks_table)
        print("Tables created successfully!")
        conn.close()
    else:
        print("Error! Cannot create database connection.")

if __name__ == "__main__":
    main()

if __name__ == '__main__':
   create_connection(r"database.db")
   create_connection_in_memory()