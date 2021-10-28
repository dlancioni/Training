# https://www.sqlitetutorial.net/sqlite-python/
import os
import sqlite3
from sqlite3 import Error
os.system("cls")


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:

        # Get Connection
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)

        # Create table
        sql = """ create table if not exists tb_1 (id integer, name text) """
        cursor = conn.cursor()
        cursor.execute(sql)

        # Insert data
        sql = """ insert into tb_1 (id, name) values (1, 'David') """
        cursor = conn.cursor()
        cursor.execute(sql)
        print(cursor.lastrowid)

        # Select data
        cursor = conn.cursor()
        cursor.execute("SELECT id, name from tb_1 where id = ?", (1,))
        rows = cursor.fetchall()
        for row in rows:
            print(str(row[0]) + " " + row[1])
        
        # Cursor info
        print(cursor.description)


    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"C:\temp\data.db")