import os
import sqlite3

# Hardcoded secret (Vulnerability)
API_KEY = "123456-SECRET-KEY"

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return cursor.fetchall()

def divide(a, b):
    # Bug: ZeroDivisionError possible
    return a / b

def unused_function():
    password = "admin123"  # Code smell + vulnerability
    return password
