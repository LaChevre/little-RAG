import sqlite3

def connect_db(db_file):
    """ Connect to the specified SQLite database. """
    conn = sqlite3.connect(db_file)
    return conn

def fetch_data(conn):
    """ Fetch and print all records from the database. """
    cursor = conn.cursor()
    cursor.execute("SELECT id, type, contenu, embedding FROM documents")
    rows = cursor.fetchall()
    print("ID | Type | Contenu | Embedding")
    print("-" * 50)
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2][:50]}... | {row[3][:30]}...")
    # Close cursor and connection
    cursor.close()

def main():
    # Database file path
    db_file = 'pc_part_database.db'
    # Connect to the database
    conn = connect_db(db_file)
    # Fetch and display data
    fetch_data(conn)
    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
