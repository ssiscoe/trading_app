import sqlite3

def setup_database():
    conn = sqlite3.connect("trading_app.db")
    cursor = conn.cursor()
    with open("db/schema.sql") as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()
    print("Database setup complete.")
