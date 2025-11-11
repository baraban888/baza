import pandas as pd
from sqlalchemy import create_engine, text

DB_PATH = "sqlite:///climate.db"

def load_csv_to_db():
    engine = create_engine(DB_PATH)

    # читаем CSV
    stations = pd.read_csv("clean_stations.csv", encoding="utf-8")
    measure  = pd.read_csv("clean_measure.csv",  encoding="utf-8")

    # пишем в БД (без явного begin; pandas сам откроет/закроет транзакцию)
    stations.to_sql("stations", con=engine, index=False, if_exists="replace")
    measure.to_sql("measure",  con=engine, index=False, if_exists="replace")

    # быстрая проверка
    with engine.connect() as conn:
        n1 = conn.execute(text("SELECT COUNT(*) FROM stations")).scalar()
        n2 = conn.execute(text("SELECT COUNT(*) FROM measure")).scalar()
        print(f"✅ CSV загружены: stations={n1}, measure={n2}")

if __name__ == "__main__":
    load_csv_to_db()

