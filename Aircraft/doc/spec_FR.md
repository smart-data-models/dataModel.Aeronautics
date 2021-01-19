Entité : Aéronef  
================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Aeronautics/blob/master/Aircraft/LICENSE.md)  
Description globale : **représente un avion générique**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `belongsToAircraftModel`: Référence à l'entité du modèle d'avion  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateIssued`: Date à laquelle la mesure a été prise  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `heading`: L'avion actuel se dirige en degrés. Untis : "degrés".  - `id`: Identifiant unique de l'entité  - `isOnGround`: Indicateur logique qui détermine si un avion est au sol  - `location`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `registration`: Numéro de queue ou immatriculation de l'avion  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `speed`: Vitesse actuelle des avions en kilomètres par heure  - `type`: Type d'entité NGSI. Il doit s'agir d'un aéronef  - `verticalSpeed`: Vitesse verticale actuelle de l'avion en mètres par seconde    
Propriétés requises  
- `id`  - `registration`  - `type`    
L'entité "Aéronef" contient une description d'un aéronef générique avec les paramètres standard utilisés par l'industrie aérienne.  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Aircraft:    
  description: 'Represent a generic aircraft'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    belongsToAircraftModel:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Reference to the aircraft model entity'    
      type: Relationship    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateIssued:    
      description: 'Date when the meassure was taken'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    heading:    
      description: 'Current aircraft heading in degrees. Untis: ''degrees'''    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    id:    
      anyOf: &aircraft_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    isOnGround:    
      description: 'Logical indicator that determines if an aircraft is on ground'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Boolean    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *aircraft_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    registration:    
      description: 'Tail number or aircraft registration'    
      pattern: ^[A-Z]-[A-Z]{4}|[A-Z]{2}-[A-Z]{3}|[A-Z]{5}|N[0-9]{1,5}[A-Z]{0,2}$    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    speed:    
      description: 'Current aircraft speed in kilometres per hour'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'kilometres per hour'    
    type:    
      description: 'NGSI Entity type. It has to be Aircraft'    
      enum:    
        - Aircraft    
      type: Property    
    verticalSpeed:    
      description: 'Current vertical aircraft speed in metres per second'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'metres per second'    
  required:    
    - id    
    - type    
    - registration    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### Aéronef NGSI V2 valeurs clés Exemple  
Voici un exemple d'un avion au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "aircraft-ABCDE",  
    "type": "Aircraft",  
    "registration": "A-BCDE",  
    "location": {  
        "type": "Point",  
        "coordinates": [50.503887, 4.469936, 10000]  
    },  
    "speed": 810,  
    "verticalSpeed": 2,  
    "isOnGround": false,  
    "heading": 45,  
    "dateIssued": "2020-12-09T19:01:35.865Z",  
    "belongsToAircraftModel": "aircraftModel-AirbusA310-200"  
}  
```  
#### Avion NGSI V2 normalisé Exemple  
Voici un exemple d'un avion au format JSON normalisé. Ce format est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
#### Avion NGSI-LD valeurs clés Exemple  
Voici un exemple d'un avion au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:Aircraft:aircraft-ABCDE",  
    "type": "Aircraft",  
    "registration": "A-BCDE",  
    "location": {  
        "type": "Point",  
        "coordinates": [50.503887, 4.469936, 10000]  
    },  
    "speed": 810,  
    "verticalSpeed": 2,  
    "isOnGround": false,  
    "heading": 45,  
    "dateIssued": "2020-12-09T19:01:35.865Z",  
    "belongsToAircraftModel": "urn:ngsi-ld:AircraftModel:aircraftModel-AirbusA310-200",  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
#### Avion NGSI-LD normalisé Exemple  
Voici un exemple d'un avion au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:Aircraft:aircraft-ABCDE",  
    "type": "Aircraft",  
    "registration": {  
        "type": "Property",  
        "value": "A-BCDE"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [50.503887, 4.469936, 10000]  
        }  
    },  
    "speed": {  
        "type": "Property",  
        "value": 810  
    },  
    "verticalSpeed": {  
        "type": "Property",  
        "value": 2  
    },  
    "isOnGround": {  
        "type": "Property",  
        "value": false  
    },  
    "heading": {  
        "type": "Property",  
        "value": 45  
    },  
    "dateIssued": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-12-09T19:01:35.865Z"  
        }  
    },  
    "belongsToAircraftModel": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AircraftModel:aircraftModel-AirbusA310-200"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
