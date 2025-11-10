from db_utils import (
    get_conn, get_projects, get_all_tasks, get_tasks_by_project,
    add_task, update_task_status, update_task_dates, rename_task,
    delete_task, delete_tasks_by_project, delete_project
)

def pretty(rows, header):
    print("\n" + header)
    for r in rows:
        print(r)

if __name__ == "__main__":
    # ВАЖНО: перед запуском закрой DB Browser (или нажми «Zapisz zmiany» и «Zamknij bazę danych»),
    # чтобы не ловить 'database is locked'.
    conn = get_conn("database.db")

    # --- SELECT демо ---
    pretty(get_projects(conn), "Проекты:")

    # --- INSERT демо (добавим задачу в проект с id=1) ---
    new_task_id = add_task(conn, (
        1,
        "Zadanie demo",
        "Dodane przez main.py",
        "zaplanowano",
        "2025-11-13",
        "2025-11-16"
    ))
    print(f"\nДобавлена задача id={new_task_id}")

    # --- UPDATE демо ---
    update_task_status(conn, new_task_id, "w trakcie")
    update_task_dates(conn, new_task_id, "2025-11-14", "2025-11-17")
    rename_task(conn, new_task_id, "Zadanie demo (renamed)")

    # --- SELECT по проекту ---
    pretty(get_tasks_by_project(conn, 1), "Задачи проекта 1:")

    # --- DELETE демо (раскомментируй по необходимости) ---
    # delete_task(conn, new_task_id)
    # delete_tasks_by_project(conn, 1)
    # delete_project(conn, 1)

    conn.close()
    print("\nГотово.")
