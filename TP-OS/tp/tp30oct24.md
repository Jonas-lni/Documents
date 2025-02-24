# TP Système d'Exploitation du 30 octobre 2024

## Avec Monsieur GIRAULT

## Prérequis: Machine sous Linux, Shell Bash 

## 1/ Grep, Find, Pipe, Redirection

Ecrire les commandes permettant de :

**1.1 Compter le nombre de ligne contenant "bin" dans le fichier /etc/passwd :**

	cat /etc/passwd | grep bin | wc -l   
ou

	cat /etc/passwd | grep bin -c

**1.2 Compter le nombre d'occurence de "bin" dans le fichier passwd :** 
	
	cat /etc/passwd|grep bin -o|wc -l

**1.3 Afficher les lignes contenant le mot "bin" et pas "sbin"**

	cat /etc/passwd|grep bin| grep -v sbin

ou

	grep bin /etc/passwd |grep -v sbin

**1.4 Création d'un fichier nommé nologin.txt contenant uniquement les lignes ne contenant pas "nologin"**

	cat /etc/passwd | grep -v nologin > nologin.txt

**1.5 Afficher le numéro des 4 premières lignes ne contenant pas "nologin"**

	
	cat /etc/passwd |grep -vn nologin|head -4

ou 

	grep -vn "nologin" /etc/passwd|head -4

**1.6 Trouver tous les fichiers de l'arborescence /etc contenant mon nom de login ecrit indifféremment en majuscule ou miniscule**

	grep -r jonas *

et 
	sudo grep -r jonas *

**1.7 Recherche des fichiers de l'arborescence /etc/ contenant dans leur nom l'expression "tab" et ecrire le résultat dans le fichiers filtabl.txt**

	find /etc -name "*tab*" > filtab.txt


**1.8 Affichage de Yes si le fichier /etc/passwd contient le terme login et No si ce n'est pas le cas :**
		
	grep -q "login" /etc/passwd && echo "Yes" || echo "No"

ou

	cat /etc/passwd|grep -q "login" && echo "Yes" || echo "No"

**1.9 Le résultat était "No" lorsque j'ai tapé la commande:**

	grep -q "login" /etc/password && echo "Yes" || echo "No"

**1.10 pour éviter les message complémentaire nous pouvons rediriger vers /dev/null**

_**exemple:**_

	grep -q "login" /etc/password && echo "Yes" || echo "No"> /dev/null

## 2/ Tubes nommés

	#!/bin/bash
	mkfifo ~/testing/tube0 2>/dev/null
	mkfifo ~/testing/tube1 2>/dev/null
	mkfifo ~/testing/tube2 2>/dev/null
	fot i in {1..20}
	do
	   tirage=${RANDOM}
	   choix_tube=`expr $tirage % 3`
	   echo -e "iteration=$i \t tirage=$tirage \t prochain tube=$choix_tube"
	   echo -n $tirage", " > ~/testing/tube$choix_tube
	   sleep 0.3
	done


**2.1 Explication des ligne en gras**

	mkfifo ~/testing/tube0 2>/dev/null


-> est la création d'un tube nommé **tube0** dans le dossier **testing** qui se trouve dans ~/ **home**. **2>** est la redirection des messages d'erreur vers **/dev/null** pour que les données d'erreur soient ignorées 

	choix_tube=`expr $tirage % 3`

->**choix_tube=** est l'attribution d'une valeur à une variable nommée **choix_tube** . **expr** est utilisée pour manipuler des chaines de caractères, dans ce cas, elle est utilisée pour faire une division modulaire avec le **%** et **$tirage** la valeur de la variable tirage . **%3** c'est pour renvoyer le reste de la division 

	echo -n $tirage", " > ~/testing/tube$choix_tube

-> Elle écrit dans un fichier qui a un nom en fonction de la variable choix_tube. le résultat est une valeur suivi d'une virgule


**2.2 Le fonctionnement du script** est la création de trois tubes 

**3.2 La commande cat ~/testing/tube N° nous permet de lire et d'observer le tube**


## 3/ Alias et configuration Bash 

**3.1 Proposition d'un alias permettant de lister les fichiers d'un répertoire sans la couleur mais en suffixant les répértoires par le caractére / pour les identifier**

	alias lsnocolor='ls --classify --color=never'

**3.2 Proposition d'un alias ayant pour nom ptxt qui retourne la chaine "X fichiers txt présent" ou le nombre X représente la quantité de fichiers avec l'extension .txt présents dans le répertoire courant duquel la commande est lancée, rien sinon** **_elle est un peu difficile pour moi_**

**3.3 Proposition d'une méthode pour que ces alias soient persistants après un reboot**

Pour rendre les alias persistants après une résolution, il faut les enregistrer dans le fichier de configuration du shell que vous utilisez (par exemple, .bashrcou .zshrcselon votre shell). Voici comment procéder

## 4/ Utilisateurs

**4.1 Création des utilisateurs Albert Einstein et Niels Bohr ayant pour nom de login respectifs einstein et bohr** **_avec le surdoer :_**

	adduser einstein

	adduser bohr

**4.2 Initialisation des mots de passe à albert pour einstein et niels pour bohr**

	mot de passe albert pour einstein

	mot de passe niels pour bohs

**4.3 Création de groupe nommmé physiciens**

	addgroup physiciens

**4.4 Ajout d'einstein et de bohr dans le groupe**

	sudo usermod -aG physiciens bohr
	
	sudo usermod -aG physiciens einstein

**4.5 Connection comme einstein grâce à la commande su - einstein dans un nouveau terminal**

	su - einstein
	
**4.6 Vérificationdes de mes identifiants en tant qu'einstein**

	whoami -> einstein 

	groups -> einstein users physiciens

	id einstein -> uid=1002(einstein) gid=1002(einstein) groups=1002(einstein),100(users),1004(physiciens)


**4.7 Changement du mot de passe d'einstein**

	sudo passwd einstein

_**ça ne marche pas parcequ'einstein n'est pas un administrateur**_

**4.8 Si Bohr est absent plusieurs semaines, dans le cadre de la sécurité je propose le verouillage du compte bohr dans le compte administrateur**

	sudo usermod -L bohr

 **_cela est possible grâce au surdoer_**

pour déverrouiller le compte lorsque l'utilisateur revient, on utilise la commande suivante :

	sudo usermod -U bohr

**4.8 Réinitialisation du mot de passe de bohr à la valeur henrik**

	passwd 

	Retype new password: 
	passwd: password updated successfull

**4.9 Se connecter dans un nouveau terminal comme bohr** -> **C'est fait** 

**4.10 Création d'un fichier dans le homedir**

**bohr n'a pas réussi à créer un fichier dans le homedir parcequ'il n'avait pas les droits pour le faire, dans admin je lui donne le droit avec la commande suivante depuis le root**

	usermod -aG sudo bohr

_le problème c'est qu'il a des droits de root_ _J'ai enlevé les droits de root dans sudo visudo_

	 touch /home/bohr/bohr.txt

**4.11 Changement de groupe pour aller dans le groupe physiciens**

	sudo -i
	
	grep physiciens /etc/group

Vérification de l'existence du groupe physiciens

	sudo usermod -aG physiciens bohr

Cette commande ajoute bohr dans le groupe Physiciens

**4.12 Création d'un nouveau fichier dans le homedir**

	touch /home/bohr/bonhr1.txt


**4.13 réalisation d'un listing détaillé des 2 fichiers crées**

	ls -l

	ls -l /home/bohr/bohr.txt /home/bohr/bohr1.txt
