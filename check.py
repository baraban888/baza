from sqlalchemy import create_engine

engine = create_engine("sqlite:///climate.db")

with engine.connect() as conn:
    print("stations (5):")
    print(conn.execute("SELECT * FROM stations LIMIT 5").fetchall())
    print("\nmeasure (5):")
    print(conn.execute("SELECT * FROM measure LIMIT 5").fetchall())

    # при необходимости:
    # print(conn.execute("SELECT COUNT(*) FROM stations").fetchone())
    # print(conn.execute("SELECT COUNT(*) FROM measure").fetchone())
