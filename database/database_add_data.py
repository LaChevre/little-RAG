import sqlite3
import json

# Chemin vers votre fichier JSON
chemin_json = 'database/data.json'

# Connexion à la base de données SQLite
conn = sqlite3.connect('pc_part_database.db')
cursor = conn.cursor()

# Création de la table si elle n'existe pas déjà
cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        contenu TEXT NOT NULL
    )
''')

# Ouvrir le fichier JSON et charger les données
with open(chemin_json, 'r', encoding='utf-8') as fichier:
    # Charger le fichier JSON comme une liste de dictionnaires
    documents = json.load(fichier)

    # Préparer les données pour l'insertion dans la base de données
    donnees_a_inserer = [(doc['type'], doc['contenu']) for doc in documents]

    # Insérer les données dans la table
    cursor.executemany('''
        INSERT INTO documents (type, contenu) VALUES (?, ?)
    ''', donnees_a_inserer)

    # Valider (commit) les changements
    conn.commit()

# Fermer la connexion à la base de données
conn.close()
