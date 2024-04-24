import json
import sqlite3

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def connect_db(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def update_database(conn, data):
    cursor = conn.cursor()
    # Check if the table exists, create if not
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        contenu TEXT NOT NULL,
        embedding BLOB NOT NULL
    )''')

    # Updating records or inserting new ones
    for item in data:
        cursor.execute('''
        INSERT INTO documents (type, contenu, embedding) VALUES (?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
        type=excluded.type,
        contenu=excluded.contenu,
        embedding=excluded.embedding
        ''', (item['type'], item['contenu'], json.dumps(item['embedding'])))
    
    conn.commit()

def main():
    # Load data from JSON
    data = load_json('little-RAG/database/updated_data.json')
    
    # Connect to the SQLite database
    conn = connect_db('my_database.db')
    
    # Update the database with the new data
    update_database(conn, data)
    
    # Close the database connection
    conn.close()
    print("Database updated successfully.")

if __name__ == "__main__":
    main()
