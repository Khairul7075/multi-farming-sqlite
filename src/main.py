 """ main.py file is the entry point for interacting with your SQLite database. It typically handles:
Connecting to the database
Running queries (like seasonal plans or compatibility checks)
Displaying results in a readable format """ 

import sqlite3 
from db_manager import execute_query


DB_PATH = "database/multi_farming.db"

def connect_db():
    return sqlite3.connect(DB_PATH)

def show_compatible_farming():
    conn = connect_db()
    cursor = conn.cursor()
    query = """
    SELECT c.name_en, a.name_en, a.notes
    FROM Crops c
    JOIN Animals a ON c.crop_id = a.compatible_crop_id;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print("Compatible Crop-Animal Pairs:")
    for crop, animal, notes in results:
        print(f"- {crop} + {animal}: {notes}")
    conn.close()

def show_seasonal_plan():
    conn = connect_db()
    cursor = conn.cursor()
    query = """
    SELECT sa.season, f.location, c.name_en, a.name_en, sa.start_date, sa.end_date
    FROM SeasonalActivities sa
    JOIN Fields f ON sa.field_id = f.field_id
    JOIN Crops c ON sa.crop_id = c.crop_id
    JOIN Animals a ON sa.animal_id = a.animal_id
    ORDER BY sa.start_date;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print("\nSeasonal Farming Plan:")
    for season, location, crop, animal, start, end in results:
        print(f"- {season} at {location}: {crop} + {animal} ({start} to {end})")
    conn.close()

if __name__ == "__main__":
    show_compatible_farming()
    show_seasonal_plan()

# How to use main.py 

query = "SELECT name_en FROM Crops;"
results = execute_query(query)
for row in results:
    print(row[0])


