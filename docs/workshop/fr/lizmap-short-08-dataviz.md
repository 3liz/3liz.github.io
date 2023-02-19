# Dataviz

## Diagramme en bar

* Ajouter un **diagramme en bar** concernant la population sur la couche des communes (et non pas un histogramme).
    * Title
    * Description
    * Couche : commune
    * Champ X : Nom
    * Pas d'agrégation
    * Trace :
        * champ **population**
        * couleur bleue

![Dataviz population](../media/dataviz_population.png)

## Camembert

* Faire un camembert sur la répartition des observateurs :
    * Ajouter un champ virtuel `count` dans `observateurs` de type **entiers** :

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

![Dataviz pie](../media/dataviz_pie.png)

## Filtrage sur les graphiques

Pour le moment, ce sont des graphiques montrant une couche entière. Il est possible de faire des graphiques pour une entité
précise, par exemple, la répartition des espèces pour un observateur.

![Dataviz filtered pie](../media/filtered_plot.png)

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

![Dataviz filtered pie](../media/dataviz_filtered.png)

??? note "Résultat final"
    ![Dataviz filtered pie](../media/filtered_plot.gif)

!!! success
    Pour les curieux, je vous recommande le [tutoriel vidéo](https://www.youtube.com/embed/aGJnScdkEtE) sur les relations entre les couches et la dataviz.

**Merci de votre attention 😎**
