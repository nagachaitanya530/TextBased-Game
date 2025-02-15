# database.py
import sqlite3

def create_table():
    conn = sqlite3.connect("game_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS calculations (
            id INTEGER PRIMARY KEY,
            expression TEXT,
            result TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_calculation(expression, result):
    create_table()
    conn = sqlite3.connect("game_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO calculations (expression, result) VALUES (?, ?)", (expression, str(result)))
    conn.commit()
    conn.close()

def get_calculation_history():
    create_table()
    conn = sqlite3.connect("game_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM calculations")
    history = cursor.fetchall()
    conn.close()
    return history

def display_calculation_history():
    history = get_calculation_history()
    if history:
        print("Calculation History:")
        for row in history:
            print(f"Expression: {row[1]}, Result: {row[2]}")
    else:
        print("No calculation history available.")
