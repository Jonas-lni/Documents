# Tables et insertion à la base de données projet_chat

- Entités principales :

**Utilisateurs : Stocke les informations des utilisateurs.**

**Messages : Stocke les messages envoyés par les utilisateurs.**

**Conversations : Stocke les conversations entre utilisateurs (pour gérer les discussions privées ou de groupe).**

1. Table utilisateurs

**Cette table stocke les informations des utilisateurs.**


	CREATE TABLE utilisateurs (
	    id SERIAL PRIMARY KEY,          -- Identifiant unique de l'utilisateur
	    pseudo VARCHAR(50) UNIQUE NOT NULL, -- Pseudo de l'utilisateur
	    email VARCHAR(100) UNIQUE NOT NULL, -- Adresse email de l'utilisateur
	    mot_de_passe VARCHAR(255) NOT NULL, -- Mot de passe hashé
    	    date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date d'inscription
	);

2. Table conversations

**Cette table stocke les conversations (privées ou de groupe).**


	CREATE TABLE conversations (
	    id SERIAL PRIMARY KEY,          -- Identifiant unique de la conversation
	    nom_conversation VARCHAR(100),  -- Nom de la conversation (optionnel, pour les groupes)
	    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date de création de la conversation
	);

3. Table messages

**Cette table stocke les messages envoyés par les utilisateurs dans une conversation.**


	CREATE TABLE messages (
	    id SERIAL PRIMARY KEY,          -- Identifiant unique du message
    	    conversation_id INT REFERENCES conversations(id) ON DELETE CASCADE, -- Lien vers la conversation
    	    utilisateur_id INT REFERENCES utilisateurs(id) ON DELETE CASCADE,   -- Lien vers l'utilisateur
    	    contenu TEXT NOT NULL,          -- Contenu du message
    	    date_envoi TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date d'envoi du message
	);
4. Table participants_conversation

**Cette table lie les utilisateurs aux conversations (pour savoir qui participe à quelle conversation).**


	CREATE TABLE participants_conversation (
    		utilisateur_id INT REFERENCES utilisateurs(id) ON DELETE CASCADE,   -- Lien vers l'utilisateur
    		conversation_id INT REFERENCES conversations(id) ON DELETE CASCADE, -- Lien vers la conversation
    		PRIMARY KEY (utilisateur_id, conversation_id) -- Clé primaire composée
	    );

**_Explication des relations :_**

**Utilisateurs :** Chaque utilisateur a un identifiant unique (id) qui est utilisé pour lier les messages et les conversations.

**Conversations :** Une conversation peut être entre deux utilisateurs (privée) ou plusieurs (groupe).

**Messages :** Chaque message est lié à une conversation et à un utilisateur.

**Participants_conversation :** Cette table permet de savoir quels utilisateurs participent à quelles conversations.

Exemple d'insertion de données

**Ajouter un utilisateur**

	INSERT INTO utilisateurs (pseudo, email, mot_de_passe)
	VALUES ('Alice', 'alice@example.com', 'motdepassehashé');

**Créer une conversation**

	INSERT INTO conversations (nom_conversation)
	VALUES ('Discussion générale');

**Ajouter des participants à la conversation**

	INSERT INTO participants_conversation (utilisateur_id, conversation_id)
	VALUES (1, 1); -- Alice participe à la conversation 1

**Envoyer un message**

	INSERT INTO messages (conversation_id, utilisateur_id, contenu)
	VALUES (1, 1, 'Bonjour tout le monde !');

**Requêtes utiles**

- Récupérer tous les messages d'une conversation

	SELECT u.pseudo, m.contenu, m.date_envoi
	FROM messages m
	JOIN utilisateurs u ON m.utilisateur_id = u.id
	WHERE m.conversation_id = 1
	ORDER BY m.date_envoi;

- Récupérer toutes les conversations d'un utilisateur

	SELECT c.id, c.nom_conversation, c.date_creation
	FROM conversations c
	JOIN participants_conversation pc ON c.id = pc.conversation_id
	WHERE pc.utilisateur_id = 1;


- Améliorations possibles

Gestion des groupes : Ajouter une colonne type_conversation dans la table conversations pour distinguer les conversations privées et les groupes.

Notifications : Ajouter une table pour gérer les notifications des utilisateurs.

Statut des messages : Ajouter une colonne statut dans la table messages pour indiquer si un message a été lu ou non.

Cette structure est une base solide pour un site de chat. Vous pouvez l'adapter en fonction des besoins spécifiques de votre application.


