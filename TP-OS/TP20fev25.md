# TP GESTION DES PROCESSUS SOUS LINUX

## voir l'ensemble des commande suivantes :
xclock
 1887  xclock&
 1888  job

 1889  ip a

 1890  clear

 1891  exit

 1892  clear

 1893  ping 192.168.150.13

 1894  bg

 1895  ls

 1896  kilfg

 1897  ++

 1898  fg

 1899  echo$!

 1900  echo $!

 1901  echo $$

 1902  history

 1903  clear

 1904  bg

 1905  fg

 1906  bg

 1907  sleep

 1908  ps

 1909  bg

 1910  sleep

 1911  jobs

 1912  top

 1913  clear

 1914  bg

 1915  &

 1916  &bg

 1917  & bg

 1918  bg

 1919  sleep &

 1920  sleep

 1921  bg

 1922  sleep &

 1923  job

 1924  bobs

 1925  jobs

 1926  clear

 1927  sleep 10 &

 1928  bg

 1929  sleep 10 &

 1930  echo "Processus en arrière-plan avec PID: $!"

 1931  bg

 1932  jobs

 1933  sleep 10 &

 1934  jobs

 1935  fg &%

 1936  fg 1%

 1937  &

 1938  sleep &

 1939  bg

 1940  fg

 1941  clear

 1942  sleep 20 &

 1943  sleep &

 1944  sleep --help

 1945  jobs

 1946  bg
 1947  sleep --help

 1948  clear

 1949  ps

 1950  wc -l/tmp/psresult

 1951  wc -l /tmp/psresult

 1952  clear

 1953  sleep 10&

 1954  sleep 30&

 1955  bg

 1956  kill 1

 1957  bg

 1958  sleep 30&

 1959  fg

 1960  bg

 1961  sleep 30&

 1962  bg

 1963  fg

 1964  clear

 1965  sleep 10 &

 1966  echo "Processus en arrière-plan avec PID: $!"

 1967  echo $!

 1968  sleep 10 & && echo "Processus en arrière plan avec Pid: $!"

 1969  sleep 10 & && echo "Processus en arrière plan avec PID: $!"

 1970  sleep 10 & & echo "Processus en arrière plan avec PID: $!"

 1971  sleep 10 &  echo "Processus en arrière plan avec PID: $!"

 1972  sleep 10 &  echo "Processus en arrière plan avec PId: $!"

 1973  kill 9352

 1974  bg

 1975  sleep 10 &  echo "Processus en arrière plan avec PId: $!"

 1976  kill 9391

 1977  ps aux | grep bash

 1978  ps - C bash

 1979  ps -C bash

 1980  ps -p 3299 -0 pid,ppid,cmd

 1981  ps -p 3299 -0 pid

 1982  clear

 1983  jobs

 1984  sleep &10

 1985  jobs

 1986  sleep 10&

 1987  jobs

 1988  fg %1

 1989  kill 9573

 1990  kill 9596

 1991  kill $!

 1992  cd

 1993  exit

 1994  history

root@EECS18:~# 

comment arreter un script qui tourne en arrière fond sur ubuntu
ChatGPT a dit :

Il existe plusieurs méthodes pour arrêter un script qui tourne en arrière-plan sur Ubuntu. Voici les solutions :
🔹 1️⃣ Trouver le Processus et l’Arrêter avec kill

Si tu as lancé un script en arrière-plan (avec &), utilise ps pour le retrouver et kill pour l’arrêter.
📌 Étape 1 : Trouver le PID du processus

Utilise cette commande pour lister les processus liés à ton script :

ps aux | grep nom_du_script

Exemple :

ps aux | grep mon_script.sh

Cela te donnera une ligne avec un PID (Process ID), par exemple :

user    12345  0.0  0.1  123456  7890 pts/0    S    12:34   0:00 /bin/bash mon_script.sh

Ici, le PID est 12345.
📌 Étape 2 : Arrêter le Processus

Utilise kill pour l’arrêter proprement :

kill 12345

Si cela ne fonctionne pas, force l’arrêt avec -9 :

kill -9 12345

🔹 2️⃣ Arrêter un Processus avec pkill

