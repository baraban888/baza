# Projekt: SQLite w praktyce

Projekt demonstruje wykorzystanie bazy danych **SQLite** w języku **Python** z użyciem modułu `sqlite3`.

## Opis

Aplikacja tworzy bazę danych `database.db` zawierającą dwie tabele:  
- **projekt** – przechowuje informacje o projektach (nazwa, daty rozpoczęcia i zakończenia),  
- **zadanie** – przechowuje zadania przypisane do projektów, powiązane relacją 1:N poprzez klucz obcy `project_id`.

## Funkcjonalność

- Nawiązywanie połączenia z bazą danych  
- Tworzenie struktury tabel  
- Dodawanie przykładowych rekordów  
- Zachowanie integralności relacji między tabelami

## Technologia

- **Python 3.x**  
- **SQLite 3**  
- Testy i weryfikacja: **DB Browser for SQLite**

## Wynik

Baza danych działa poprawnie. Zostały utworzone relacje 1:N między tabelami `projekt` i `zadanie`.  
Projekt stanowi praktyczne wdrożenie podstaw pracy z SQLite w środowisku Python.
