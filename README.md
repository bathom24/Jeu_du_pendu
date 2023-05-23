# Jeu_du_pendu

Les fichiers ci-joints permettent de jouer au jeu du pendu contre un programme informatique. 
Le dépôt contient :
-	Un script python permettant d’exécuter le jeu
-	Un fichier texte contenant une liste de mots dans laquelle le script choisira un mot de manière aléatoire
-	Le présent fichier texte décrivant le déroulement d’une partie et le fonctionnement du script

A l’exécution du script, le programme choisit un mot de manière aléatoire dans le fichier texte et la partie démarre. 
Déroulement de la partie 
Le programme affiche alors une liste de x tirets correspondant aux x lettres du mot à trouver et indique au joueur qu’il possède 6 essais. A chaque tour, il propose au joueur de choisir une lettre. Le joueur entre alors une lettre et appuie sur Entrée. 
-	Si la lettre fait partie du mot mystère, le programme renvoie l’état actuel du mot avec le(s) tiret(s) correspondant(s) remplacé(s) par la lettre trouvée, affiche ‘Bien joué’ ainsi que le nombre d’essais restant qui reste inchangé. 
-	Si la lettre ne fait pas partie du mot mystère ou si le joueur entre un caractère alphanumérique, le programme renvoie l’état actuel du mot toujours incomplet, affiche ‘Raté’ et le nombre d’essais restant auquel il a soustrait 1.
-	Si le joueur appuie sur Entrée sans avoir choisi de lettre, le programme lui indique ‘Aucune lettre choisie’ et renvoie le nombre d’essais restant inchangé et l’état actuel du mot inchangé. 

Fin de partie
Lorsque toutes les lettres ont été trouvées ou que le nombre d’essais restant est nul, la partie s’arrête. Dans le premier cas, le programme affiche ‘Gagné !’, dans le second cas, il affiche ‘Perdu, le mot était {Affichage du mot mystère}’. 
