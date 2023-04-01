"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import inspect
import sqlite3
from faker import Faker
from datetime import datetime

def main():
    global db_path
    db_path = os.path.join(get_script_dir(), 'social_network.db')
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE people (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            created_at TEXT,
            updated_at TEXT
        )
    ''')

    con.commit()
    con.close()

    return

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    fake = Faker()
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    for i in range(200):
        name = fake.name()
        age = fake.random_int(1,100)
        
        created_at = datetime.now().strftime('%Y-%m-%d')
        updated_at = datetime.now().strftime('%Y-%m-%d')

        cur.execute('''
            INSERT INTO people (name, 
                                age,  
                                created_at, 
                                updated_at)
                                VALUES (?, ?, ?, ?);
        ''', (name, age, created_at, updated_at))

    con.commit()
    con.close()
    return

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
   main()