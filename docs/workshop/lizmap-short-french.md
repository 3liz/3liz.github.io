---
hide:
  - navigation
---

# Atelier Lizmap

## Pré-requis

Cet atelier concerne les utilisateurs de l'atelier Lizmap sur 1/2 journée.

* Client FTP (WinSCP sous Windows, Filezilla sous macOS/Linux)
     * `qgis/theme_formation` : le dossier pour l'atelier
     * `qgis/theme_formation/media/metadata.pdf` : un fichier PDF
* QGIS 3.16
* Extension Lizmap dans QGIS Bureautique
* Projet QGIS dans l'email
     * Le projet QGIS contient déjà les couches PostgreSQL
  
## Liens

* Démo https://demo.lizmap.com
* Hébergement Lizmap clé en main https://www.lizmap.com
* Présentations PDF/HTML https://docs.3liz.org/talks/#lizmap
* Mailing-list Osgeo Lizmap
    * https://lists.osgeo.org/mailman/listinfo/lizmap
* Comptes Twitter :
    * https://twitter.com/LizmapForQgis pour Lizmap uniquement
    * https://twitter.com/3LIZ_news à propos de 3Liz
    * https://twitter.com/3lizRelease à chaque fois que l'on fait une nouvelle version sur un projet GitHub dans un de nos projets
* Code source
    * Lizmap Web Client https://github.com/3liz/lizmap-web-client/
    * Lizmap côte QGIS (bureautique et serveur) : https://github.com/3liz/lizmap-plugin/
    * 3Liz https://github.com/3liz/ pour extensions QGIS Serveur, modules Lizmap

## Documentation

* https://docs.lizmap.com/
  * Voir l'architecture de Lizmap et les manuels

## Première publication rapide

* Ouvrir le projet
* Mettre une emprise correcte (en montrant toutes les îles)
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
* Ouvrir l'extension Lizmap
* **Seulement une fois**, ajouter un serveur Lizmap avec l'URL de la page d'accueil
    * Exemple `https://workshop.lizmap.com/qgis_fr_matin/`.
    * On n'a pas besoin du nom d'utilisateur et du mot de passe
* Quitter l'extension Lizmap (le fichier Lizmap est créé dès que l'on ferme la fenêtre)
* Transférer le projet (`.qgs` et `.cfg`) dans le dossier `qgis/theme_formation` sur le FTP

!!! tip
    **Bonus** si vous avez une petite image PNG `nom_du_projet.qgs.png` pour remplacer l'image du projet par défaut.

## Prendre en main l'interface web Lizmap

* La carte
* Les dossiers
* L'interface d'administration

## Légende

* Faire des groupes dans la légende
    * `Saisie`
    * `Données`
    * `hidden`, avec `h` minuscule
* Ranger les couches dans les groupes en regardant la capture ci-dessous  
* Renommer les couches avec un nom plus présentable
    * **Exception** pour l'orthophoto IGN, dans le groupe `hidden` qui doit avoir le nom `ign-photo`
    
![legend](./media/legend.png)

!!! success
    Lizmap utilise **QGIS Serveur** en arrière-plan, la légende est donc identique que sur QGIS Bureautique.

    Certaines configurations dans le projet QGIS **ou** dans l'extension Lizmap ont un impact dans l'interface web.

!!! tip
    **À partir de maintenant**, envoyez souvent les données sur le serveur pour voir les modifications.

* Faire une symbologie rapide sur les points.
* Ajouter des étiquettes avec le nom de la commune et ajouter un seuil de visibilité en fonction de l'échelle (1:300 000)
    * Champs `name` pour la source des étiquettes
    * Onglet **Rendu**, seuil de visibilité minimum 1:300 000
* Manipulation dans **l'extension** Lizmap, dans l'onglet **Couches** :
    * Pour les **communes**, mettre la couche visible par défaut
    * Ajouter des **liens** sur deux couches :
        * PDF pour les observateurs : `media/metadata.pdf`, un lien vers un PDF, stocké dans le dossier `media` (vous pouvez le voir dans le logiciel FTP)
        * HTML pour les communes : `https://fr.wikipedia.org/wiki/Liste_des_communes_de_la_Polyn%C3%A9sie_fran%C3%A7aise`
    * Dans l'onglet **fond**, ajouter la couche **IGN France** **Orthophoto**. Désormais, on n'a plus besoin de clé.

![Lizmap layer properties](./media/lizmap_layer_properties.png)

## Table attributaire

* Depuis **l'extension**, activer la table attributaire pour la couche des **communes**.
    * Dans l'onglet **table attributaire**, ajouter une nouvelle couche

![Lizmap attribute table](./media/lizmap_attribute_table.png)

!!! tip
    On peut améliorer le visuel de notre table attributaire en ajoutant des alias sur nos champs :
    
    * **Propriétés** de la couche vecteur ➡ **Formulaire d'attribut** ➡ **Alias** pour chaque champ

## Interactions avec les popups "auto" et "qgis"

* Dans **l'extension** Lizmap, onglet **couches**, activer les popups sur la couche `commune` en mode `auto` et vérifier le résultat en cliquant sur une commune
* Faire une popup un mode **QGIS** sur la même couche :

Ces popups **QGIS** sont très puissantes grâce à l'utilisation des **expressions** QGIS :

```html
<ul>
    <li>[% "name" %]</li>
    <li>[% "population" %]</li>
</ul>
```

