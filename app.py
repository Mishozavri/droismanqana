import sqlite3
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    phonenumber TEXT NOT NULL,
    address TEXT NOT NULL
)
''')
conn.commit()

def add_user(username, phonenumber, address):
    cursor.execute('INSERT INTO users (username, phonenumber, address) VALUES (?, ?, ?)',
                   (username, phonenumber, address))
    conn.commit()

def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()

def update_user(user_id, username, phonenumber, address):
    cursor.execute('''
        UPDATE users 
        SET username = ?, phonenumber = ?, address = ? 
        WHERE id = ?
    ''', (username, phonenumber, address, user_id))
    conn.commit()