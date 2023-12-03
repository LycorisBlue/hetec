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
