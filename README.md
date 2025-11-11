# Projekt: Baza danych z CSV → SQLite (Kodilla)

## Uruchomienie
```bash
# (opcjonalnie) utwórz wirtualne środowisko
# py -m venv .venv && .venv\Scripts\activate  # Windows
# python3 -m venv .venv && source .venv/bin/activate  # Linux/Mac

pip install -r requirements.txt

# Umieść pliki: clean_stations.csv, clean_measure.csv w katalogu projektu
python main.py     # ładuje CSV do climate.db
python check.py    # szybka weryfikacja SELECT * LIMIT 5
Wymagania: SQLAlchemy==1.3.16, pandas.
Autor rozwiązania: Alex Bahatiuk (wdrożenie lokalne)
Wsparcie asystenta: ChatGPT (AI)