Si tu connais le nom du script ou du programme, tu peux l’arrêter directement :

pkill -f nom_du_script

Exemple :

pkill -f mon_script.sh

Cela ferme tous les processus correspondant à mon_script.sh.
🔹 3️⃣ Utiliser jobs et fg / kill

Si tu as lancé un script avec & et qu’il tourne en arrière-plan dans ton terminal :
📌 Étape 1 : Voir les processus en arrière-plan

jobs -l

Exemple de sortie :

[1]+  12345 Running   ./mon_script.sh &

Le PID est 12345.
📌 Étape 2 : Ramener le script en avant-plan

fg %1

Puis, pour l’arrêter proprement, appuie sur CTRL + C.

Si fg ne fonctionne pas, tue-le avec :

kill %1

🔹 4️⃣ Utiliser htop pour Trouver et Tuer le Processus

Si tu as htop installé (sinon installe-le avec sudo apt install htop), fais :

htop

    Cherche ton script avec les flèches.
    Sélectionne-le et appuie sur F9.
    Choisis 9 pour tuer le processus.

✅ Résumé Rapide

    Lister les processus et tuer avec kill :

ps aux | grep mon_script.sh
kill -9 12345

Tuer un processus avec pkill :

pkill -f mon_script.sh

Lister les jobs et les arrêter :

jobs -l
fg %1  # Puis CTRL + C

Utiliser htop pour tuer un processus :

htop



	root@EECS18:~# ps aux | grep s
script.sh  snap/      

	root@EECS18:~# ps aux | grep script.sh 

root       35668  0.0  0.0  12652  3712 pts/8    S+   13:46   0:00 /bin/bash ./script.sh

root       35689  0.0  0.0  11780  2560 pts/6    S+   13:47   0:00 grep --color=auto script.sh

	root@EECS18:~# kill -9 35668

LE script de la section 4 du TP20fev25 sera arrêté grâce à la commande `kill -9 35668`

voir la commande ` xosview`

voir la commande `glances` c'est l'équivalent de `top` pour voir la charge des processus sur la machine




## **nohup** -> `nohup shuf -i 1-1000000000 > /tmp/numbers10`

la génération des nombres aléatoires dans numbers10 ne s'arrête pas pour l'arrêter il est nécessaire de passer par `ps aux |grep numbers10` pour trouver le **PID** afin de l'arrêter avec 
la commande `kill -9 numéro du PID` **trouvé** grâce à la commande ps aux|grep <fichier>

voir: 			`sleep 10 &  echo "Processus en arrière plan avec PId: $!"`



les commandes :  **top** et **kill** sont les plus importantes dans ce TP : on les utiliseras souvent  **prof**

	taskset -c 2-4  stress-ng --cpu 10
	
	stress-ng ( a chercher) 

 `taskset -c 2,4,6,8  stress-ng --cpu 10`  -> avec cette commande on stress le CPU 2,4,6,8 (on observe que le CPU que nous avons obtenu grâce à **shift** 1 dans top augmente)

 `taskset -pc 1 45308`

 ` taskset -pc 1 45308`

 `ps -eo pid,comm,%cpu --sort=-%cpu | head -10`

  `cpulimit`  pour limiter l'utilisation d'un Cpu : ` cpulimit -l 15 -p 45308` :  45308 est un PID d'un Cpu 

**8.3** reduire le nombre de coeurs 

`cat /sys/device/system/cpu/cpu?/online`    pour afficher le nombre de CPU qui tournent sur notre machine `cat /sys/devices/system/cpu/cpu?/online|wc -l`
**le cpu0** ne s'arrêtera pas parcequ'il doit tourner tout le temps, c'est le dernier a s'éteindre mais les autres **oui* il s'éteingnent 

`echo 0 > /sys/devices/system/cpu/cpu1/online` Cpu1 éteint et pour l'allumer, il faut remplacer 0 par **1** et on observe l'extinction dans top et son redemarrage. 



`echo 1 > /sys/devices/system/cpu/cpu1/online` pour l'allumer  et on observe dans top ils reviennt tous, un à un. 


 

`cpufreq-set -g powersave`  et `cpufreq-set -g performance` pour mettre dans powersave et performance 
