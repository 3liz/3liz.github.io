# Actions

Nous allons créer une action permettant de connaitre la distance entre un logement et la borne incendie la plus proche.
Nous nous réfererons à la [documentation](https://docs.lizmap.com/current/fr/publish/lizmap_plugin/actions.html) pour la création d'actions.

## SQL

Commençons par créer une table de bornes incendie :

```sql
SET SEARCH_PATH = votre_schema;
CREATE TABLE IF NOT EXISTS bornes_incendie
(
    id SERIAL PRIMARY KEY,
    geom geometry(Point,2154)
);

CREATE INDEX ON bornes_incendie USING GIST (geom);
```

## Propriétés du projet

* Charger la couche `bornes_incendie` dans le projet QGIS
* Ajouter, en édition, plusieurs points représentant des bornes incendie sur la carte
* Rendre visible cette couche à l'ouverture de Lizmap
* Activer les popups pour cette couche

## Exercice

En vous inspirant de la documenation, créer le SQL ainsi que le JSON de l'action. Celle-ci doit :

* Ajouter un bouton dans la popup des entités des logements
* Au clique, afficher le message "La plus proche borne a pour id %1 et est à %2 m", où %1 est l'identifant de la borne et %2 la distance en mètre
* Au clique, afficher une droite entre le logement et la borne incendie la plus proche et zoomer dessus

## Solution

??? note "SQL de l'action"
    * Ajoute la fonction `query_to_geojson` disponible [ici](https://docs.lizmap.com/current/fr/publish/lizmap_plugin/actions.html#mandatory-postgresql-functions).
    * Puis créer la fonction `lizmap_get_data`.
    ```sql
    SET SEARCH_PATH = z_formation;
    -- Create a query depending on the action, layer and feature and returns a GeoJSON.
    CREATE OR REPLACE FUNCTION lizmap_get_data(parameters json)
    RETURNS json AS
    $$
    DECLARE
        feature_id varchar;
        layer_name text;
        layer_table text;
        layer_schema text;
        action_name text;
        sqltext text;
        datasource text;
        ajson json;
    BEGIN

        action_name:= parameters->>'action_name';
        feature_id:= (parameters->>'feature_id')::varchar;
        layer_name:= parameters->>'layer_name';
        layer_schema:= parameters->>'layer_schema';
        layer_table:= parameters->>'layer_table';

        IF action_name = 'plus_proche_borne_incendie' THEN
            -- Dessine une ligne jusqu'à la plus proche borne à incendie
            datasource:= format('
                WITH tmp_logement AS (
                SELECT geom FROM logement WHERE id = ''%1$s''
                )
                SELECT
                    id, ST_Distance(bornes_incendie.geom, logement.geom),
                    ''La plus proche borne a pour id '' || bornes_incendie.id || '' et est à '' || ST_Distance(bornes_incendie.geom, logement.geom)::integer || ''m'' AS message,
                    ST_MakeLine(logement.geom, bornes_incendie.geom) AS geom,
                    bornes_incendie.id AS borne_id
                    FROM
                        bornes_incendie,
                        tmp_logement logement
                    ORDER BY ST_Distance(bornes_incendie.geom, logement.geom)
                LIMIT 1
            ',
            feature_id
            );
        ELSE
        -- Default : return geometry
            datasource:= format('
                SELECT
                %1$s AS id,
                ''The geometry of the object have been displayed in the map'' AS message
                geom
                FROM "%2$s"."%3$s"
                WHERE id = %1$s
            ',
            feature_id,
            layer_schema,
            layer_table
            );

        END IF;

        SELECT query_to_geojson(datasource)
        INTO ajson
        ;
        RETURN ajson;
    END;
    $$
    LANGUAGE 'plpgsql'
    IMMUTABLE STRICT;

    COMMENT ON FUNCTION lizmap_get_data(json) IS 'Generate a valid GeoJSON from an action described by a name, PostgreSQL schema and table name of the source data, a QGIS layer name, a feature id and additional options.';
    ```
    * Puis créer le JSON:
    ```json
    [
        {
            "name": "plus_proche_borne_incendie",
            "title": "Trouver la plus proche borne à incendie de ce logement",
            "scope": "feature",
            "layers" : [
                "logement_47b4d824_19f3_40a6_95ac_c144f8e53562"
            ],
            "icon": "icon-resize-small",
            "options": {},
            "style": {
                "graphicName": "circle",
                "pointRadius": 6,
                "fill": true,
                "fillColor": "lightred",
                "fillOpacity": 0.3,
                "stroke": true,
                "strokeWidth": 4,
                "strokeColor": "red",
                "strokeOpacity": 0.8
            },
            "callbacks": [
                {"method": "zoom"},
                {"method": "select", "layerId": "bornes_incendie_7e4f3577_4c55_4351_8949_a4359ae05340"}
            ]
        }
    ]
    ```