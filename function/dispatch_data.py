import mysql.connector

# Fonction pour insérer les données du dictionnaire dans la table
def inserer_raltion(dictionnaire, relation):
    # Se connecter à la base de données MySQL
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hetec"
    )

    if db.is_connected():
        # Créer un curseur pour exécuter les requêtes SQL
        cursor = db.cursor()

        # Requête pour insérer les données dans la table spécifiée
        insert_query = f'''
        INSERT INTO parainnage (parrain, filleul, {relation})
        VALUES (%s, %s, %s)
        '''

        try:
            # Parcourir le dictionnaire et insérer les données
            for parrain, filleul in dictionnaire.items():
                valeurs = (parrain, filleul, "relation_inconnue")  # Vous pouvez remplacer "relation_inconnue" par une valeur appropriée
                cursor.execute(insert_query, valeurs)

            db.commit()
            print("Données insérées avec succès.")
        except mysql.connector.Error as err:
            print(f"Erreur lors de l'insertion des données : {err}")
            db.rollback()
        finally:
            # Fermer le curseur et la connexion à la base de données
            cursor.close()
            db.close()

# Exemple d'utilisation de la fonction avec un dictionnaire
donnees = {
    "parrain1": "filleul1",
    "parrain2": "filleul2",
    "parrain3": "filleul3"
}

nom_table = "parainnage"  # Remplacez par le nom de votre table

# Appel de la fonction pour insérer les données
inserer_raltion(donnees, nom_table)
