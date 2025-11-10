import sqlite3

# Настоящая база данных
db_file = "database.db"

# Файл с SQL-командами (test.db)
sql_file = "test.sql"

# Открываем файл и читаем SQL-код
with open(sql_file, "r", encoding="utf-8") as f:
    sql_script = f.read()

# Подключаемся к базе и выполняем SQL
with sqlite3.connect(db_file) as conn:
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()

print("✅ SQL-скрипт из test.db успешно выполнен и добавлен в database.db")
