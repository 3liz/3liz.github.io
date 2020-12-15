---
Title: Atelier Lizmap
Favicon: media/lizmap.png
...

# Atelier Lizmap journée QGIS-FR

## Sommaire

[TOC]

## Pré-requis

Cet atelier concerne les utilisateurs des journées QGIS-FR décembre 2020 sur l'atelier Lizmap :

* FTP Client
* QGIS 3.10  
* Extension Lizmap
* Projet QGIS de l'email

## Documentation

* https://docs.lizmap.com/current/fr/

## Liens

* Hébergement Lizmap clé en main https://www.lizmap.com
* Mailing-list Osgeo Lizmap
    * http://osgeo-org.1560.x6.nabble.com/Lizmap-f5416555.html
    * https://lists.osgeo.org/mailman/listinfo/lizmap
* Compte Twitter https://twitter.com/LizmapForQgis
* Code source
    * Lizmap Web Client https://github.com/3liz/lizmap-web-client/
    * 3Liz https://github.com/3liz/

## Première publication

* Ouvrir le projet
* Vérifier l'emprise  
* Dans les propriétés du projet :
    * Onglet **Relations**, ajouter toutes les relations automatiquemes
    * Onglet **QGIS Serveur**,
        * **Capacités des services**, mettre un **titre** et un **résumé**
        * **Capacité WMS**, utiliser l'emprise actuelle du canevas
        * **Capacité WFS**, publier toutes les couches
* Ouvrir l'extension Lizmap et quitter.
* Transférer le projet (`.qgs` et `.cfg`) dans le dossier `theme_formation`

**Bonus** si vous avez une petite image PNG.

## Prendre en main l'interface Lizmap

* La carte
* Les dossiers
* L'interface d'administration
    
## Légende

* Faire des groupes dans la légende
    * `Saisie`
    * `Données`
    * `hidden`, avec `h` minuscule
* Renommer les couches avec un nom plus présentable
    * **Exception** pour l'orthophoto IGN, dans le groupe `hidden` avec comme nom `ign-photo`
    
![legend](./media/legend.png)

* Faire une symbologie rapide sur les communes :
    * **Catégorisation** sur `name`
    * Astuce, changer le symbole pour enlever en partie le remplissage
    * Enlever la ligne pour `Water`
* Manipulation dans l'extension Lizmap pour l'affichage
* Mettre des liens sur une couche : 
    * `media/metadata.pdf`, un lien vers un PDF, stocké dans le dossier `media`
    * `https://fr.wikipedia.org/wiki/Liste_des_communes_de_la_Polyn%C3%A9sie_fran%C3%A7aise`
* Dans l'extension Lizmap, ajouter un **fond**, **IGN France**, **Orthophoto** avec la clée `pratique`

## Table attributaire

* Depuis l'extension, activer la table attributaire pour la couche des **communes**.

## Interactions avec les popups

* Dans l'extension Lizmap, activer les popups sur la couche `commune` en mode `auto`.
* Utiliser les alias sur un champ pour les "nettoyer" depuis les **propriétés de la couche** -> 
  **Formulaire d'attributs** -> un champ en particulier -> **Alias**.
* Faire une popup un mode **QGIS** :

**Astuce** : QGIS -> **Vue** -> **Afficher les infobulles** pour afficher directement dans QGIS.

```html
<ul>
<li>[% "name" %]</li>
<li>[% "population" %]</li>
</ul>
```

On peut aussi utiliser des expressions QGIS : 
    * Mettre en majuscule le nom de la commune
    * Afficher la population en rouge si moins de 20 000 habitants

## Édition d'une couche

On souhaite désormais rendre éditable une couche depuis l'interface web afin de pouvoir ajouter des **observations**.

* Dans QGIS, faire un essai du formulaire par défaut sur la couche des **observations**.
* Améliorer le formulaire dans QGIS
    * Propriétés de la couche -> Formulaire d'attributs -> Conception par glisser/déposer
    * Supprimer le champ `id`
    * Faire 2 groupes : `Requis` et `Optionel`
    
![Drag/drop form](./media/drag_and_drop.png)

* Configurer les champs :
    * `fk_id_person` : 
        * Alias `Observateur`
        * Référence de la relation avec `name`
    * `fk_id_specie` : 
        * Alias `Espèce`
        * Valeur relationnelle `species` `id` et `es_nom_commun`
    * `date` : 
        * Alias `Date`
        * Date/heure; par défaut
    * `photo` : 
        * Alias `Photo`
        * Pièce jointe
    * `gender` : 
        * Alias `Genre`
        * Liste de valeurs : `Mâle`, `Femelle`

![Form values](./media/list_value.png)

* Une fois que le formulaire est OK dans Lizmap (à peu près 🙂), ajouter l'édition dans l'extension Lizmap pour cette couche.

## Dataviz

* Ajouter une diagramme en bar concernant la population sur la couche des communes.
* Ajouter un camembert de la répartition des observateurs
    * Ajouter un champ virtuel dans observateurs
    
```
relation_aggregate(
	relation:='observation_fk_id_person_fkey',
	aggregate:='count',
	expression:="id"
)
```

* Pour le moment, ce ne sont que des Dataviz à l'échelle d'une couche. Il est possible de faire des graphiques
  pour une entité, par ex, pour un observateur, on souhaite la répartition des genres de ses observations
  

## Impression PDF

### Choix de la zone d'impression

* Dans le projet QGIS, il y a déjà une mise en page.
    * Activer l'impression dans l'extension Lizmap
    * Personnaliser la zone de titre.

### Depuis une popup

* Dupliquer la mise en page et en faire un atlas : 
    * Activer l'atlas sur les communes
    * Changer le titre pour afficher le nom de la commune
    * Configurer la carte pour suivre l'atlas.
