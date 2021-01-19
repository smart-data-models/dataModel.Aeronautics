Entité : Vol  
============  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Aeronautics/blob/master/Flight/LICENSE.md)  
Description globale : **Une description d'un vol générique**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `arrivesToAirport`: Référence à l'entité de l'aéroport d'arrivée  - `belongsToAirline`: Référence à l'entité aérienne  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateAIBT`: Temps réel d'entrée dans le bloc  - `dateALDT`: Heure d'atterrissage réelle  - `dateAOBT`: Temps réel hors bloc  - `dateATO`: Durée réelle  - `dateATOT`: Temps de décollage effectif  - `dateAXIT`: Taxi réel à temps  - `dateAXOT`: Temps de taxi effectif  - `dateArrival`: Date d'arrivée du vol  - `dateCIBT`: Temps d'entrée dans le bloc calculé  - `dateCLDT`: Heure d'atterrissage calculée  - `dateCOBT`: Temps hors bloc calculé  - `dateCTO`: Durée calculée  - `dateCTOT`: Temps de décollage calculé  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateDeparture`: Date de départ du vol  - `dateEIBT`: Durée estimée de l'entrée dans le bloc  - `dateELDT`: Estimation de l'heure d'atterrissage  - `dateEOBT`: Estimation de la durée de la sortie de bloc  - `dateETO`: Durée estimée  - `dateETOT`: Temps de décollage estimé  - `dateEXIT`: Estimation de la durée du trajet en taxi  - `dateEXOT`: Estimation du temps de taxi  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateSIBT`: Heure prévue d'arrivée dans le bloc  - `dateSLDT`: Heure d'atterrissage prévue  - `dateSOBT`: Heure de fermeture prévue  - `dateSTOT`: Heure de décollage prévue  - `dateTIBT`: Temps d'entrée dans le bloc cible  - `dateTLDT`: Heure d'atterrissage prévue  - `dateTOBT`: Temps hors bloc cible  - `dateTSAT`: Délai d'approbation du démarrage cible  - `dateTTOT`: Temps de décollage des objectifs  - `departsFromAirport`: Référence à l'entité de l'aéroport de départ  - `description`: Une description de cet article  - `flightNumber`: Identifiant du vol sans information sur la compagnie aérienne  - `flightNumberIATA`: Identificateur de vol IATA  - `flightNumberICAO`: Identificateur de vol OACI  - `flightType`: Type de vol décrit dans le document OACI 4444 Annexe 2. Enumération : "S, N, G, M, X  - `hasAircraft`: Référence à l'entité de l'aéronef  - `hasAircraftModel`: Référence à l'entité du modèle d'avion  - `id`: Identifiant unique de l'entité  - `location`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `passengerCount`: Nombre de passagers du vol  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `state`: État actuel du vol. Enum : "prévu, actif, inconnu, redirigé, atterri, dérouté, annulé".  - `type`: Type d'entité NGSI. Il doit s'agir d'un vol    
Propriétés requises  
- `id`  - `type`    
L'entité de vol contient une description d'un vol générique avec les paramètres standard utilisés par l'industrie aérienne. Ce modèle est basé sur les spécifications publiées par les principaux organismes du secteur tels que [EUROCONTROL](https://www.eurocontrol.int/), [OACI](https://www.icao.int/) et [IATA](https://www.iata.org/).  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Flight:    
  description: 'A description of a generic flight'    
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
    arrivesToAirport:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Reference to the arrival airport entity'    
      type: Relationship    
    belongsToAirline:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Reference to the airline entity'    
      type: Relationship    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateAIBT:    
      description: 'Actual In-Block Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateALDT:    
      description: 'Actual Landing Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateAOBT:    
      description: 'Actual Off-Block Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateATO:    
      description: 'Actual Time Over'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateATOT:    
      description: 'Actual Take-Off Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateAXIT:    
      description: 'Actual Taxi-In Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateAXOT:    
      description: 'Actual Taxi-Out Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateArrival:    
      description: 'Arrival date of the flight'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateCIBT:    
      description: 'Calculated In-Block Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateCLDT:    
      description: 'Calculated Landing Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateCOBT:    
      description: 'Calculated Off-Block Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateCTO:    
      description: 'Calculated Time Over'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateCTOT:    
      description: 'Calculated Take-Off Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateDeparture:    
      description: 'Departure date of the flight'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateEIBT:    
      description: 'Estimated In-Block Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateELDT:    
      description: 'Estimated Landing Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateEOBT:    
      description: 'Estimated Off-Block Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateETO:    
      description: 'Estimated Time Over'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateETOT:    
      description: 'Estimated Take-Off Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateEXIT:    
      description: 'Estimated Taxi-In Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateEXOT:    
      description: 'Estimated Taxi-Out Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateSIBT:    
      description: 'Scheduled In-Block Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateSLDT:    
      description: 'Scheduled Landing Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateSOBT:    
      description: 'Scheduled Off-Block Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateSTOT:    
      description: 'Scheduled Take-Off Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateTIBT:    
      description: 'Target In-Block Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateTLDT:    
      description: 'Target Landing Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateTOBT:    
      description: 'Target Off-Block Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateTSAT:    
      description: 'Target Start Up Approval Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateTTOT:    
      description: 'Target Take-Off Time'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    departsFromAirport:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Reference to the departure airport entity'    
      type: Relationship    
    description:    
      description: 'A description of this item'    
      type: Property    
    flightNumber:    
      description: 'Flight identifier without information of airline'    
      pattern: ^[A-Z0-9]{1,}$    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    flightNumberIATA:    
      description: 'IATA flight identifier'    
      pattern: ^[A-Z0-9]{3,}$    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    flightNumberICAO:    
      description: 'ICAO flight identifier'    
      pattern: ^[A-Z]{3}[A-Z0-9]{1,}$    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    flightType:    
      description: 'Flight type described as ICAO doc 4444 Appendix 2. Enum:''S, N, G, M, X'''    
      enum:    
        - S    
        - N    
        - G    
        - M    
        - X    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    hasAircraft:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Reference to the aircraft entity'    
      type: Relationship    
    hasAircraftModel:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: 'Reference to the aircraft model entity'    
      type: Relationship    
    id:    
      anyOf: &flight_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *flight_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    passengerCount:    
      description: 'Number of flight passengers'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Integer    
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
    state:    
      description: 'Current state of the flight. Enum:''scheduled, active, unknown, redirected, landed, diverted, cancelled'''    
      enum:    
        - scheduled    
        - active    
        - unknown    
        - redirected    
        - landed    
        - diverted    
        - cancelled    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    type:    
      description: 'NGSI Entity type. It has to be Flight'    
      enum:    
        - Flight    
      type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### Vol NGSI V2 - Exemple de valeurs clés  
