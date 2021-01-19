Entité : AircraftModel  
======================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Aeronautics/blob/master/AircraftModel/LICENSE.md)  
Description globale : **Description d'un modèle d'avion générique**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `capacity`: Nombre de sièges  - `ceiling`: Altitude maximale que le modèle d'avion peut atteindre en mètres  - `codeIATA`: Type d'avion IATA  - `codeICAO`: Type d'avion OACI  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `height`: Hauteur du modèle d'avion en mètres  - `id`: Identifiant unique de l'entité  - `length`: Longueur du modèle d'avion en mètres  - `location`:   - `maximumAllowedFuel`: Carburant maximal des avions en kilogrammes  - `maximumAllowedSpeed`:  Vitesse maximale des avions en kilomètres par heure  - `mtow`:  Poids maximum des avions au décollage en kilogrammes  - `name`: Le nom de cet article.  - `numberOfEngines`: Nombre de moteurs  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: Type d'entité NGSI. Il doit s'agir d'un modèle d'avion  - `wingSpan`: Modèle d'avion en mètres d'envergure    
Propriétés requises  
- `id`  - `name`  - `type`    
L'entité AircraftModel contient une description d'un modèle d'avion générique avec les paramètres standards utilisés par l'industrie aérienne.  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AircraftModel:    
  description: 'A description of a generic aircraft model'    
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
    capacity:    
      description: 'Number of seatings'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Integer    
    ceiling:    
      description: 'Maximum altitude the aircraft model can reach in metres'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: metres    
    codeIATA:    
      description: 'IATA aircraft type'    
      pattern: ^[A-Z0-9]{3}$    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    codeICAO:    
      description: 'ICAO aircraft type'    
      pattern: ^[A-Z]{1}[A-Z0-9]{3}$    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    height:    
      description: 'Aircraft model height in metres'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: metres    
    id:    
      anyOf: &aircraftmodel_-_properties_-_owner_-_items_-_anyof    
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
    length:    
      description: 'Aircraft model length in metres'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: metres    
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
    maximumAllowedFuel:    
      description: 'Aircraft maximum fuel in kilograms'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: kilograms    
    maximumAllowedSpeed:    
      description: ' Aircraft maximum speed in kilometers per hour'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'kilometers per hour'    
    mtow:    
      description: ' Aircraft maximum takeoff weight in kilograms'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: kilograms    
    name:    
      description: 'The name of this item.'    
      type: Property    
    numberOfEngines:    
      description: 'Number of engines'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Integer    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *aircraftmodel_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
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
    type:    
      description: 'NGSI Entity type. It has to be AircraftModel'    
      enum:    
        - AircraftModel    
      type: Property    
    wingSpan:    
      description: 'Aircraft model wingspan in metres'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: metres    
  required:    
    - id    
    - type    
    - name    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### AircraftModel NGSI V2 key-values Example  
Voici un exemple de modèle d'avion au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "aircraftModel-AirbusA310-200",  
    "type": "AircraftModel",  
    "codeIATA": "312",  
    "codeICAO": "A310",  
    "name": "Airbus A310-200",  
    "length": 46.66,  
    "wingSpan": 43.9,  
    "height": 15.8,  
    "mtow": 144000,  
    "maximumAllowedSpeed": 850,  
    "maximumAllowedFuel": 47940,  
    "ceiling": 12527,  
    "numberOfEngines": 4,  
    "capacity": 150  
}  
```  
#### AircraftModel NGSI V2 normalisé Exemple  
Voici un exemple de modèle d'avion au format JSON normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "aircraftModel-AirbusA310-200",  
    "type": "AircraftModel",  
    "codeIATA": {  
        "value": "312"  
    },  
    "codeICAO": {  
        "value": "A310"  
    },  
    "name": {  
        "value": "Airbus A310-200"  
    },  
    "length": {  
        "value": 46.66  
    },  
    "wingSpan": {  
        "value": 43.9  
    },  
    "height": {  
        "value": 15.8  
    },  
    "mtow": {  
        "value": 144000  
    },  
    "maximumAllowedSpeed": {  
        "value": 850  
    },  
    "maximumAllowedFuel": {  
        "value": 47940  
    },  
    "ceiling": {  
        "value": 12527  
    },  
    "numberOfEngines": {  
        "value": 12527  
    },  
    "capacity": {  
        "value": 12527  
    }  
}  
```  
#### AircraftModel NGSI-LD key-values Example  
Voici un exemple de modèle d'avion au format JSON-LD comme valeurs clés. Ce modèle est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:AircraftModel:aircraftModel-AirbusA310-200",  
    "type": "AircraftModel",  
    "codeIATA": "312",  
    "codeICAO": "A310",  
    "name": "Airbus A310-200",  
    "length": 46.66,  
    "wingSpan": 43.9,  
    "height": 15.8,  
    "mtow": 144000,  
    "maximumAllowedSpeed": 850,  
    "maximumAllowedFuel": 47940,  
    "ceiling": 12527,  
    "numberOfEngines": 4,  
    "capacity": 150,  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
#### AircraftModel NGSI-LD normalisé Exemple  
Voici un exemple de modèle d'avion au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:AircraftModel:aircraftModel-AirbusA310-200",  
    "type": "AircraftModel",  
    "codeIATA": {  
        "type": "Property",  
        "value": "312"  
    },  
    "codeICAO": {  
        "type": "Property",  
        "value": "A310"  
    },  
    "name": {  
        "type": "Property",  
        "value": "Airbus A310-200"  
    },  
    "length": {  
        "type": "Property",  
        "value": 46.66  
    },  
    "wingSpan": {  
        "type": "Property",  
        "value": 43.9  
    },  
    "height": {  
        "type": "Property",  
        "value": 15.8  
    },  
    "mtow": {  
        "type": "Property",  
        "value": 144000  
    },  
    "maximumAllowedSpeed": {  
        "type": "Property",  
        "value": 850  
    },  
    "maximumAllowedFuel": {  
        "type": "Property",  
        "value": 47940  
    },  
    "ceiling": {  
        "type": "Property",  
        "value": 12527  
    },  
    "numberOfEngines": {  
        "type": "Property",  
        "value": 4  
    },  
    "capacity": {  
        "type": "Property",  
        "value": 150  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
