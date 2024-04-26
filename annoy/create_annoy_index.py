import sqlite3
import json
from annoy import AnnoyIndex

def load_embeddings_from_db(db_path):
    """
    Load and deserialize embeddings from a SQLite database.
    Args:
    - db_path: Path to the SQLite database file.

    Returns:
    - List of embeddings (each as a list of floats).
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT embedding FROM documents")
    embeddings = [json.loads(row[0]) for row in cursor.fetchall()]
    conn.close()
    return embeddings

def create_annoy_index(embeddings, num_trees=10):
    """
    Create and build an ANNOY index from embeddings.
    Args:
    - embeddings: List of embeddings (each as a list of floats).
    - num_trees: Number of trees for ANNOY index.

    Returns:
    - AnnoyIndex object.
    """
    # Assuming all embeddings have the same dimension
    f = len(embeddings[0])
    t = AnnoyIndex(f, 'angular')  # Using angular distance
    for i, emb in enumerate(embeddings):
        t.add_item(i, emb)
    t.build(num_trees)
    return t

def main():
    db_path = 'pc_part_database.db'  # Path to your SQLite database
    index_path = 'pc_parts.ann'  # Path to save the ANNOY index

    # Load embeddings from the database
    embeddings = load_embeddings_from_db(db_path)
    
    # Create and build the ANNOY index
    t = create_annoy_index(embeddings, num_trees=10)
    
    # Save the index to disk
    t.save(index_path)
    print("ANNOY index created and saved successfully.")

if __name__ == "__main__":
    main()
