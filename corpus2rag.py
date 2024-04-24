import sqlite3

# Function to calculate Jaccard similarity
def jaccard_similarity(query, document):
    query = query.lower().split(" ")
    document = document.lower().split(" ")
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection) / len(union)

# Function to load documents from the SQLite database
def load_documents_from_db():
    conn = sqlite3.connect('pc_part_database.db')  # Connect to the database
    cursor = conn.cursor()
    cursor.execute("SELECT contenu FROM documents")  # Execute a query to retrieve the documents
    documents = [row[0] for row in cursor.fetchall()]  # Extract documents from query results
    conn.close()  # Close the database connection
    return documents

# Function to return the best response from the database based on Jaccard similarity
def return_response(query):
    corpus = load_documents_from_db()  # Load documents from the database
    similarities = []
    for doc in corpus:
        similarity = jaccard_similarity(query, doc)  # Calculate similarity for each document
        similarities.append(similarity)
    # Return the document with the highest similarity
    return corpus[similarities.index(max(similarities))]

# Example usage
#query = "describe a GPU"
#best_response = return_response(query)
#print(best_response)