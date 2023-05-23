import random

#Ouverture du fichier en mode lecture
with open("mots_pendu.txt", 'r') as f:
    #Lire le contenu du fichier
    mots=f.read()
    #Transformation de la chaine de caractère lue ligne par ligne en une liste de mots
    mots=mots.split("\n")

# Fonction pour choisir un mot au hasard
def choisir_mot(mots):
    return random.choice(mots)
mot_aleatoire = choisir_mot(mots)
#print(mot_aleatoire)

longueur = len(mot_aleatoire)

nb_chances = 6
etat_actuel_mot = longueur * '_'
print(etat_actuel_mot)
while nb_chances > 0 and etat_actuel_mot.find('_') != -1:
    lettre_choisie = input('Choisir une lettre : ') # Ajouter une liste de lettres demandées pour pouvoir retourner 'déja demandée'
    L = mot_aleatoire.find(lettre_choisie)
    #Cas ou aucune lettre n'est choisie
    if lettre_choisie=='':
        print('Aucune lettre choisie')
    #Cas ou la lettre choisie n'est pas dans le mot
    elif lettre_choisie not in mot_aleatoire:
        print('Raté !')
        nb_chances -= 1
    #Cas ou la lettre choisie est dans le mot
    else:
        liste_indices=[indice for indice, lettre in enumerate(mot_aleatoire) if lettre == lettre_choisie]
        for i in liste_indices:
                    etat_actuel_mot = etat_actuel_mot[:i]+lettre_choisie+etat_actuel_mot[i+1:]
        print('Bien joué')
    print(f'Nombre d\'essais restants : {nb_chances}')
    print(etat_actuel_mot)

#Fin de partie

#Cas ou il ne reste aucune chance
if nb_chances == 0:
    print(f'Perdu, le mot était {mot_aleatoire}')
#Cas ou le mot a été trouvé entièrement
else:
    print('Gagné !')
