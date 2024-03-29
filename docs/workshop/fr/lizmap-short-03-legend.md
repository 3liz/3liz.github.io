# Légende

* Faire des groupes dans la légende
    * `Saisie`
    * `Données`
* À l'aide de l'extension Lizmap, dans l'onglet **Fond de cartes** :
    * on peut ajouter le fond "Orthophoto", qui va ajouter lui-même un groupe `baselayers`
* Ranger les couches dans les groupes en regardant la capture ci-dessous  
* Renommer les couches avec un nom plus présentable

** Note, je ne vais plus utiliser le groupe ``hidden``.

![legend](../media/legend.png)

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
        * Fichiers PDF pour les observateurs :

            * `media/metadata.pdf` (un fichier se trouvant **déjà** sur le serveur, ne pas faire l'envoi ❗)
            * ou alors un fichier à vous `media/votre_document.extension` et faire l'envoi vers le serveur

        * Lien HTML pour les communes : `https://fr.wikipedia.org/wiki/Liste_des_communes_de_la_Polyn%C3%A9sie_fran%C3%A7aise`
    * Dans l'onglet **fond**, ajouter la couche **IGN France** **Orthophoto**. Désormais, on n'a plus besoin de clé.

![Lizmap layer properties](../media/lizmap_layer_properties.png)

**Rendons notre carte "interactif" pour répondre au clic sur la carte avec l'usage des [popups](./lizmap-short-04-popups.md) 👉**
