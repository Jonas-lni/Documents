# Tp volumes logiques

## Disques virtuels
 
## Notion:
wubuntu : interface de microsoft sous ubuntu **intéressant**

  **dd if=/dev/zero of=vdiskX count=X bs=1G status=progress** X c'est le numéro du vdisk
  
  **losetup -Pf --show vdisk3**

 Vétrification **ls -lh**

**pvremove  --force  --force /dev/loop34** ->  effacer les loop lié à un disque virtuel

## 2/Création d'un PV:

- root@EECS18:/home/user18/vdisks# **pvcreate /dev/loop33** création d'un PV associé au disk1

- root@EECS18:/home/user18/vdisks# **pvcreate /dev/loop34** création d'un PV associé au disk2

- root@EECS18:/home/user18/vdisks# **pvcreate /dev/loop35** création d'un PV associé au disk3

- root@EECS18:/home/user18/vdisks# **pvcreate /dev/loop36** création d'un PV associé au disk4

## 3/Creation d'un VG:

**vgcreate mousquetaire /dev/loop33** ->  creation du VG demandé dans la ligne 3.1 du TP du 9 janvier 2025

**vgextend mousquetaire /dev/loop34** -> extension du VG mousquetaire en ajoutant le disque de 2GO (vdisk2) on obtient un espace de 3GO

## 4/ Construction initiale LV:

**lvcreate -L 700MB -n atos mousquetaire** -> création du volume atos

**lvcreate -L 1400MB -n aramis mousquetaire** -> création du volume aramis


## 5/ Création de file system :

**5.1** Informations sur atos collectées grâce à la commande **lvdisplay** -> voir atos 

**root@EECS18:** /home/user18/vdisks# **mkfs.ext4 /dev/mousquetaire/atos**

mke2fs 1.46.5 (30-Dec-2021)

Rejet des blocs de périphérique : complété                            

En train de créer un système de fichiers avec 179200 4k blocs et 44832 i-noeuds.

UUID de système de fichiers=8fcb2cb7-fa1a-48bf-bc8a-7cd1175e7a37

Superblocs de secours stockés sur les blocs : 

	32768, 98304, 163840

Allocation des tables de groupe : complété                            

Écriture des tables d'i-noeuds : complété                            

Création du journal (4096 blocs) : complété

Écriture des superblocs et de l'information de comptabilité du système de

fichiers : complété

**5.2** montage des file systems :

Information collectées sur **lvdisplay -m**

root@EECS18:~/vdisks# **sudo mount /dev/mousquetaire/atos /montage/atosvol**

root@EECS18:~/vdisks# **mkdir /montage/aramisvol**

mkdir: impossible de créer le répertoire «/montage/aramisvol»: Le fichier existe

root@EECS18:~/vdisks# **sudo mount /dev/mousquetaire/aramis /montage/aramisvol**

root@EECS18:~/vdisks# mkdir **/montage/prtosvol**

root@EECS18:~/vdisks# **sudo mount /dev/mousquetaire/portos /montage/prtosvol**

root@EECS18:~/vdisks# **mount**

# 6/ changement de taille: 

On souhaite augmenter la taille du LV atos
 

**6.1** Augmentation de la taille du VG mousquetaire à 6GB, avec le disque qui a 3 GB

**lvdisplay -m** on trouve le loop du disque qui à 3GB
  
root@EECS18:~/vdisks# **vgextend mousquetaire /dev/loop36** extention du VG mousquetaire   

**6.3** Augmentation de la taille du LV atos à 1.5GB via la commande lvresize 

**lvresize -L 1.5G /dev/mousquetaire/atos**

	lvdisplay

**6.7** lorsque la commande **df -kh /montage/atosvol** a été tapée pour vérifier si atos avait bien 1.5GB -> nous avons constaté que atos avait toujours 700 MB bien que 1.5GB lui ont été alloués. 

Le file systems doit savoir qu'il y a plus d'espace et qu'il pouvait l'occuper : 

- la commande root@EECS18:~/vdisks#  **resize2fs /dev/mousquetaire/atos** informe le file systems qu'il peut occuper, l'espace disponible

 - lorsque je vérifie avec le commande **df -kh /montage/atosvol** on constate qu'il occupe bien les 1.5GB qui lui ont été alloué  

 **6.10** Augmentation de la taille LV atos à 2GB via la commande **lvresize** avec l'option précedente 

    1- **lvresize -L 2G /dev/mousquetaire/atos**

    2- **resize2fs /dev/mousquetaire/atos**

 lorsqu'on vérifie -> **df -kh /montage/atosvol** on constate que c'est bien augmenté 


## 7/ Remplacement:

**7.1/** Ajout du disque de 3GB au VG mousquetaire ** vgextend mousquetaire /dev/loop35** 

	lvdisplay  **nous a permis d'obtenir le loop35 pour cibler le disque à ajouter dans la ligne de commande vgextend


**7.3** 	pvmove /dev/loop33

**7.4**		vgreduce mousquetaire /dev/loop33

#  8/ Rangement :

**8.1**

**8.2**

**8.3**

**8.4**

**8.5**

