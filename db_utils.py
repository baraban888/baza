import sqlite3
from typing import Iterable, Tuple, List, Optional, Any

DB_PATH = "database.db"

def get_conn(db_path: str = DB_PATH) -> sqlite3.Connection:
    """Open SQLite connection with foreign keys enabled."""
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

# ---------- SELECT ----------
def get_projects(conn: sqlite3.Connection) -> List[Tuple[Any, ...]]:
    sql = "SELECT id, nazwa, start_date, end_date FROM projekt ORDER BY id;"
    return conn.execute(sql).fetchall()

def get_all_tasks(conn: sqlite3.Connection) -> List[Tuple[Any, ...]]:
    sql = """
    SELECT z.id, z.project_id, z.nazwa, z.opis, z.status, z.start_date, z.end_date,
           p.nazwa AS project_name
    FROM zadanie z
    JOIN projekt p ON p.id = z.project_id
    ORDER BY z.id;
    """
    return conn.execute(sql).fetchall()

def get_tasks_by_project(conn: sqlite3.Connection, project_id: int) -> List[Tuple[Any, ...]]:
    sql = """
    SELECT id, nazwa, opis, status, start_date, end_date
    FROM zadanie
    WHERE project_id = ?
    ORDER BY id;
    """
    return conn.execute(sql, (project_id,)).fetchall()

# ---------- INSERT ----------
def add_task(conn: sqlite3.Connection,
             task: Tuple[int, str, Optional[str], Optional[str], Optional[str], Optional[str]]
             ) -> int:
    """
    task = (project_id, nazwa, opis, status, start_date, end_date)
    Returns: new task id
    """
    sql = """
    INSERT INTO zadanie(project_id, nazwa, opis, status, start_date, end_date)
    VALUES(?, ?, ?, ?, ?, ?)
    """
    cur = conn.execute(sql, task)
    conn.commit()
    return cur.lastrowid

# ---------- UPDATE ----------
def update_task_status(conn: sqlite3.Connection, task_id: int, new_status: str) -> int:
    sql = "UPDATE zadanie SET status = ? WHERE id = ?"
    cur = conn.execute(sql, (new_status, task_id))
    conn.commit()
    return cur.rowcount

def update_task_dates(conn: sqlite3.Connection, task_id: int,
                      start_date: str, end_date: str) -> int:
    sql = "UPDATE zadanie SET start_date = ?, end_date = ? WHERE id = ?"
    cur = conn.execute(sql, (start_date, end_date, task_id))
    conn.commit()
    return cur.rowcount

def rename_task(conn: sqlite3.Connection, task_id: int, new_name: str) -> int:
    sql = "UPDATE zadanie SET nazwa = ? WHERE id = ?"
    cur = conn.execute(sql, (new_name, task_id))
    conn.commit()
    return cur.rowcount

# ---------- DELETE ----------
def delete_task(conn: sqlite3.Connection, task_id: int) -> int:
    cur = conn.execute("DELETE FROM zadanie WHERE id = ?", (task_id,))
    conn.commit()
    return cur.rowcount

def delete_tasks_by_project(conn: sqlite3.Connection, project_id: int) -> int:
    cur = conn.execute("DELETE FROM zadanie WHERE project_id = ?", (project_id,))
    conn.commit()
    return cur.rowcount

def delete_project(conn: sqlite3.Connection, project_id: int) -> int:
    """
    Если в схеме НЕТ ON DELETE CASCADE, сначала удаляем задачи.
    """
    delete_tasks_by_project(conn, project_id)  # безопасно
    cur = conn.execute("DELETE FROM projekt WHERE id = ?", (project_id,))
    conn.commit()
    return cur.rowcount
