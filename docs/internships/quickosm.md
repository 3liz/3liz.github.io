# Amélioration de l'extension QuickOSM

!!! summary ""
    Annonce de stage publiée le 2 mars 2021

## Description

QuickOSM est une extension QGIS qui permet de récupérer des données d'OpenStreetMap (OSM) en interrogeant un 
serveur Overpass. En ayant quelques connaissances en OSM, l'utilisateur peut télécharger des données dans 
QGIS par thématique et par emprise. QuickOSM s'occupe de façon transparente de faire la requête au serveur,
lire les données, faire un parsage des données et les afficher dans QGIS.

Nous savons par expérience et par le nombre de téléchargements que l'extension est beaucoup utilisée. Le
travail de ce stage sera donc très fortement utilisé par la suite par les utilisateurs de QGIS.

Le code source de l'extension est sur GitHub : 

https://github.com/3liz/QuickOSM

et sur le dépôt officiel QGIS : 

https://plugins.qgis.org/plugins/QuickOSM/

![QuickOSM](./media/quickosm.png)

## Objectifs du stage

L'objectif global du stage est d'améliorer l'extension QuickOSM sur plusieurs points.

### Passage à QGIS Processing

**QGIS Processing** est une partie intégrante de QGIS désormais. Il est fortement recommander d'utiliser ce
framework dès que possible. L'extension n'utilise que partiellement le framework Processing pour le moment.

### "Carte" clé en main

L'utilisation principale de QuickOSM se concentre sur le premier panneau "Requête rapide" mais il nécessite de
connaître les clés et les valeurs dans OSM. Souvent, les utilisateurs souhaitent télécharger une thématique
précise, par exemple faire une carte cyclable. Il serait très intéressant d'avoir la possibilité de
sélectionner un "thème" et ensuite l'extension se chargera de télécharger toutes les couches propres à cette
thématique.

### Configuration JOSM

[JOSM](https://wiki.openstreetmap.org/wiki/JOSM) est l'éditeur le plus puissant pour contribuer sur la base de
données OSM. Il existe des "JOSM Presets" qui décrivent, dans beaucoup de langues, la correspondance entre un
nom commun et la traduction dans OSM. En utilisant ces "presets", on pourrait taper "boulangerie" et QuickOSM
peut aller télécharger "amenity=bakery". Ces presets dans JOSM sont accessibles avec la touche F3.

### Multi-clé

Comme dit plus haut, le panneau le plus utilisé est celui de la "Requête rapide". Mais il ne se contente que
d'une seule clé. Il faut revoir l'interface graphique afin de pouvoir ajouter plusieurs clés dans une seule
requête Overpass.

### Autres possibilités

Selon l'avancement ou les objectifs du stage, on peut ajouter des fonctionnalités, comme améliorer la
possibilité de travailler avec des fichiers OSM en locaux, ajouter des styles QGIS pour les thèmes ci-dessus
etc.

# Compétences qui seront approfondies

De formation bac+2 à bac+3 en géomatique ou informatique, vous souhaitez approfondir les points suivants :

* Language Python
* API PyQGIS, PyQt et Qt
* Écriture des tests unitaires
* Bonnes pratiques Python (Flake8, PyLint)
* Améliorer l'IHM afin de réduire la barrière d'entrée à l'utilisation de QuickOSM

# Conditions du stage

Le stage se déroulera en télétravail ou en présentiel à Montpellier.
Le suivi des développements se feront sur Github. La communication avec l'équipe de 3Liz se fera au travers 
des outils de chat et de gestion de projet Gitlab. La durée de travail hebdomadaire est de 35 heures du lundi
au vendredi.

La durée du stage peut-être variable selon la convention.
Gratification selon les dispositions légales.

# Contacts

Par mail, etrimaille@3liz.com
