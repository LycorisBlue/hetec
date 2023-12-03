from module import *


def main():
    nom = "John Doe"  # Remplacez par le nom de l'utilisateur
    age = 30
    date_naissance = "01/01/1992"  # Remplacez par la date de naissance
    taille = 175.0
    poids = 70.0
    print("============================================")


    while True:

        print("Menu :")
        print("1. Creation d'une table")
        print("2. Insertion des données")
        print("3. Attribution")
        print("4. Synchronisation")
        print("5. Annuler")

        choix = input("Entrez votre choix : ")

        if choix == '1':
            print("")
            creer_table()
            print("")
            print("============================================")
        elif choix == '2':
            print("")
            inserer_donnees()
            print("")
            print("============================================")
        elif choix == '3':
            print("")
            chaine = input("la relation: (ex: IDA1-IDA2): ")

            fillleul, parrain = separer_chaine(chaine)

            fillleul = recuperer_noms_table(fillleul, 1)
            parrain = recuperer_noms_table(parrain)


            create_dict(parrain, fillleul, chaine)
            synchronisation(chaine)
            print("============================================")
        elif choix == '4':
            print("")
            print("============================================")
        elif choix == '5':
            print("Vous avez choisi d'annuler.")
            break
        else:
            print("Choix invalide. Veuillez entrer un nombre de 1 à 5.")

if __name__ == "__main__":
    main()
