import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connected to database.")
        return conn
    except Error as e:
        print(e)
    return None

def insert_project(conn, project):
    sql = ''' INSERT INTO projekt(nazwa, start_date, end_date)
              VALUES(?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def insert_task(conn, task):
    sql = ''' INSERT INTO zadanie(project_id, nazwa, opis, status, start_date, end_date)
              VALUES(?, ?, ?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

def main():
    database = "database.db"

    conn = create_connection(database)
    with conn:
        # добавляем проект
        project = ('Projekt BuildTracker', '2025-11-02', '2026-01-15')
        project_id = insert_project(conn, project)

        # добавляем задания
        task1 = (project_id, 'Створити базу даних', 'Структура таблиць', 'в процесі', '2025-11-03', '2025-11-05')
        task2 = (project_id, 'Розробити фронтенд', 'React-інтерфейс', 'заплановано', '2025-11-06', '2025-11-10')

        insert_task(conn, task1)
        insert_task(conn, task2)

        print("✅ Дані успішно додані!")

if __name__ == '__main__':
    main()
