""" db_manager.py should act as a helper module to manage SQLite database operations—like connecting to the database, 
executing queries, and optionally fetching results. 
This keeps your main.py clean and modular. """ 

import sqlite3

DB_PATH = "database/multi_farming.db"

def connect_db():
    """Establish a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

def execute_query(query, params=None):
    """Execute a query and return results (for SELECT)."""
    conn = connect_db()
    if not conn:
        return []
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"Query execution error: {e}")
        return []
    finally:
        conn.close()

def execute_non_query(query, params=None):
    """Execute a query that doesn't return results (INSERT, UPDATE, DELETE)."""
    conn = connect_db()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Non-query execution error: {e}")
    finally:
        conn.close() 






