Entität: Aircraft  
=================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Aeronautics/blob/master/Aircraft/LICENSE.md)  
Globale Beschreibung: **Repräsentiert ein generisches Flugzeug**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift.  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `belongsToAircraftModel`: Referenz auf die Flugzeugmodell-Entität  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateIssued`: Datum, an dem die Messung durchgeführt wurde  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `heading`: Aktueller Flugzeugkurs in Grad. Untis: 'Grad'  - `id`: Eindeutiger Bezeichner der Entität  - `isOnGround`: Logischer Indikator, der bestimmt, ob ein Flugzeug am Boden ist  - `location`:   - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `registration`: Hecknummer oder Flugzeugregistrierung  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `speed`: Aktuelle Flugzeuggeschwindigkeit in Kilometern pro Stunde  - `type`: NGSI Entity-Typ. Es muss Aircraft sein  - `verticalSpeed`: Aktuelle vertikale Fluggeschwindigkeit in Metern pro Sekunde    
Erforderliche Eigenschaften  
- `id`  - `registration`  - `type`    
Die Entität "Aircraft" enthält eine Beschreibung eines generischen Flugzeugs mit den von der Luftfahrtindustrie verwendeten Standardparametern.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### Flugzeuge NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Aircraft im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### Flugzeuge NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein Aircraft im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
    "id": "aircraft-ABCDE",  
    "type": "Aircraft",  
    "registration": {  
        "value": "A-BCDE"  
    },  
    "location": {  
        "type": "geo:json",  
        "value": {  
            "type": "Point",  
            "coordinates": [50.503887, 4.469936, 10000]  
        }  
    },  
    "speed": {  
        "value": 810  
    },  
    "verticalSpeed": {  
        "value": 2  
    },  
    "isOnGround": {  
        "value": false  
    },  
    "heading": {  
        "value": 45  
    },  
    "dateIssued": {  
        "type": "DateTime",  
        "value": "2020-12-09T19:01:35.865Z"  
    },  
    "belongsToAircraftModel": {  
        "type": "Relationship",  
        "value": "aircraftModel-AirbusA310-200"  
    }  
}  
```  
#### Flugzeuge NGSI-LD-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Aircraft im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
      "coordinates": [  
        50.503887,  
        4.469936,  
        10000  
      ]  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### Flugzeuge NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein Aircraft im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Aircraft:aircraft-ABCDE",  
  "type": "Aircraft",  
  "registration": "A-BCDE",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      50.503887,  
      4.469936,  
      10000  
    ]  
  },  
  "speed": 810,  
  "verticalSpeed": 2,  
  "isOnGround": false,  
  "heading": 45,  
  "dateIssued": "2020-12-09T19:01:35.865Z",  
  "belongsToAircraftModel": "urn:ngsi-ld:AircraftModel:aircraftModel-AirbusA310-200",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
