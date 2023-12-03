def infos_utilisateur():
    nom = "John Doe"  # Remplacez par le nom de l'utilisateur
    age = 30
    date_naissance = "01/01/1992"  # Remplacez par la date de naissance
    taille = 175.0
    poids = 70.0

    while True:
        print("Menu :")
        print("1. Nom de l'utilisateur")
        print("2. Âge et date de naissance")
        print("3. Taille")
        print("4. Poids")
        print("5. Annuler")

        choix = input("Entrez votre choix : ")

        if choix == '1':
            print(f"Nom de l'utilisateur : {nom}")
        elif choix == '2':
            print(f"Âge : {age}")
            print(f"Date de naissance : {date_naissance}")
        elif choix == '3':
            print(f"Taille : {taille} cm")
        elif choix == '4':
            print(f"Poids : {poids} kg")
        elif choix == '5':
            print("Vous avez choisi d'annuler.")
            break
        else:
            print("Choix invalide. Veuillez entrer un nombre de 1 à 5.")

infos_utilisateur()



def convertir_en_nom_image(chaine):
    chaine = "pictures/" + chaine.replace(' ', '_')
    chaine += '.png'
    return chaine

  # Affiche le résultat après la conversion


import random
chaine = "ida1-id2"

# Séparer la chaîne en deux variables
parties = chaine.split('-')

if len(parties) == 2:
    ida1, id2 = parties
    #print("Première partie :", ida1)
    #print("Deuxième partie :", id2)
else:
    print("La chaîne n'est pas au bon format.")



liste_plus_grande = [f"Nom_{i}" for i in range(20)]
liste_plus_petite = [f"Nom_{i}" for i in range(10)]

dictionnaire = {}

for cle in liste_plus_petite:
    if liste_plus_grande:
        valeur = random.choice(liste_plus_grande)
        dictionnaire[cle] = valeur
        liste_plus_grande.remove(valeur)

print("Dictionnaire final :", dictionnaire)
print("--------")
print(liste_plus_grande)


for cle in liste_plus_petite:
    if liste_plus_petite:
        valeur = random.choice(liste_plus_grande)
        dictionnaire[cle] = valeur
        liste_plus_grande.remove(valeur)
    else:
        break





def main():
    print("La fonction main() s'exécute.")
    answer = input("saisir un nom: ")
    nom_image = convertir_en_nom_image(answer)
    print(nom_image)

if __name__ == "__main__":
    main()
