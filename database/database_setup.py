import sqlite3

# Connectez-vous à la base de données SQLite
conn = sqlite3.connect('pc_part_database.db')

# Créer un objet cursor pour exécuter des commandes SQL
cursor = conn.cursor()

# Activer le support du JSON dans SQLite
cursor.execute("PRAGMA foreign_keys = ON")

# Créer une nouvelle table pour stocker les informations sur les composants de PC
cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY,
        type TEXT NOT NULL,  
        contenu TEXT NOT NULL
    )
''')

# Créer un index pour optimiser les requêtes sur la colonne 'type'
cursor.execute('''
    CREATE INDEX IF NOT EXISTS idx_type ON documents (type)
''')

# Commit (appliquer) les changements
conn.commit()

# Fermer la connexion à la base de données
conn.close()
