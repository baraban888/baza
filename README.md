# Projekt: Baza danych SQLite – Zadanie Kodilla

Ten projekt został przygotowany w ramach modułu **"Połączenie z bazą danych w Pythonie"** (Kodilla Bootcamp).  
Zadaniem było utworzenie bazy danych SQLite oraz napisanie funkcji, które wykonują operacje CRUD  
(Create, Read, Update, Delete) dla tabel **projekt** i **zadanie**.

---

## 🔹 Struktura bazy danych

Baza danych: `database.db`  
Zawiera dwie tabele:

### Tabela `projekt`
| Kolumna     | Typ   | Opis                      |
|--------------|-------|---------------------------|
| id           | INTEGER PRIMARY KEY AUTOINCREMENT | Identyfikator projektu |
| nazwa        | TEXT  | Nazwa projektu            |
| start_date   | TEXT  | Data rozpoczęcia          |
| end_date     | TEXT  | Data zakończenia          |

### Tabela `zadanie`
| Kolumna     | Typ   | Opis                        |
|--------------|-------|-----------------------------|
| id           | INTEGER PRIMARY KEY AUTOINCREMENT   | Identyfikator zadania  |
| project_id   | INTEGER                            | Klucz obcy do projektu |
| nazwa        | TEXT                               | Nazwa zadania          |
| opis         | TEXT                               | Opis zadania           |
| status       | TEXT                               | Status (np. w trakcie) |
| start_date   | TEXT                               | Data rozpoczęcia       |
| end_date     | TEXT                               | Data zakończenia       |

---

## 🔹 Pliki projektu

- `db_utils.py` – funkcje do połączenia z bazą danych oraz operacji CRUD  
- `main.py` – przykładowe użycie funkcji (dodawanie, aktualizacja, usuwanie danych)  
- `test.sql` – skrypt SQL do dodania nowego zadania przez plik  
- `run_sql_from_file.py` – uruchamianie komend SQL z pliku  
- `database.db` – właściwa baza danych SQLite  

---

## 🔹 Zakres funkcjonalności

✅ Dodawanie nowego projektu lub zadania  
✅ Pobieranie danych (SELECT) według projektu  
✅ Aktualizacja statusu lub daty zadania  
✅ Usuwanie pojedynczego zadania lub projektu  
✅ Obsługa kluczy obcych (PRAGMA foreign_keys = ON)

---

## 🔹 Uruchomienie

1. Upewnij się, że masz zainstalowanego **Python 3**.  
2. Uruchom w terminalu:
   ```bash
   python main.py

🔹 Autor
## Autor
Projekt zrealizowany przez: **ChatGPT (asystent AI)**
Wsparcie / wdrożenie lokalne: **Alex Bahatiuk**
Nowa Sól, Polska
Bootcamp Kodilla – Moduł 13