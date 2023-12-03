import random

parrain = [f"Parrain_{i}" for i in range(10)]
filleul = [f"filleul_{i}" for i in range(5)]


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

create_dict(parrain, filleul)

print("Dictionnaire final :", dictionnaire)
print("--------")
print(filleul)
print("--------")
print(parrain)
print("--------")


