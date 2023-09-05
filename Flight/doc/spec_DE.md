<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: Flug  
=============<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Aeronautics/blob/master/Flight/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Eine Beschreibung eines generischen Fluges**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivesToAirport[*]`: Verweis auf die Entität des Ankunftsflughafens  - `belongsToAirline[*]`: Verweis auf die Fluggesellschaft  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateAIBT[date-time]`: Tatsächliche In-Block-Zeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateALDT[date-time]`: Tatsächliche Landezeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAOBT[date-time]`: Tatsächliche Off-Block-Zeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateATO[date-time]`: Tatsächliche Zeit über  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateATOT[date-time]`: Tatsächliche Abflugzeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAXIT[date-time]`: Tatsächliche Taxi-In-Zeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAXOT[date-time]`: Tatsächliche Taxi-Out-Zeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateArrival[date-time]`: Ankunftsdatum des Fluges  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCIBT[date-time]`: Berechnete In-Block-Zeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCLDT[date-time]`: Berechnete Landezeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCOBT[date-time]`: Berechnete Off-Block-Zeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCTO[date-time]`: Berechnete Zeit über  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCTOT[date-time]`: Berechnete Abflugzeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateDeparture[date-time]`: Abflugdatum des Fluges  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEIBT[date-time]`: Geschätzte Zeit innerhalb des Blocks  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateELDT[date-time]`: Geschätzte Landezeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEOBT[date-time]`: Geschätzte Zeit außerhalb des Blocks  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateETO[date-time]`: Geschätzte Zeit über  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateETOT[date-time]`: Geschätzte Abflugzeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEXIT[date-time]`: Geschätzte Taxi-In-Zeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEXOT[date-time]`: Geschätzte Taxi-Out-Zeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `dateSIBT[date-time]`: Geplante Zeit innerhalb des Blocks  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSLDT[date-time]`: Geplante Landezeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSOBT[date-time]`: Geplante Zeit außerhalb des Blocks  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSTOT[date-time]`: Geplante Abflugzeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTIBT[date-time]`: Ziel-In-Block-Zeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTLDT[date-time]`: Ziellandezeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTOBT[date-time]`: Zielzeit außerhalb des Blocks  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTSAT[date-time]`: Ziel Start-up Genehmigungszeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTTOT[date-time]`: Ziel-Startzeit  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `departsFromAirport[*]`: Verweis auf die Entität des Abflughafens  - `description[string]`: Eine Beschreibung dieses Artikels  - `flightNumber[string]`: Flugkennung ohne Angabe der Fluggesellschaft  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightNumberIATA[string]`: IATA-Flugkennung  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightNumberICAO[string]`: ICAO-Flugkennung  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightType[string]`: Flugmuster gemäß ICAO-Dok 4444 Anhang 2 beschrieben. Enum:'S, N, G, M, X'  . Model: [http://schema.org/Text](http://schema.org/Text)- `hasAircraft[*]`: Verweis auf das Luftfahrzeugobjekt  - `hasAircraftModel[*]`: Verweis auf die Entität des Luftfahrzeugmodells  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `passengerCount[number]`: Anzahl der Fluggäste  . Model: [http://schema.org/Integer](http://schema.org/Integer)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `state[string]`: Aktueller Status des Fluges. Enum:'geplant, aktiv, unbekannt, umgeleitet, gelandet, umgeleitet, annulliert'.  . Model: [http://schema.org/Text](http://schema.org/Text)- `type[string]`: NGSI-Entitätstyp. Es muss Flight sein  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Die Flug-Entität enthält eine Beschreibung eines generischen Fluges mit den von der Luftfahrtindustrie verwendeten Standardparametern. Dieses Modell basiert auf Spezifikationen, die von den wichtigsten Organen der Branche wie [EUROCONTROL](https://www.eurocontrol.int/), [ICAO](https://www.icao.int/) und [IATA](https://www.iata.org/) veröffentlicht wurden.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Flight:    
  description: A description of a generic flight    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    arrivesToAirport:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: Reference to the arrival airport entity    
      x-ngsi:    
        type: Relationship    
    belongsToAirline:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: Reference to the airline entity    
      x-ngsi:    
        type: Relationship    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateAIBT:    
      description: Actual In-Block Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateALDT:    
      description: Actual Landing Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateAOBT:    
      description: Actual Off-Block Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateATO:    
      description: Actual Time Over    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateATOT:    
      description: Actual Take-Off Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateAXIT:    
      description: Actual Taxi-In Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateAXOT:    
      description: Actual Taxi-Out Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateArrival:    
      description: Arrival date of the flight    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateCIBT:    
      description: Calculated In-Block Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateCLDT:    
      description: Calculated Landing Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateCOBT:    
      description: Calculated Off-Block Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateCTO:    
      description: Calculated Time Over    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateCTOT:    
      description: Calculated Take-Off Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateDeparture:    
      description: Departure date of the flight    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateEIBT:    
      description: Estimated In-Block Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateELDT:    
      description: Estimated Landing Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateEOBT:    
      description: Estimated Off-Block Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateETO:    
      description: Estimated Time Over    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateETOT:    
      description: Estimated Take-Off Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateEXIT:    
      description: Estimated Taxi-In Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateEXOT:    
      description: Estimated Taxi-Out Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateSIBT:    
      description: Scheduled In-Block Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateSLDT:    
      description: Scheduled Landing Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateSOBT:    
      description: Scheduled Off-Block Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateSTOT:    
      description: Scheduled Take-Off Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateTIBT:    
      description: Target In-Block Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateTLDT:    
      description: Target Landing Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateTOBT:    
      description: Target Off-Block Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateTSAT:    
      description: Target Start Up Approval Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateTTOT:    
      description: Target Take-Off Time    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    departsFromAirport:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: Reference to the departure airport entity    
      x-ngsi:    
        type: Relationship    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    flightNumber:    
      description: Flight identifier without information of airline    
      pattern: ^[A-Z0-9]{1,}$    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    flightNumberIATA:    
      description: IATA flight identifier    
      pattern: ^[A-Z0-9]{3,}$    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    flightNumberICAO:    
      description: ICAO flight identifier    
      pattern: ^[A-Z]{3}[A-Z0-9]{1,}$    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    flightType:    
      description: 'Flight type described as ICAO doc 4444 Appendix 2. Enum:''S, N, G, M, X'''    
      enum:    
        - S    
        - N    
        - G    
        - M    
        - X    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    hasAircraft:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: Reference to the aircraft entity    
      x-ngsi:    
        type: Relationship    
    hasAircraftModel:    
      anyOf:    
        - maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - format: uri    
          type: string    
      description: Reference to the aircraft model entity    
      x-ngsi:    
        type: Relationship    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    passengerCount:    
      description: Number of flight passengers    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Integer    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
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
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Flight    
      enum:    
        - Flight    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Aeronautics/blob/master/Flight/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Aeronautics/Flight/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### Flug NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Flight im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### Flug NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen Flug im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-v2 kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "flight-3732",  
    "type": "Flight",  
    "flightNumber": {  
        "type": "Text",  
        "value": "3732"  
    },  
    "flightNumberIATA": {  
        "type": "Text",  
        "value": "SN3732"  
    },  
    "flightNumberICAO": {  
        "type": "Text",  
        "value": "BEL3732"  
    },  
    "flightType": {  
        "type": "Text",  
        "value": "G"  
    },  
    "state": {  
        "type": "Text",  
        "value": "active"  
    },  
    "passengerCount": {  
        "type": "Number",  
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
</details>  
#### Flug NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen Flug im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Flight:flight-3732",  
    "type": "Flight",  
    "arrivesToAirport": "urn:ngsi-ld:Airline:airport-MAD",  
    "belongsToAirline": "urn:ngsi-ld:Airline:airline-SN",  
    "dateArrival": "2018-12-01T12:40:01.00Z",  
    "dateDeparture": "2018-12-01T10:40:01.00Z",  
    "dateSIBT": "2018-12-01T12:40:01.00Z",  
    "dateSLDT": "2018-12-01T12:35:01.00Z",  
    "dateSOBT": "2018-12-01T10:40:01.00Z",  
    "dateSTOT": "2018-12-01T10:45:01.00Z",  
    "departsFromAirport": "urn:ngsi-ld:Airline:airport-BMA",  
    "flightNumber": "3732",  
    "flightNumberIATA": "SN3732",  
    "flightNumberICAO": "BEL3732",  
    "flightType": "G",  
    "hasAircraft": "urn:ngsi-ld:Aircraft:aircraft-ABCDE",  
    "hasAircraftModel": "urn:ngsi-ld:AircraftModel:aircraftModel-AirbusA310-200",  
    "passengerCount": 25,  
    "state": "active",  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Aeronautics/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Flug NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen Flug im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Flight:flight-3732",  
    "type": "Flight",  
    "arrivesToAirport": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Airline:airport-MAD"  
    },  
    "belongsToAirline": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Airline:airline-SN"  
    },  
    "dateArrival": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2018-12-01T12:40:01.00Z"  
        }  
    },  
    "dateDeparture": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2018-12-01T10:40:01.00Z"  
        }  
    },  
    "dateSIBT": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2018-12-01T12:40:01.00Z"  
        }  
    },  
    "dateSLDT": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2018-12-01T12:35:01.00Z"  
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
    "departsFromAirport": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Airline:airport-BMA"  
    },  
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
    "hasAircraft": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Aircraft:aircraft-ABCDE"  
    },  
    "hasAircraftModel": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:AircraftModel:aircraftModel-AirbusA310-200"  
    },  
    "passengerCount": {  
        "type": "Property",  
        "value": 25  
    },  
    "state": {  
        "type": "Property",  
        "value": "active"  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Aeronautics/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