Voici un exemple de vol en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "flight-3732",  
    "type": "Flight",  
    "flightNumber": "3732",  
    "flightNumberIATA": "SN3732",  
    "flightNumberICAO": "BEL3732",  
    "flightType": "G",  
    "state": "active",  
    "passengerCount": 25,  
    "dateDeparture": "2018-12-01T10:40:01.00Z",  
    "dateArrival": "2018-12-01T12:40:01.00Z",  
    "dateSOBT": "2018-12-01T10:40:01.00Z",  
    "dateSTOT": "2018-12-01T10:45:01.00Z",  
    "dateSLDT": "2018-12-01T12:35:01.00Z",  
    "dateSIBT": "2018-12-01T12:40:01.00Z",  
    "hasAircraft": "aircraft-ABCDE",  
    "hasAircraftModel": "aircraftModel-AirbusA310-200",  
    "departsFromAirport": "airport-BMA",  
    "arrivesToAirport": "airport-MAD",  
    "belongsToAirline": "airline-SN"  
}  
```  
#### Vol NGSI V2 normalisé Exemple  
Voici un exemple d'un vol au format JSON tel que normalisé. Ce format est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "flight-3732",  
    "type": "Flight",  
    "flightNumber": {  
        "value": "3732"  
    },  
    "flightNumberIATA": {  
        "value": "SN3732"  
    },  
    "flightNumberICAO": {  
        "value": "BEL3732"  
    },  
    "flightType": {  
        "value": "G"  
    },  
    "state": {  
        "value": "active"  
    },  
    "passengerCount": {  
        "value": 25  
    },  
    "dateDeparture": {  
        "type": "DateTime",  
        "value": "2018-12-01T10:40:01.00Z"  
    },  
    "dateArrival": {  
        "type": "DateTime",  
        "value": "2018-12-01T12:40:01.00Z"  
    },  
    "dateSOBT": {  
        "type": "DateTime",  
        "value": "2018-12-01T10:40:01.00Z"  
    },  
    "dateSTOT": {  
        "type": "DateTime",  
        "value": "2018-12-01T10:45:01.00Z"  
    },  
    "dateSLDT": {  
        "type": "DateTime",  
        "value": "2018-12-01T12:35:01.00Z"  
    },  
    "dateSIBT": {  
        "type": "DateTime",  
        "value": "2018-12-01T12:40:01.00Z"  
    },  
    "hasAircraft": {  
        "type": "Relationship",  
        "value": "aircraft-ABCDE"  
    },  
    "hasAircraftModel": {  
        "type": "Relationship",  
        "value": "aircraftModel-AirbusA310-200"  
    },  
    "departsFromAirport": {  
        "type": "Relationship",  
        "value": "airport-BMA"  
    },  
    "arrivesToAirport": {  
        "type": "Relationship",  
        "value": "airport-MAD"  
    },  
    "belongsToAirline": {  
        "type": "Relationship",  
        "value": "airline-SN"  
    }  
}  
```  
#### Vol NGSI-LD valeurs clés Exemple  
Voici un exemple de vol au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:Flight:flight-3732",  
    "type": "Flight",  
    "flightNumber": "3732",  
    "flightNumberIATA": "SN3732",  
    "flightNumberICAO": "BEL3732",  
    "flightType": "G",  
    "state": "active",  
    "passengerCount": 25,  
    "dateDeparture": "2018-12-01T10:40:01.00Z",  
    "dateArrival": "2018-12-01T12:40:01.00Z",  
    "dateSOBT": "2018-12-01T10:40:01.00Z",  
    "dateSTOT": "2018-12-01T10:45:01.00Z",  
    "dateSLDT": "2018-12-01T12:35:01.00Z",  
    "dateSIBT": "2018-12-01T12:40:01.00Z",  
    "hasAircraft": "urn:ngsi-ld:Aircraft:aircraft-ABCDE",  
    "hasAircraftModel": "urn:ngsi-ld:AircraftModel:aircraftModel-AirbusA310-200",  
    "departsFromAirport": "urn:ngsi-ld:Airline:airport-BMA",  
    "arrivesToAirport": "urn:ngsi-ld:Airline:airport-MAD",  
    "belongsToAirline": "urn:ngsi-ld:Airline:airline-SN",  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
