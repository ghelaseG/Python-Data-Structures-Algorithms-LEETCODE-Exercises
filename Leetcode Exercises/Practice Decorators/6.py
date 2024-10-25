"""
Write a Python program that implements a decorator to retry a function multiple times in case of failure.
"""

import sqlite3
import time

def retry_on_failure(max_retries, delay = 1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Error occurred: {e}. Retrying ...")
                    time.sleep(delay)
            raise Exception("Maximum retries exceeded. Function failed.")
        
        return wrapper
    return decorator

@retry_on_failure(max_retries=3, delay=2)
def connect_to_sql():
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

try:
    data = connect_to_sql()
    print("Data retrieved successfully:", data)
except Exception as e:
    print(f"Failed to connect to database: {e}")
    