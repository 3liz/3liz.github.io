# WinSCP

## Installation

* Vous devez télécharger et installer le logiciel **WinSCP** depuis ce lien: 
https://winscp.net/eng/download.php
  
* Une fois l'installation effectuée, vous pouvez enregistrer la connexion vers le serveur FTP.
  
## Enregistrement de votre serveur Lizmap

* 1 Par email, vous avez dû recevoir les identifiants de connexions vers le serveur FTP.
* 2 Ouvrez **WinSCP**.
* 3 Le panneau pour ajouter une nouvelle connexion s'ouvre automatiquement à la première ouverture du logiciel.
  Sinon cliquez sur le bouton `Nouvelle session` situé en haut à gauche de la fenêtre.

![WinSCP](./media/ftp_winscp_1.jpg)

* 4 **Nouveau site**

![WinSCP](./media/ftp_winscp_2.jpg)

* 5 Complétez les informations :
    * **1** : Protocole de fichier: `FTP`
    * **2** : Chiffrement: `Chiffrement TSL/SSL explicite`
    * **3** : Nom d'hôte : Le serveur FTP reçu par email
    * **4** : Numéro de Port: `21`
    * **5** : Nom d'utilisateur : Le nom d'utilisateur reçu par email
    * **6** : Mot de passe : Le mot de passe reçu par email

![WinSCP](./media/ftp_winscp_3.jpg)

* 6 Cliquer sur sauver pour enregistrer le nouveau site :
    * **1** : Enregistrer la session sous : Nom du site, ex : Lizmap
    * **2** : Enregistrer le mot de passe: Vous pouvez côcher la case si vous le souhaitez
    * **3** : Créer un raccourci sur le bureau : Permet d'avoir un accès direct au site via un raccourci sur votre bureau

![WinSCP](./media/ftp_winscp_4.jpg)

* 7 Pour vous connecter à votre nouveau site allez dans l'onglet `Session` puis `Sites` et cliquez sur votre site.

![WinSCP](./media/ftp_winscp_5.jpg)

* 8 Vous devriez avoir un écran semblable à celui-ci: 

![WinSCP](./media/ftp_winscp_6.jpg)

* Description de l'interface
    * Sur la gauche, votre ordinateur
    * Sur la droite, le serveur

* Par **glisser/déposer**, nous allons déplacer des fichiers de votre ordinateur vers le serveur.

## Arborescence par défaut

Sur le serveur, **toujours** dans le dossier `qgis`, nous allons créer des répertoires qui seront vos thématiques Lizmap.

Ensuite, dans votre panneau d'administration Lizmap, vous devez ajouter ce répertoire.

Par exemple :

```bash
/
├── qgis
│   ├── forest
│   │   ├── jungle.qgs
│   │   ├── jungle.qgs.cfg
│   │   └── media
│   │       └── logo.png
│   ├── social
│   └── urban
│       ├── populated_places.qgs
│       ├── populated_places.qgs.cfg
│       ├── urban_project.qgs
│       └── urban_project.qgs.cfg
└── web
```
