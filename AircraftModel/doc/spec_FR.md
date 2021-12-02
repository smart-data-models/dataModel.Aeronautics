Entité : AircraftModel  
======================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Aeronautics/blob/master/AircraftModel/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Description d'un modèle d'avion générique**  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `capacity`: Nombre de places  - `ceiling`: Altitude maximale que le modèle d'avion peut atteindre en mètres  - `codeIATA`: Type d'avion IATA  - `codeICAO`: Type d'aéronef OACI  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `height`: Hauteur du modèle d'avion en mètres  - `id`: Identifiant unique de l'entité  - `length`: Longueur du modèle d'avion en mètres  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `maximumAllowedFuel`: Carburant maximal de l'avion en kilogrammes  - `maximumAllowedSpeed`:  Vitesse maximale de l'avion en kilomètres par heure  - `mtow`:  Poids maximal de l'avion au décollage en kilogrammes  - `name`: Le nom de cet élément.  - `numberOfEngines`: Nombre de moteurs  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Type d'entité NGSI. Il doit être AircraftModel  - `wingSpan`: Envergure du modèle d'avion en mètres    
Propriétés requises  
- `id`  - `name`  - `type`    
L'entité AircraftModel contient la description d'un modèle d'avion générique avec les paramètres standard utilisés par l'industrie du transport aérien.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AircraftModel:    
  description: 'A description of a generic aircraft model'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
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
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
      type: Geoproperty    
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
            format: uri    
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
#### AircraftModel Valeurs-clés NGSI-v2 Exemple  
Voici un exemple d'un AircraftModel au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### AircraftModel NGSI-v2 normalisé Exemple  
Voici un exemple d'un AircraftModel au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### AircraftModel Valeurs-clés NGSI-LD Exemple  
Voici un exemple d'un AircraftModel au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### AircraftModel NGSI-LD normalisé Exemple  
Voici un exemple d'un AircraftModel au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude