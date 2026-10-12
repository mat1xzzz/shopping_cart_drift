import sqlite3

def connect():
    database = sqlite3.connect("total_achievements.db")
    database.execute("PRAGMA foreign_keys = ON")
    return database

def add_achievements():
    database = connect()
    cursor = database.cursor()
    cursor.execute("INSERT INTO  (,) VALUES (?,?)", (, ))
    database.commit()
    clients_id = cursor.lastrowid
    database.close()
    return clients_id