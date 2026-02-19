import sqlite3

class Database:
    def __init__(self, db_name='assistant.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS command_history (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                command TEXT NOT NULL,
                                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                            )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS preferences (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                preference_key TEXT UNIQUE,
                                preference_value TEXT
                            )''')
        self.connection.commit()

    def add_command(self, command):
        self.cursor.execute('INSERT INTO command_history (command) VALUES (?)', (command,))
        self.connection.commit()

    def get_command_history(self):
        self.cursor.execute('SELECT * FROM command_history ORDER BY timestamp DESC')
        return self.cursor.fetchall()

    def set_preference(self, key, value):
        try:
            self.cursor.execute('INSERT INTO preferences (preference_key, preference_value) VALUES (?, ?)', (key, value))
        except sqlite3.IntegrityError:
            self.cursor.execute('UPDATE preferences SET preference_value = ? WHERE preference_key = ?', (value, key))
        self.connection.commit()

    def get_preference(self, key):
        self.cursor.execute('SELECT preference_value FROM preferences WHERE preference_key = ?', (key,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def close(self):
        self.connection.close()