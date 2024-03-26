# Interactions au clic

Découvrons le principe des **popups** **automatiques** et **Infobulle QGIS**.

## Automatique

* Se rendre dans **l'extension** Lizmap, onglet **couches**
* Activer les popups sur la couche `commune` en mode **Automatique**
* Vérifier le résultat en cliquant sur une commune dans la carte Lizmap

## Infobulle QGIS

* Retourner dans l'extension Lizmap
* Changer la popup un mode **Infobulle QGIS** sur la même couche et cliquer sur le bouton **Générer un tableau HTML**.
* Dans les propriétés de la couche vecteur `commune`, onglet **Affichage**, puis **Infobulle HTML**, observer le code HTML.

!!! tip
    Dans QGIS ➡ **Vue** ➡ **Panneaux** → **Aperçu HTML Lizmap** pour afficher directement dans QGIS bureautique.
    Vous devez sélectionner aussi l'outil infobulle dans la barre d'outils.

Ces informations avec les **infobulles QGIS** sont très puissantes grâce à l'utilisation des **expressions** QGIS 🚀

### Personnalisation de l'infobulle

!!! tip
    On peut facilement supprimer un champ du rendu HTML en supprimant l'ensemble d'un bloc `<tr>...</tr>`.

On peut aussi utiliser des **expressions** QGIS :

* Mettre en majuscule le nom de la commune
* Afficher la population en rouge si moins de 20 000 habitants

??? note "Afficher les solutions"
    * Première solution pour les majuscules :
    ```html
    [% upper("name") %]
    ```
    * Deuxième solution pour la population en rouge :
    ```html
    <td style="color:[% if( "population" > 20000, 'black', 'red') %]">[% "population" %]</td>
    ```

!!! success
    Les expressions QGIS sont vraiment puissantes pour dynamiser du contenu.

**Nous allons voir comment [publier la table attributaire d'une couche](./lizmap-short-05-attribute-table.md) 👉**
