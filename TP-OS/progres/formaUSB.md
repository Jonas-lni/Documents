
## Formatage d'une clé USB sur linux en ligne de commande:

root@EECS18:~# **umount /mnt** : permet de monter la clé usb sur /mnt

pour lire la clé USB il faut aller dans **/media/user18**

root@EECS18:~# **ls /mnt** -> le résultat: voir la ligne en dessous. 

résultat **root@EECS18:~# mount**
 
il faut etre dans le root -> **lsblk** pour voir le format -> aller dans /dev 

Faire un **umount** umount /media/user18/CCCOMA_X64FRE_FR-FR_DV9 -> de sda1 : ** pas dans le dossier mais à l'extérieur**

Faire un **umount** umount /media/user18/UEFI_NTFS -> de sda2 : ** pas dans le dossier mais à l'extérieur**

puis faire -> **mkfs.ext4 sda** pour formater cliquer par la suite sur entrer - entrer

mkfs.ext4 /dev/sda **-L MYKEY**    -> -L permet de donner un nom à la clé USB à formater : **important**


vérifier avec **tune2fs -l /dev/sda** pour vérifier    
