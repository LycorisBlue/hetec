import mysql.connector

def convertir_en_nom_image(chaine):
    chaine = "pictures/" + chaine.replace(' ', '_')
    chaine += '.png'
    return chaine

# Fonction pour insérer des données dans une table MySQL
def inserer_donnees():
    # Se connecter à la base de données MySQL
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hetec"
    )

    if db.is_connected():
        # Demander le nom de la table dans laquelle insérer les données
        nom_table = input("Entrez le nom de la table : ")

        while True:
            if nom_table.lower() == 'exit':
                break

            valeurs = []

            # Demander chaque champ séparément
            nom = input("Entrez le nom : ")
            if nom.lower() == 'exit':
                break
            valeurs.append(nom)

            niveau = nom_table
            valeurs.append(niveau)

            img = convertir_en_nom_image(nom)
            valeurs.append(img)

            filleul = "false"
            valeurs.append(filleul)

            parrain = 0
            valeurs.append(parrain)

            # Créer un curseur pour exécuter les requêtes SQL
            cursor = db.cursor()

            # Requête pour insérer les données dans la table spécifiée
            insert_query = f'''
            INSERT INTO {nom_table} (nom, niveau, img, filleul, parrain)
            VALUES (%s, %s, %s, %s, %s)
            '''

            try:
                # Exécuter la requête pour insérer les données
                cursor.execute(insert_query, tuple(valeurs))
                db.commit()
                print("Données insérées avec succès.")
            except mysql.connector.Error as err:
                print(f"Erreur lors de l'insertion des données : {err}")
                db.rollback()
            finally:
                # Fermer le curseur
                cursor.close()

        # Fermer la connexion à la base de données
        db.close()

# Appel de la fonction pour insérer des données
inserer_donnees()
