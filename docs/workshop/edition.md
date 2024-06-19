# Édition

Nous allons faire un petit modèle de données pour recenser des logements.

Nous pourrons voir à travers cet exemple différent aspect de Lizmap.

```mermaid
classDiagram
class logement{
    id serial PK
    adresse text not null
    code_insee text
    type text not null
    nb_pieces int
    besoin_renov boolean
    pmr boolean not null
    fiche_web text
    photo text,
    date_construction date,
    date_revision_fiche date default now()
    geom Point EPSG:2154
}

class agents{
    id serial PK
    nom text not null
}

class etat_des_lieux{
    id serial PK
    id_logement int not null
    id_agent int not null
    date date not null
    photo text
}

logement -- etat_des_lieux
agents -- etat_des_lieux
```

## SQL

Commençons par créer les tables.

```sql
DROP SCHEMA IF EXISTS z_formation CASCADE;
CREATE SCHEMA z_formation;
```

??? note "Afficher les solutions"
    ```sql
    CREATE TABLE z_formation.logement (
        id SERIAL PRIMARY KEY,
        adresse TEXT NOT NULL,
        code_insee text,
        type TEXT NOT NULL,
        nb_pieces INTEGER,
        besoin_renov boolean,
        pmr boolean NOT NULL,
        fiche_web TEXT,
        photo TEXT,
        date_construction DATE,
        date_revision_fiche DATE,
        geom Geometry(Point, 2154)
    );
    CREATE TABLE z_formation.agents
    (
        id SERIAL PRIMARY KEY,
        nom TEXT NOT NULL
    );

    CREATE TABLE z_formation.etat_des_lieux
    (
        id SERIAL PRIMARY KEY,
        id_logement INTEGER NOT NULL,
        id_agent INTEGER NOT NULL,
        date TIMESTAMP NOT NULL,
        photo TEXT,
        FOREIGN KEY (id_logement) REFERENCES z_formation.logement(id),
        FOREIGN KEY (id_agent) REFERENCES z_formation.agents(id)
    );
    ```

N'oublions pas l'index spatial

```sql
CREATE INDEX ON z_formation.logement USING GIST (geom);
```

!!! info

    Pour profiter pleinement de cette excerice, vous devez avoir une couche des communes avec les codes INSEE dans
    votre projet également. Cette couche ne doit pas nécessairement être dans la base PostgreSQL, car on n'édite pas
    la couche des communes en ligne.

## Propriétés du projet

* Charger les couches dans le projet QGIS.
* **Propriétés du projet**, onglet **Relations**, ajouter toutes les relations **automatiquement** avec le bouton **découvrir**.

## Formulaire logement

!!! tip
    Regarder uniquement le formulaire dans QGIS bureautique dans un premier temps, pendant les différentes étapes,
    en ouvrant une session d'édition.

* Dans les propriétés de la couche `logement` :
  * Ajouter des alias sur les champs
  * Faire un formulaire par glisser/déposer
  * Ajouter des **onglets** et des **groupes**
    ![dnd form](./media/longer-workshop/dnd.png)

!!! tip
    Nous n'avons pas besoin du champ `id` pour nos utilisateurs lors d'une édition. C'est une information *interne*.
    Nous pouvons donc le supprimer.

### Paramétrage des "outils" pour les champs

Pour l'ensemble des champs, nous allons configurer les **Type d'outil** ainsi que les contraintes si nécessaire.

Nous allons utiliser la documentation Lizmap sur
[les formulaires avancés](https://docs.lizmap.com/current/fr/publish/layer_properties/attributes_form.html#advanced-form).

* `adresse` :
    * Édition de texte
    * Ajouter une expression pour la contrainte et une erreur qui sera affichée si l'expression n'est pas valide.
    * On peut vérifier si la chaîne est non `NULL` ET non vide.

!!! tip
    On remarque que QGIS détecte les contraintes des champs qui sont en base de données. Mais on peut personnaliser
    les messages d'erreurs.

!!! tip
    Concernant l'expression de **contrainte**, QGIS va l'exécuter et va vérifier si l'expression renvoi
    une valeur **booléenne** si la saisie est **valide** ou **non**.

* `code_insee` :
    * Valeur relationnelle
      * Couche **commune**
      * Clé **INSEE_COM**
      * Valeurs **NOM**
    * Expression de filtre `intersects( @geometry,  @current_geometry )`
    * Ajouter une contrainte et une erreur pour le non NULL
    * Renforcer la contrainte par expression
* `type` :
    * Liste de valeurs
      * `studio` ➡ `Studio`
      * `appartement` ➡ `Appartement`
      * `maison` ➡ `Maison`
      * `villa` ➡ `Villa`
      * ...
* `nb_pieces` :
    * Plage de valeur
* `pmr` :
    * Case à cocher, uniquement **oui** ou **non**, car définition non null lors de la création de la table
* `photo` :
    * Pièce jointe
        * Chemin par défaut, ou alors un dossier comme `../media/specific_media_folder`
        * Filtre `Images (*.png *.jpg *.jpeg)`
* `besoin_renov` :
    * Liste de valeurs, pour transformer la case à cocher en menu déroulant pour inclure le null possible.
        * Valeur NULL ➡ `Inderterminé`
        * `true` ➡ `Oui`
        * `false` ➡ `Non`
* `fiche_web` :
    * Texte
       * Renforçons la contrainte avec une expression. Une [regex](https://fr.wikipedia.org/wiki/Expression_r%C3%A9guli%C3%A8re)
         est plus appropriée, mais utilisons une expression
         simple pour vérifier que la chaîne commence par `http`
       * Ajouter une description pour la contrainte
* `date_construction`
    * Date
        * format `dd/MM/yyyy`
        * La date de construction n'étant pas obligatoire, il faut en tenir compte dans l'expression de vérification
        * `"date_construction" is null or "date_construction" <=  now() `
* `date_revision_fiche`
    * Date
        * Format date

!!! warning
    Le support **complet** des expressions est un sujet complexe et non terminé. Il y a plein de **différents**
    contextes pour l'évaluation des expressions, voir le ticket [GitHub](https://github.com/3liz/lizmap-web-client/issues/3226).

    L'évaluation d'une expression lors d'une MAJ de l'entité ne peut pas se faire via une expression QGIS.
    Il faut utiliser un [trigger](https://docs.3liz.org/formation-postgis/triggers/)

## Utilisation des popups avec la relation

Nous pouvons activer :

* les popups "Automatique" pour la couche des états des lieux.
* l'affichage des popups enfants dans la couche des logements

## Édition des tables filles

Pour permettre l'ajout des états des lieux, il faut :

* Avoir les relations
* Avoir l'édition sur les 2 couches
* Avoir l'outil de table attributaire sur les couches filles

## Quelques solutions

??? note "Vérifier qu'un champ n'est ni NULL ni une chaîne vide"
    ` "adresse" IS NOT NULL AND "adresse" <> ''`

??? note "Vérifier que la chaîne commence par `http`"
    `left("fiche_web", 4) = 'http'`

    Sinon, avec [regex101](https://regex101.com/), une regexp possible: `(http|https):\/\/([\w-]+(\.[\w-]+)+)`

## Continuer plus loin

On peut continuer plus loin avec l'utilisation de la dataviz, par exemple pour afficher dans les informations **d'une**
commune la répartition des types de logements.
