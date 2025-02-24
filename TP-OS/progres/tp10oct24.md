## TP Système d'Exploitation du 10  octobre 2024

## Avec Monsieur GIRAULT

## 1- Manipulation des fichiers 

L'objectif de ce TP de s'initier aux commandes ligne, relatives à la manipulation et l'édition de fichiers.

1/ #Manipulation de fichiers

1.1 Vérifier le répertoire de travail courant initial par la commande _**pwd**_:/home/jonas

1.2 Lister les fichiers présents dans ce répertoire via la commande _**ls**_: README.md TP-OS ecolo.md kabylie

1.3 Tous les fichiers sont-ils visibles ? Comment les faire apparaître :

	 les fichiers ne sont pas tous visibles, pour les faire apparaitre, il faut utiliser la commande ls -la

1.4 Créer à l'aide des commandes mkdir et touch l'arborescence suivante : figure1
(touch permet notamment de créer un fichier vide) _* les commandes suivantes nous permettent de créer l'arborescence de la figure N°1 :

	mkdir -p exo1/{ete21/{mer,montagne},ete22,ete23,ete24} :création des dossiers 

	touch exo1/ete21/mer/foto{1,2}{.jpg,.txt} : création des fichiers du dossier mer

	touch exo1/ete21/montagne/foto3{.jpg,.txt} : création des fichiers du dossier montagne

	touch exo1/ete22/foto{4,5,6,7}{.jpg,.txt} : création des fichiers du dossier ete22

	touch exo1/ete23/foto{8,9}.jpg : création des fichiers du dossier ete23

	touch exo1/ete24/foto10.jpg : création du fichier du dossier ete24

1.5 Renommer le fichier foto10.jpg en foto20.jpg :

	 mv foto10.jpg foto20.jpg

1.6 Se placer dans le répertoire ete24 et déplacer les fichiers situés dans le répertoire montagne dans le répertoire mer :

	mv /home/jonas/TP-OS/exo1/ete21/montagne/ *  /home/jonas/TP-OS/exo1/ete21/mer

1.7 En utilisant uniquement des chemins absolus

1.8 En utilisant uniquement des chemins relatifs

1.9 Supprimer le répertoire montagne :

	 rm -r montagne/

1.10 Quelque que soit votre répertoire courant, proposer 2 commandes permettant de retourner au répertoire initial et appliquer. -> **cd**

1.11 Supprimer le répertoire ete23. Que constatez-vous ? : 

	rm -r ete23 

j'ai constaté que la suppression a été faite lorsque j'ai ajouté l'oprion **-r**

1.12 En vous aidant du man rm, proposer une commande supprimant un répertoire et toute l' arborescence qui en dépend (fichiers et sous-répertoires) -> **rm -r exo1** **_supprime aussi toute l'arborescence de la figure 1_**
Appliquer cette commande pour supprimer le répertoire ete23 et ses fichiers 

1.13 Que pensez-vous des risques associés à cette commande : 

	cette commande supprime tous les dossiers et leurs fichiers**, elle supprime la globalité des données

1.14 Renommer le répertoire ete22 en hiver22 :

	 mv ete22 hiver22

1.15 Copier le fichier foto20.jpg en foto20.txt dans le répertoire ete24 :

	 mv foto20.jpg foto20.txt

l. 16 Déplacer les fichiers sous mer dans le répertoire ete21 :

	 mv /home/jonas/TP-OS/exo1//ete21/mer/* /home/jonas/TP-OS/exo1/ete21/

1.17 Déplacer les fichiers foto3 sous hiver22 et les renommer foto33 :

	mv /home/jonas/TP-OS/exo1/ete21/montagne/* /home/jonas/TP-OS/exo1/hiver22_  

	mv foto3.jpg foto33.jpg

	mv foto3.txt foto33.txt

1.18 Liste en détail uniquement les fichiers ayant pour extension .txt du répertoire ete21 : 

	ls *.txt 


1.19 Déplacer l'ensemble des fichiers ayant pour extension .jpg du répertoire ete21 vers ete24 1.20 Supprimer les fichiers avec l'extension .txt du répertoire hiver22 :

	mv /home/jonas/TP-OS/exo1/ete21/*.jpg /home/jonas/TP-OS/exo1/ete24/

1.20 supprimer les fichiers avec l'extension .txt du répertoire hiver22 : se positionser dans le répertoire **hiver22** avant de taper la commande suivante :

	rm *.txt	

1.21 Proposer un diagramme de la nouvelle arborescence (dans un style semblable à la figure 1).	 

	mkdir -p stock/{stock1/{farine,ble},stock2/{mais,sarrasin},stock3,stock4,stock5}

1.22 A partir du man ls, trouver la(les) option(s) à ajouter à la commande ls afin d'obtenir la liste détaillée des fichiers du répertoire /usr/bin rangés dans Itordre de taille croissante avec une lecture aisée de la taille du fichier. L'usage de chaque option doit être justifiée.

	ls -lS --reverse --human-readable /usr/bin

 **ls : liste**

 **-l : afficharge de la liste détaillée des fichiers**

 **-S : Trie les fichiers par ordre décroissant**

 **--reverse : inverse l'ordre de tri décroissant de -S**

 **-h: affiche les fichiers dans un format lisible**

 **/usr/bin : le répertoire dans lequel la commande de recherche a été effectuée** 
	
# 2- Edition de fichiers

2.1 Créer un répertoire nommé exo2 et dans ce dossier, à l'aide de l'éditeur vi, créer 2 fichiers composés d'au moins 5 lignes contenant les informations suivantes :

Fichier 1 : pregen 

prénom de l'étudiant     genre (masculin, féminin, ) 

Fichier 2 : prenum 

prénom de l'étudiant     nombre entier (entre 1 et 1000) tous différents

2.2 Que proposez-vous pour optimiser la création de ces 2 fichiers ?

 _La commande_ **vi pregen prenum** _permet la création des deux fichiers en même temps_ 

2.3 Visualiser rapidement les fichiers générés par la commande cat : **c'est fait**

# 3 -Quelques opérations sur les fichiers texte

3.1 Afficher les 2 premières lignes du fichier pregen :

	head -n 2 pregen

3.2 Afficher depuis la ligne 3 jusqu'à la fin du fichier prenum

	 tail -n +3 prenum | head -n -0

3.3 En utilisant la commande wc compter le nombre de mots dans le fichier pregen puis compter le nombre de lignes du fichier prenum
	
Le nombre de mot dans le fichier pregen 	

	**wc -w pregen**

Le nombre de ligne du fichier prenum

	**wc -l prenum**

3.4 Afficher uniquement la colonne des nombres du fichier prenum

	cut -d ' ' -f 1 prenum

3.5 Afficher le fichier prenum en triant sur les nombres du plus grand au plus petit

	sort -k2 -r prenum

3.6 Réaliser un affichage synthétique des informations contenues dans les fichiers. Le résultat obtenu doit être de la forme : prénom nombre genre

	awk '{print $1, $2, $3}' prenum pregen

3.7 Que proposez-vous si l'on souhaite les champs dans l'ordre suivant : prénom genre nombre

	awk '{print $1, $3, $2}' pregen


# 4 -Divers

4.1 Afficher l'historique des commandes

	history

4.2 Proposer 2 façons de rejouer la dernière commande sort

 **1-la première façon c'est de retourner en arrière avec la flèche vers le haut**
 ** 2- avec la commande : !!**