#### Vol NGSI-LD normalisé Exemple  
Voici un exemple d'un vol au format JSON-LD tel que normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:Flight:flight-3732",  
    "type": "Flight",  
    "flightNumber": {  
        "type": "Property",  
        "value": "3732"  
    },  
    "flightNumberIATA": {  
        "type": "Property",  
        "value": "SN3732"  
    },  
    "flightNumberICAO": {  
        "type": "Property",  
        "value": "BEL3732"  
    },  
    "flightType": {  
        "type": "Property",  
        "value": "G"  
    },  
    "state": {  
        "type": "Property",  
        "value": "active"  
    },  
    "passengerCount": {  
        "type": "Property",  
        "value": 25  
    },  
    "dateDeparture": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2018-12-01T10:40:01.00Z"  
        }  
    },  
    "dateArrival": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2018-12-01T12:40:01.00Z"  
        }  
    },  
    "dateSOBT": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2018-12-01T10:40:01.00Z"  
        }  
    },  
    "dateSTOT": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2018-12-01T10:45:01.00Z"  
        }  
    },  
    "dateSLDT": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2018-12-01T12:35:01.00Z"  
        }  
    },  
    "dateSIBT": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2018-12-01T12:40:01.00Z"  
        }  
    },  
    "hasAircraft": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Aircraft:aircraft-ABCDE"  
    },  
    "hasAircraftModel": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AircraftModel:aircraftModel-AirbusA310-200"  
    },  
    "departsFromAirport": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Airline:airport-BMA"  
    },  
    "arrivesToAirport": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Airline:airport-MAD"  
    },  
    "belongsToAirline": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Airline:airline-SN"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
