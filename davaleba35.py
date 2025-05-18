import sqlite3

conn = sqlite3.connect('sports.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS footballers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        lastname TEXT NOT NULL,
        age INTEGER,
        country TEXT
    )
''')

footballers_data = [
    ('Lionel', 'Messi', 36, 'Argentina'),
    ('Cristiano', 'Ronaldo', 39, 'Portugal'),
    ('Kylian', 'Mbappe', 25, 'France'),
    ('Erling', 'Haaland', 24, 'Norway'),
    ('Luka', 'Modric', 38, 'Croatia')
]

cursor.executemany('''
    INSERT INTO footballers (name, lastname, age, country)
    VALUES (?, ?, ?, ?)
''', footballers_data)

cursor.execute('''
    UPDATE footballers
    SET age = 26
    WHERE name = 'Kylian' AND lastname = 'Mbappe'
''')

cursor.execute('''
    DELETE FROM footballers
    WHERE name = 'Kylian' AND lastname = 'Mbappe'
''')

cursor.execute('SELECT * FROM footballers')
remaining_footballers = cursor.fetchall()

print("OTHER FOOTBOLERS:")
for player in remaining_footballers:
    print(player)

conn.commit()
conn.close()