# 📚 Mikrolib – Domowa Biblioteczka

Aplikacja webowa stworzona w oparciu o **Flask**, **SQLAlchemy**, **Flask-Migrate** oraz **SQLite**.  
Projekt jest rozwiniętą wersją zadania „Domowa biblioteczka” i umożliwia zarządzanie:

- książkami,
- autorami,
- wypożyczeniami (informacja, kto i kiedy wypożyczył książkę oraz kiedy ją zwrócono).

Struktura danych spełnia wymagania relacyjne:  
- książka może mieć wielu autorów,  
- autor może napisać wiele książek,  
- książka może być dostępna na półce lub wypożyczona.

## 🏗️ **Technologie**

- Python 3.12  
- Flask  
- Flask-SQLAlchemy  
- Flask-Migrate  
- SQLite  
- Jinja2 (szablony)

## 📁 **Struktura projektu**

# 📚 Mikrolib – Domowa Biblioteczka

Aplikacja webowa stworzona w oparciu o **Flask**, **SQLAlchemy**, **Flask-Migrate** oraz **SQLite**.  
Projekt jest rozwiniętą wersją zadania „Domowa biblioteczka” i umożliwia zarządzanie:

- książkami,
- autorami,
- wypożyczeniami (informacja, kto i kiedy wypożyczył książkę oraz kiedy ją zwrócono).

Struktura danych spełnia wymagania relacyjne:  
- książka może mieć wielu autorów,  
- autor może napisać wiele książek,  
- książka może być dostępna na półce lub wypożyczona.

## 🏗️ **Technologie**

- Python 3.12  
- Flask  
- Flask-SQLAlchemy  
- Flask-Migrate  
- SQLite  
- Jinja2 (szablony)

## 📁 **Struktura projektu**

mikrolib/
│
├── app/
│ ├── init.py
│ ├── models.py
│ └── routes/
│ ├── books.py
│ ├── authors.py
│ └── loans.py
│
├── migrations/ # Flask-Migrate – automatyczne migracje bazy danych
│
├── templates/
│ ├── books/
│ ├── authors/
│ └── loans/
│
├── config.py
├── mikrolib.py # punkt startowy aplikacji
└── README.md

## ✨ **Funkcje aplikacji**

### 📘 Książki
- lista książek  
- dodawanie nowej książki  
- informacja o tym, czy książka jest na półce  
- walidacja unikalnego numeru ISBN  
  - w przypadku błędu wyświetlany jest komunikat:  
    **„Książka z takim numerem ISBN już istnieje!”**
### 📖 Wypożyczenia
- lista wypożyczeń (aktywne zawsze wyświetlane na górze)  
- dodawanie wypożyczenia  
- wybór tylko książek dostępnych na półce  
- zapis:
  - kto wypożyczył  
  - kiedy wypożyczył  
  - do kiedy ma zwrócić  
  - kiedy zwrócono (jeśli null → wypożyczenie aktywne)

---

## ▶️ **Instrukcja uruchomienia lokalnie**

### 1) Sklonuj repozytorium

```bash
git clone https://github.com/baraban888/baza/tree/mikrolib
cd mikrolib
2) Stwórz i aktywuj wirtualne środowisko
Windows (PowerShell)
python -m venv venv
venv\Scripts\activate

Git Bash
python -m venv venv
source venv/Scripts/activate

3) Zainstaluj wymagania
pip install -r requirements.txt

4) Wykonaj migracje bazy danych
flask db upgrade

5) Uruchom aplikację
$env:FLASK_APP = "mikrolib.py"   # PowerShell
flask run


Lub w Git Bash:
export FLASK_APP=mikrolib.py
flask run
Aplikacja będzie dostępna pod adresem:
👉 http://127.0.0.1:5000
🧪 Testowanie

Wejdź na /books – lista książek
Dodaj książkę
Spróbuj dodać drugi raz ten sam ISBN – pojawi się komunikat błędu
Przejdź do autorów /authors
Przejdź do wypożyczeń /loans
📌 Uwagi końcowe
Projekt spełnia wszystkie wymagania zadania Kodilla:
relacje między tabelami,
formularze dodawania,
walidacje,
migracje,
czytelna struktura kodu,
wyraźne podziały na moduły,
zgodność z dobrymi praktykami.
👤 Autor

Projekt realizowany w ramach Bootcampu Kodilla – Python Developer.