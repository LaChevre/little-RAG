import sqlite3

def setup_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('pc_part_database.db')

    # Create a cursor object using the connection
    cursor = conn.cursor()

    # Enable foreign key constraint support in SQLite
    cursor.execute("PRAGMA foreign_keys = ON")

    # Create a new table to store PC component information
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            contenu TEXT NOT NULL,
            embedding TEXT
        )
    ''')

    # Create an index to optimize queries on the 'type' column
    cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_type ON documents (type)
    ''')

    # Commit the changes to the database
    conn.commit()

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Database setup complete.")
