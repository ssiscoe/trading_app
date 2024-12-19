import sqlite3
import pandas as pd
import os

def load_trades(database_path=None):
    if database_path is None:
        # Construct path relative to project root
        database_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 
                                   'database', 'trading.db')
    
    conn = sqlite3.connect(database_path)
    df = pd.read_sql_query("SELECT * FROM trades", conn)
    conn.close()
    return df

if __name__ == "__main__":
    df = load_trades()
    print(df)