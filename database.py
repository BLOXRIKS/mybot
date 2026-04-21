import sqlite3

class Database:
    def __init__(self, db_name='clicker_bot.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            clicks INTEGER DEFAULT 0,
            upgrades INTEGER DEFAULT 0
        )''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            clicks INTEGER DEFAULT 0
        )''')

    def add_user(self, username):
        try:
            self.cursor.execute('INSERT INTO users (username) VALUES (?)', (username,))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print(f'User {username} already exists.')

    def record_click(self, username):
        self.cursor.execute('UPDATE users SET clicks = clicks + 1 WHERE username = ?', (username,))
        self.conn.commit()

    def upgrade_user(self, username):
        self.cursor.execute('UPDATE users SET upgrades = upgrades + 1 WHERE username = ?', (username,))
        self.conn.commit()

    def update_leaderboard(self):
        self.cursor.execute('DELETE FROM leaderboard')
        self.cursor.execute('''INSERT INTO leaderboard (username, clicks) 
            SELECT username, clicks FROM users 
            ORDER BY clicks DESC
            LIMIT 10''')
        self.conn.commit()

    def get_statistics(self, username):
        self.cursor.execute('SELECT clicks, upgrades FROM users WHERE username = ?', (username,))
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()

if __name__ == '__main__':
    db = Database()