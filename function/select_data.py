import mysql.connector
import random

dictionnaire = {}


def create_dict(parrain, filleul):
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




# Fonction pour récupérer les noms de la table depuis MySQL
def recuperer_noms_table(nom_table):
    # Se connecter à la base de données MySQL
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hetec"
    )

    noms = []  # Tableau pour stocker les noms

    if db.is_connected():
        # Créer un curseur pour exécuter les requêtes SQL
        cursor = db.cursor()

        # Requête pour récupérer tous les noms de la table spécifiée
        select_query = f'''
        SELECT nom FROM {nom_table}
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

# Utilisation de la fonction pour récupérer les noms de la table
filleul = recuperer_noms_table('ida1')
parrain = recuperer_noms_table('id2')


create_dict(parrain, filleul)
# Afficher les noms récupérés
#print("Noms récupérés de la table :", filleul)
#print("-----------------")
#print("Noms récupérés de la table :", parrain)

print("Dictionnaire final :", dictionnaire)
print("--------")
print(filleul)
print("--------")
print(parrain)
print("--------")
