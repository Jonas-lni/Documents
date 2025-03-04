
# configuration de PostgreSQL sur un VPS IONOS

## 1. Installation de PostgreSQL
Connecte-toi à ton VPS via SSH :

**Sur le terminal tape :** `ssh root@ton_ip_vps`

**A- Puis installe PostgreSQL (si ce n'est pas déjà fait) :**


**Tape :** `sudo apt update && sudo apt install postgresql postgresql-contrib -y`

**B- Vérifie que le service est actif :**

**Tape:** `sudo systemctl status postgresql`

## 2. Création d'un utilisateur et d'une base de données
**A- Accède à PostgreSQL en tant qu’utilisateur postgres :**

**Tape:** `sudo -u postgres psql`

**B- Crée un utilisateur sécurisé :**

**Tape:** `CREATE USER mon_user WITH ENCRYPTED PASSWORD 'mon_mot_de_passe';`

**C- Crée une base de données :**

**Tape:** `CREATE DATABASE mon_chat_db OWNER mon_user;`

**D- Autorise l'utilisateur à se connecter :**

**Tape:** `GRANT ALL PRIVILEGES ON DATABASE mon_chat_db TO mon_user;`

**E- Quitte PostgreSQL :**

**Tape:** `\q`

## 3. Sécurisation et accès distant

**Option 1 : Accès local uniquement (recommandé)**

Par défaut, PostgreSQL n’écoute que sur localhost. Vérifie dans **/etc/postgresql/XX/main/postgresql.conf :**

**Tape:** `sudo nano /etc/postgresql/XX/main/postgresql.conf`

**(XX correspond à la version installée, ex: 15)**

Assure-toi que cette ligne est bien réglée :

**listen_addresses = 'localhost'**

**Redémarre PostgreSQL :** `sudo systemctl restart postgresql`

➡️ Ton site web pourra se connecter en local sur le VPS, mais pas depuis l’extérieur.

**Option 2 : Accès distant sécurisé (si nécessaire)**

Si tu veux autoriser un accès distant (ex: depuis ton PC), modifie postgresql.conf :

**listen_addresses = '*'**

Puis édite le fichier des permissions **/etc/postgresql/XX/main/pg_hba.conf :**

`sudo nano /etc/postgresql/XX/main/pg_hba.conf`

**Ajoute cette ligne pour autoriser ton IP publique :**

**host    mon_chat_db    mon_user    ton_ip_publique/32    md5**

**Redémarre PostgreSQL :**

`sudo systemctl restart postgresql`

**⚠️ Sécurise ton VPS en ouvrant uniquement le port PostgreSQL (5432) à ton IP avec iptables ou ufw.**

## 4. Connexion depuis ton site web
**Dans ton code Python, utilise psycopg2 :**

import psycopg2
conn = psycopg2.connect(
    dbname="mon_chat_db",
    user="mon_user",
    password="mon_mot_de_passe",
    host="127.0.0.1",  # ou ton IP VPS si distant
    port="5432"
)
cursor = conn.cursor()
cursor.execute("SELECT 'Connexion réussie !'")
print(cursor.fetchone())
conn.close()

## 5. Sauvegardes et maintenance
**Pour sauvegarder la base :**

`pg_dump -U mon_user -W mon_chat_db > sauvegarde.sql`

Pour restaurer :

`psql -U mon_user -d mon_chat_db -f sauvegarde.sql`

