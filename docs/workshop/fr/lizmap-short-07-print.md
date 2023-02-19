# Impression PDF

## Choix de la zone d'impression par l'utilisateur

* Dans le projet QGIS, il y a déjà une mise en page `Landscape A4`.
    * Activer l'impression dans l'**extension** Lizmap, onglet **Options**
    * Personnaliser la zone de titre dans le PDF :
        * Clic sur le titre `Example workshop`
        * **Identifiant de l'objet** ➡ `title`

!!! success
    Dans ce cas-là, c'est l'utilisateur qui choisit ce qu'il souhaite imprimer en PDF.

## Après un clic sur la carte, liée à une entité

* Dupliquer la mise en page actuelle et en faire un atlas :
    * Menu **Projet**, **Gestionnaire de mise en page**, **Dupliquer**, nom `Fiche commune PDF`
    * Éditer cette nouvelle mise en page
    * Activer l'atlas sur la couche des communes
    * Changer le titre pour afficher le nom de la commune
    * Configurer la carte pour suivre l'atlas.

!!! success
    Alors que dans ce cas-là, le PDF est lié à une entité précise.

**Passons à la dernière partie, [l'ajout de graphiques](./lizmap-short-08-dataviz.md) dans notre projet 👉**
