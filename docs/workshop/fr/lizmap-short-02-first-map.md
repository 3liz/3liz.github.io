# Première publication rapide

Nous allons publier le projet QGIS qui se trouve dans l'email afin de faire notre première carte visualisable sur
internet.

## Extension Lizmap

* Installer l'extension Lizmap
* Cliquer sur **Ajouter votre premier serveur** et suivre les étapes
    * L'URL de la page d'accueil, exemple :
        * `https://workshop.lizmap.com/qgisfr/`
    * Le nom d'utilisateur et son mot de passe
    * Si ces informations sont corrects, il demande le nom du serveur. Ce nom est libre, pour votre organisation.
* Si votre serveur s'affiche bien dans le tableau, c'est bon 👍
* Dans les **paramètres** :
    * **Enregistrer le projet QGIS automatiquement**
    * Passer en mode **Débutant** 😏
* Fermer l'extension Lizmap

## Manipulation dans QGIS

* Ouvrir le projet
* Mettre un zoom et une emprise correcte (en montrant toutes les îles)
* Dans les propriétés du projet :
    * Menu **Projet** / **Propriétés**
    * Onglet **Relations**, ajouter toutes les relations **automatiquement** avec le bouton **découvrir** (si PostgreSQL)
    * Onglet **QGIS Serveur**,
        * **Capacités des services**
              * mettre un **titre** et un **résumé**
        * **Capacité WMS**
              * utiliser l'emprise actuelle du canevas dans l'**étendue annoncée**.
        * **Capacité WFS**
              * **publier** toutes les couches
    * Cliquer sur **OK**."
* Ouvrir l'extension Lizmap
* Dans l'onglet **Envoi**, il faut envoyer les données fichiers, dans le bon dossier `theme formation`.
* Quitter l'extension Lizmap (le fichier Lizmap est créé dès que l'on ferme la fenêtre)

!!! tip
    **Bonus** si vous avez une petite image PNG qui se nomme `nom_du_projet.qgs.png` pour remplacer l'image du projet par défaut.
    Vous pouvez regarder l'aide dans l'extension Lizmap → **Options de la carte** pour avoir de l'aide sur la vignette.
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
