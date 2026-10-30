import sqlite3

def secure_login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Prepared statement - Prevents SQL Injection
    # Fixes Tom' OR '1'='1'-- payload
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    return result is not None