* Copier/coller ce code HTML dans les propriétés de la couche vecteur `commune`, onglet **Affichage**, puis **Infobulle HTML**.
* **Astuce** : QGIS ➡ **Vue** ➡ **Afficher les infobulles** pour afficher directement dans QGIS bureautique. Vous devez sélectionner aussi l'outil infobulle dans la barre d'outils.

### Avec des expressions

On peut aussi utiliser des expressions QGIS :

* Mettre en majuscule le nom de la commune
* Afficher la population en rouge si moins de 20 000 habitants

??? note "Afficher les solutions"
    * Première solution pour les majuscules :
    ```html
    <ul>
        <li>[% upper("name") %]</li>
        <li>[% "population" %]</li>
    </ul>
    ```
    * Deuxième solution pour la population en rouge :
    ```html
    <ul>
        <li>[% upper("name") %]</li>
        <li style="color:[% if( "population" > 20000, 'black', 'red') %]">[% "population" %]</li>
    </ul>
    ```

On peut avoir le même style graphique que la popup `auto` avec la popup `qgis` en lisant la
[documentation](https://docs.lizmap.com/current/fr/publish/configuration/popup.html#qgis-popup).

## Édition d'une couche

On souhaite désormais rendre éditable une couche depuis l'interface web afin de pouvoir ajouter des **observations**.

* Dans QGIS, faire un essai du formulaire par défaut sur la couche des **observations**. Vous avez besoin de passer en mode édition d'abord avec le petit crayon **jaune**.
* Améliorer le formulaire dans QGIS :
    * Propriétés de la couche ➡ Formulaire d'attributs ➡ Conception par glisser/déposer
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
        * Date/heure par défaut
    * `photo` : 
        * Alias `Photo`
        * Pièce jointe
    * `gender` : 
        * Alias `Genre`
        * Liste de valeurs : `Mâle`, `Femelle`

![Form values](./media/list_value.png)

* Une fois que le formulaire est OK dans QGIS (à peu près 🙂), ajouter l'**édition** dans l'extension Lizmap pour cette couche.

!!! success
    On peut utiliser des expressions QGIS dans les formulaires (visibilité, conditions, valeurs par défaut etc).
    [Lire la documentation](https://docs.lizmap.com/current/fr/publish/configuration/expression.html).

## Impression PDF

### Choix de la zone d'impression par l'utilisateur

* Dans le projet QGIS, il y a déjà une mise en page `Landscape A4`.
    * Activer l'impression dans l'**extension** Lizmap, onglet **Options**
    * Personnaliser la zone de titre dans le PDF :
        * Clic sur le titre `Example workshop`
        * **Identifiant de l'objet** ➡ `title`

!!! success
    Dans ce cas-là, c'est l'utilisateur qui choisit ce qu'il souhaite imprimer en PDF.

### Depuis une popup, lié à une entité

* Dupliquer la mise en page actuelle et en faire un atlas :
    * Menu **Projet**, **Gestionnaire de mise en page**, **Dupliquer**, nom `Fiche commune PDF`
    * Éditer cette nouvelle mise en page
    * Activer l'atlas sur la couche des communes
    * Changer le titre pour afficher le nom de la commune
    * Configurer la carte pour suivre l'atlas.

!!! success
    Alors que dans ce cas-là, le PDF est lié a une entité précise.

## Dataviz

### Diagramme en bar

* Ajouter un **diagramme en bar** concernant la population sur la couche des communes (et non pas un histogramme).
    * Title
    * Description
    * Couche : commune
    * Champ X : Nom
    * Pas d'agrégation
    * Trace :
        * champ **population**
        * couleur bleue

![Dataviz population](./media/dataviz_population.png)

### Camembert

* Faire un camembert sur la répartition des observateurs :
    * Ajouter un champ virtuel `count` dans **observateurs** de type **entiers** :

```
relation_aggregate(
	relation:='observation_fk_id_person_fkey',
	aggregate:='count',
	expression:="id"
)
```

* Puis ajouter le camembert :
    * Title
    * Description
    * Couche : Observateurs
    * Champ X : Nom
    * Agrégation sum
    * Trace : count

![Dataviz pie](./media/dataviz_pie.png)

### Filtrage sur les graphiques

Pour le moment, ce sont des graphiques montrant une couche entière. Il est possible de faire des graphiques pour une entité
précise, par exemple, la répartition des espèces pour un observateur.

![Dataviz filtered pie](./media/filtered_plot.png)

* Ajouter un champ virtuel `label_species` (text) dans la couche `observations` pour avoir le nom de l'espèce :

```
attribute(get_feature('species_aa247cf3_58c8_4852_8ada_1d707a593cfe', 'id', "fk_id_specie"),'es_nom_commun')
```

* Ajouter un camembert sur la couche des observateurs :

    * Camembert
    * Titre : Espèce de l'observateur
    * Couche : Observations
    * Champ X : `label_species`
    * Agrégation `Count`
    * Traces : `id`
    * Case à cocher **Afficher le graphique filtré dans la popup du parent**
    * Case à cocher **Afficher seulement dans les popups des enfants**

![Dataviz filtered pie](./media/dataviz_filtered.png)

??? note "Résultat final"
    ![Dataviz filtered pie](./media/filtered_plot.gif)

**Merci de votre attention 😎**