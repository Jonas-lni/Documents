## configuration réseaux :

pour pouvoir faire le TP Systèmes d'exploitation du mois de janvier 2025, il faut passer en mode ROOT

Faire des : apt install -y ethtool
            apt install wireshark
            apt install nmap 
            apt install nc 
            apt install openssh-server
            apt install etherape

récupérer les RFCs 1918 et 3927

            Wget hhtps://wwww.ietf.org/rfc/rfc1918.txt

            Wget hhtps://wwww.ietf.org/rfc/rfc3927.txt


## Diagramme de séquence:

Pour comprendre le réseau en profondeur, il est essentiel de comprendre les netmask (CIDR) et les schémas des trames -> les sollicitation et et les réponses : ARP - Broadcast - source et destination

Désactivation du Wifi pour isoler le réseau de l'internet pour voir clairement ce qui se passe:

        systemctl mask evahi-daemon
        systemctl stop ufw
        systemctl stop NetworkManager 
        nmcli radio wifi off
ok

   sysctl net.ipv4    

   sysctl -w ipv4.ip_default_ttl = 1  **(ttl : time to live) à faire une recherche sur la modification du nombre du ttl )**

   sysctl -w ipv4.ip_default_ttl=1

   sysctl -w ipv4.ip_default_ttl = 1

   sysctl -w ipv4.ip_default ttl = 1

   clear

   sysctl net | grep ttl

   sysctl -w net.ipv4.ip_default_ttl = 1

   sysctl -w net.ipv4.ip_default_ttl=1

   ping 192.168.2.2

ping 192.168.2.130

   sysctl -w net.ipv4.ip_default_ttl=64

   sysctl -w net.ipv4.ip_default_ttl=64

   sysctl net | grep ttl


- **3.11 réduire la MTU d'une interface du routeur par la commande**

        ip link set dev <interface> mtu <valeur>  

exemple :  ip link set dev enp1s0 mtu 1000 -> ip a on observe que la MTU de mon interface **enp1s0** est de 1000

avec la commande
                ping -s 1200 192.168.2.130 -c1 -M do

on dit au pc d'envoyer le paquet sans le couper, si la MTU du routeur est de 1100, il ne passera pas parceque la MTU du routeur est inférieure à celle du paquer envoyé qui est de 1200

- **3.13 l'outil tracepath** cet outil nous permet par ou passe une trame

        tracepath -n 192.168.2.130

ça nous donne concrétement :

**root@EECS18:~# tracepath -n 192.168.2.130
 1?: [LOCALHOST]                      pmtu 1000
 1:  192.168.2.1                                           2.992ms
 1:  192.168.2.1                                           2.880ms
 2:  192.168.2.130                                         3.247ms reached
     Resume: pmtu 1000 hops 2 back 2 ***

 # 4/ communication niveau 4

La communication haut niveau (au sens du modèle OSI) entre machines s'effectue via des ports

**4.1 Vérifier par la commande** **_ss -ntualp_** quels sont les ports ouverts sur ma machine

La commande suivante nous permet de voir les ports ouverts:

        ss -ntualp

La commande suivante ouvre le port 9000 :

        nc -l 9000

La commande cette commande me permet de me connecter à l'ip 192.168.2.2 ce qui permet d'échanger avec ce pc:

        nc 192.168.2.2 9001


Envoi d'un fichier à un autre pc :

        root@EECS18:~# nano paris.txt   # création d'un fichier paris.txt

        root@EECS18:~# cat paris.txt | nc 192.168.2.6 9001   # envoi du fichier à mounir qui a une adresse ip de 192.168.2.6

La commande suivante, permet la lecture du fichier envoyé:

        nc -l 9001 > paris.txt

**Ajout de perte sur une liaison**

**6.5 - Réalisation d'un ping vers une machine et observation du % de perte affiché**

        ping <Ip_machine > -c 10 

**6.6 - Cette Commande applique une perte de 20% sur les paquets à transmettre**

        tc qdisc add dev <interface> root netem loss 20%

**6.7 - Suppression des pertes par la commande suivante**

        tc qdisc del dev <interfaces> root netem
