import sqlite3

def get_connection():
    return sqlite3.connect("dashboard/data/uboats.db", check_same_thread=False)