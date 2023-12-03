import mysql.connector
import random






# Fonction pour se connecter à la base de données
def connecter_bdd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hetec"
    )

def create_dict(parrain, filleul, relation):
    dictionnaire = {}
    if len(parrain) < len(filleul):
        for cle in parrain:
            if parrain:
                valeur = random.choice(filleul)
                dictionnaire[cle] = valeur
                filleul.remove(valeur)
            else:
                break
    else:
        for cle in parrain:
            if filleul:
                valeur = random.choice(filleul)
                dictionnaire[cle] = valeur
                filleul.remove(valeur)
            else:
                break
    inserer_relation(dictionnaire, relation)
    dictionnaire = {}

def separer_chaine(chaine):
    parties = chaine.split('-')

    if len(parties) == 2:
        filleul, parrain = parties
        return filleul, parrain

def convertir_en_nom_image(chaine):
    chaine = "pictures/" + chaine.replace(' ', '_')
    chaine += '.png'
    return chaine


"""
    Fonction pour créer une table dans MySQL
"""

def creer_table():
    # Se connecter à la base de données MySQL
    db = connecter_bdd()

    if db.is_connected():
        # Demander le nom de la table via un prompt
        nom_table = input("Entrez le nom de la table : ")

        # Créer un curseur pour exécuter les requêtes SQL
        cursor = db.cursor()

        # Requête pour créer la table avec les champs spécifiés
        create_table_query = f'''
        CREATE TABLE {nom_table} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(255),
            niveau VARCHAR(10),
            img VARCHAR(255),
            filleul VARCHAR(6),
            parrain INT
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



"""
    Fonction pour insérer des données dans une table MySQL
"""

def inserer_donnees():
    # Se connecter à la base de données MySQL
    db = connecter_bdd()

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


def recuperer_noms_table(nom_table, c=0):
    # Se connecter à la base de données MySQL
    db = connecter_bdd()

    noms = []  # Tableau pour stocker les noms

    if db.is_connected():
        # Créer un curseur pour exécuter les requêtes SQL
        cursor = db.cursor()

        # Requête pour récupérer tous les noms de la table spécifiée
        if c == 0:
            select_query = f'''
            SELECT nom FROM {nom_table}
            '''
        else:
            select_query = f'''
            SELECT nom FROM {nom_table} WHERE filleul = "false"
            '''

        try:
            # Exécuter la requête pour récupérer les noms
            cursor.execute(select_query)
            resultats = cursor.fetchall()

            # Ajouter les noms au tableau
            for resultat in resultats:
                noms.append(resultat[0])

        except mysql.connector.Error as err:
            print(f"Erreur lors de la récupération des noms : {err}")
        finally:
            # Fermer le curseur et la connexion à la base de données
            cursor.close()
            db.close()

    return noms


def inserer_relation(dictionnaire, relation):
    # Se connecter à la base de données MySQL
    db = connecter_bdd()

    if db.is_connected():
        # Créer un curseur pour exécuter les requêtes SQL
        cursor = db.cursor()

        # Requête pour insérer les données dans la table spécifiée
        insert_query = f'''
        INSERT INTO parainnage (parrain, filleul, relation)
        VALUES (%s, %s, %s)
        '''

        try:
            # Parcourir le dictionnaire et insérer les données
            for parrain, filleul in dictionnaire.items():
                valeurs = (parrain, filleul, relation)  # Vous pouvez remplacer "relation_inconnue" par une valeur appropriée
                cursor.execute(insert_query, valeurs)

            db.commit()
            print("Données insérées avec succès.")
            print(dictionnaire)
        except mysql.connector.Error as err:
            print(f"Erreur lors de l'insertion des données : {err}")
            db.rollback()
        finally:
            # Fermer le curseur et la connexion à la base de données
            cursor.close()
            db.close()


def synchronisation(relation):
    filleuls = []
    parrains = []
    print(relation)

    # Se connecter à la base de données MySQL
    db = connecter_bdd()

    if db.is_connected():
        # Créer un curseur pour exécuter les requêtes SQL
        cursor = db.cursor()

        # Requête pour récupérer les noms et prénoms depuis une relation
        select_query = f'''
        SELECT filleul, parrain FROM parainnage WHERE relation = '{relation}'
        '''

        try:
            # Exécuter la requête pour récupérer les données
            cursor.execute(select_query)
            resultats = cursor.fetchall()

            # Ajouter les noms et prénoms aux tableaux
            for resultat in resultats:
                filleuls.append(resultat[0])
                parrains.append(resultat[1])

            mettre_a_jour_statut(filleuls, parrains, relation)
            print(f"Synchronisation réussi de la relation {relation}")

        except mysql.connector.Error as err:
            print(f"Erreur lors de la récupération des données : {err}")
        finally:
            # Fermer le curseur et la connexion à la base de données
            cursor.close()
            db.close()




def mettre_a_jour_statut(filleul, parrain, relation):
    f, p = separer_chaine(relation)
    # Se connecter à la base de données MySQL
    db = connecter_bdd()

    if db.is_connected():
        # Créer un curseur pour exécuter les requêtes SQL
        cursor = db.cursor()

        # Mettre à jour le statut pour chaque nom dans la liste
        if len(parrain) > 0:
            for nom in parrain:
                try:
                    # Requête pour mettre à jour le statut en ajoutant +1
                    update_query = f'''
                    UPDATE {p}
                    SET parrain = parrain + 1
                    WHERE nom = '{nom}'
                    '''

                    # Exécuter la requête de mise à jour
                    cursor.execute(update_query)
                    db.commit()
                    print(f"Statut mis à jour pour {nom}")
                except mysql.connector.Error as err:
                    print(f"Erreur lors de la mise à jour du statut pour {nom} : {err}")
                    db.rollback()
        for nom in filleul:
                try:
                    # Requête pour mettre à jour le statut en ajoutant +1
                    update_query = f'''
                    UPDATE {f}
                    SET filleul = "true"
                    WHERE nom = '{nom}'
                    '''

                    # Exécuter la requête de mise à jour
                    cursor.execute(update_query)
                    db.commit()
                    print(f"Statut mis à jour pour {nom}")
                except mysql.connector.Error as err:
                    print(f"Erreur lors de la mise à jour du statut pour {nom} : {err}")
                    db.rollback()


        # Fermer le curseur et la connexion à la base de données
        cursor.close()
        db.close()
