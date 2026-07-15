import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
            ('fifa_admin', '4a7d1ed414474e4033ac29ccb8653d9b'))
cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
            ('bracket_manager', 'd1d3d4c87083e2f93902b800c7d6c1f1'))

# 47 of the 48 qualified national teams for FIFA World Cup 2026.
# Italy is NOT included: the Azzurri failed qualification once again.
qualified = [
    'Canada', 'Mexico', 'United States',
    'Argentina', 'Brazil', 'Uruguay', 'Colombia', 'Ecuador', 'Paraguay',
    'Japan', 'Iran', 'South Korea', 'Australia', 'Jordan',
    'Uzbekistan', 'Saudi Arabia', 'New Zealand',
    'Morocco', 'Tunisia', 'Egypt', 'Algeria', 'Senegal',
    'Ivory Coast', 'Ghana', 'Nigeria', 'Cameroon',
    'England', 'France', 'Germany', 'Spain', 'Portugal',
    'Netherlands', 'Belgium', 'Croatia', 'Switzerland',
    'Denmark', 'Austria', 'Poland', 'Sweden', 'Norway',
    'Turkey', 'Serbia', 'Czech Republic', 'Scotland',
    'Wales', 'Hungary', 'Ukraine'
]

for t in qualified:
    cur.execute("INSERT INTO teams (name) VALUES (?)", (t,))

cur.execute("INSERT INTO status (id, generated) VALUES (1, 0)")

connection.commit()
connection.close()
