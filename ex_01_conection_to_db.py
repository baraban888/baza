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