import mysql.connector

# Fonction pour créer une table dans MySQL
def creer_table():
    # Se connecter à la base de données MySQL
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hetec"
    )

    if db.is_connected():
        # Demander le nom de la table via un prompt
        nom_table = input("Entrez le nom de la table : ")

        # Créer un curseur pour exécuter les requêtes SQL
        cursor = db.cursor()

        # Requête pour créer la table avec les champs spécifiés
        create_table_query = f'''
        CREATE TABLE {nom_table} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            parrain VARCHAR(255),
            filleul VARCHAR(10),
            relation VARCHAR(255)
        )
        '''

        try:
            # Exécuter la requête pour créer la table
            cursor.execute(create_table_query)
            print(f"La table '{nom_table}' a été créée avec succès.")
        except mysql.connector.Error as err:
            print(f"Erreur lors de la création de la table : {err}")
        finally:
            # Fermer le curseur et la connexion à la base de données
            cursor.close()
            db.close()

# Appel de la fonction pour créer la table
creer_table()
