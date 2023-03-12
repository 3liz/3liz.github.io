# Première publication rapide

Nous allons publier le projet QGIS qui se trouve dans l'email afin de faire notre première carte visualisable sur
internet.

## Manipulation dans QGIS

* Ouvrir le projet
* Mettre un zoom et une emprise correcte (en montrant toutes les îles)
* Dans les propriétés du projet :
    * Menu **Projet** / **Propriétés**
    * Onglet **Relations**, ajouter toutes les relations **automatiquement** avec le bouton **découvrir**
    * Onglet **QGIS Serveur**,
        * **Capacités des services**
              * mettre un **titre** et un **résumé**
        * **Capacité WMS**
              * utiliser l'emprise actuelle du canevas dans l'**étendue annoncée**.
        * **Capacité WFS**
              * **publier** toutes les couches
    * Cliquer sur **OK**."
* Ouvrir l'extension Lizmap
* **Seulement lors de la première utilisation**, ajouter un serveur Lizmap **en bas** avec :
    * l'URL de la page d'accueil, exemple `https://workshop.lizmap.com/osgeofr/`.
    * Le nom d'utilisateur et son mot de passe
* Quitter l'extension Lizmap (le fichier Lizmap est créé dès que l'on ferme la fenêtre)
* Transférer le projet (`.qgs` et `.cfg`) dans le dossier `qgis/theme_formation` sur le FTP

!!! tip
    **Bonus** si vous avez une petite image PNG qui se nomme `nom_du_projet.qgs.png` pour remplacer l'image du projet par défaut.
    Il faut mettre cette image à côté de votre fichier `nom_du_projet.qgs`. L'image peut-être **jpeg** aussi.

## Prendre en main l'interface web Lizmap

* Se rendre dans l'interface d'administration
    * Les dossiers

!!! warning
    **Seul un** participant va faire la manipulation suivante afin de publier le dossier avec **l'ensemble** des projets QGIS.

* Se rendre sur la page d'accueil puis sur votre carte

!!! success
    Dans votre légende Lizmap, si vous pouvez voir vos couches et les afficher, c'est que ça marche !

**Nous allons désormais [personnaliser l'affichage de nos couches](./lizmap-short-03-legend.md), par exemple afficher
certaines couches par défaut 👉**
