import sqlite3

def setup_database(db_path):
    """
    Creates the database schema if it doesn't exist.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check if the table already exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='trends';")
    if not cursor.fetchone():
        # If the table does not exist, execute the script
        with open("db/schema.sql", "r") as schema_file:
            cursor.executescript(schema_file.read())
    
    conn.commit()
    conn.close()
