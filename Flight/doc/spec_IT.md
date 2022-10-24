<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Volo  
============<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Aeronautics/blob/master/Flight/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Descrizione di un volo generico**  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivesToAirport[*]`: Riferimento all'entità aeroporto di arrivo  - `belongsToAirline[*]`: Riferimento all'entità compagnia aerea  - `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateAIBT[string]`: Tempo effettivo di permanenza nel blocco  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateALDT[string]`: Tempo effettivo di atterraggio  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAOBT[string]`: Tempo effettivo fuori dal blocco  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateATO[string]`: Tempo effettivo di superamento  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateATOT[string]`: Tempo effettivo di decollo  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAXIT[string]`: Tempo effettivo di arrivo in taxi  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAXOT[string]`: Tempo effettivo di uscita in taxi  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateArrival[string]`: Data di arrivo del volo  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCIBT[string]`: Tempo in-blocco calcolato  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCLDT[string]`: Tempo di atterraggio calcolato  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCOBT[string]`: Tempo calcolato fuori dal blocco  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCTO[string]`: Tempo calcolato di superamento  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCTOT[string]`: Tempo di decollo calcolato  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateDeparture[string]`: Data di partenza del volo  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEIBT[string]`: Tempo stimato di permanenza nel blocco  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateELDT[string]`: Tempo stimato di atterraggio  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEOBT[string]`: Tempo stimato fuori dal blocco  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateETO[string]`: Tempo stimato di superamento  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateETOT[string]`: Tempo stimato di decollo  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEXIT[string]`: Tempo stimato di arrivo in taxi  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEXOT[string]`: Tempo stimato di uscita in taxi  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateSIBT[string]`: Tempo di permanenza programmata nel blocco  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSLDT[string]`: Orario di atterraggio previsto  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSOBT[string]`: Tempo programmato fuori dal blocco  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSTOT[string]`: Orario di decollo previsto  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTIBT[string]`: Tempo target in-block  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTLDT[string]`: Tempo di atterraggio target  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTOBT[string]`: Tempo target fuori dal blocco  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTSAT[string]`: Tempo di approvazione dell'avvio dell'obiettivo  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTTOT[string]`: Tempo di decollo previsto  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `departsFromAirport[*]`: Riferimento all'entità dell'aeroporto di partenza  - `description[string]`: Descrizione dell'articolo  - `flightNumber[string]`: Identificatore di volo senza informazioni sulla compagnia aerea  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightNumberIATA[string]`: Identificatore di volo IATA  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightNumberICAO[string]`: Identificatore di volo ICAO  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightType[string]`: Tipo di volo descritto come da documento ICAO 4444 Appendice 2. Enum: "S, N, G, M, X".  . Model: [http://schema.org/Text](http://schema.org/Text)- `hasAircraft[*]`: Riferimento all'entità aeromobile  - `hasAircraftModel[*]`: Riferimento all'entità del modello di aeromobile  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento.  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `passengerCount[integer]`: Numero di passeggeri del volo  . Model: [http://schema.org/Integer](http://schema.org/Integer)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `state[string]`: Stato attuale del volo. Enum:'programmato, attivo, sconosciuto, reindirizzato, atterrato, deviato, cancellato'.  . Model: [http://schema.org/Text](http://schema.org/Text)- `type[string]`: Tipo di entità NGSI. Deve essere Volo  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
L'entità Volo contiene una descrizione di un volo generico con i parametri standard utilizzati dall'industria aerea. Questo modello si basa sulle specifiche pubblicate dai principali organismi del settore, come [EUROCONTROL](https://www.eurocontrol.int/), [ICAO](https://www.icao.int/) e [IATA](https://www.iata.org/).  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Flight:    
  description: 'A description of a generic flight'    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
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
      description: 'Reference to the arrival airport entity'    
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
      description: 'Reference to the airline entity'    
      x-ngsi:    
        type: Relationship    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateAIBT:    
      description: 'Actual In-Block Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateALDT:    
      description: 'Actual Landing Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateAOBT:    
      description: 'Actual Off-Block Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateATO:    
      description: 'Actual Time Over'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateATOT:    
      description: 'Actual Take-Off Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateAXIT:    
      description: 'Actual Taxi-In Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateAXOT:    
      description: 'Actual Taxi-Out Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateArrival:    
      description: 'Arrival date of the flight'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateCIBT:    
      description: 'Calculated In-Block Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateCLDT:    
      description: 'Calculated Landing Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateCOBT:    
      description: 'Calculated Off-Block Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateCTO:    
      description: 'Calculated Time Over'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateCTOT:    
      description: 'Calculated Take-Off Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateDeparture:    
      description: 'Departure date of the flight'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateEIBT:    
      description: 'Estimated In-Block Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateELDT:    
      description: 'Estimated Landing Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateEOBT:    
      description: 'Estimated Off-Block Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateETO:    
      description: 'Estimated Time Over'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateETOT:    
      description: 'Estimated Take-Off Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateEXIT:    
      description: 'Estimated Taxi-In Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateEXOT:    
      description: 'Estimated Taxi-Out Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateSIBT:    
      description: 'Scheduled In-Block Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateSLDT:    
      description: 'Scheduled Landing Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateSOBT:    
      description: 'Scheduled Off-Block Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateSTOT:    
      description: 'Scheduled Take-Off Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateTIBT:    
      description: 'Target In-Block Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateTLDT:    
      description: 'Target Landing Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateTOBT:    
      description: 'Target Off-Block Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateTSAT:    
      description: 'Target Start Up Approval Time'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateTTOT:    
      description: 'Target Take-Off Time'    
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
      description: 'Reference to the departure airport entity'    
      x-ngsi:    
        type: Relationship    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    flightNumber:    
      description: 'Flight identifier without information of airline'    
      pattern: ^[A-Z0-9]{1,}$    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    flightNumberIATA:    
      description: 'IATA flight identifier'    
      pattern: ^[A-Z0-9]{3,}$    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    flightNumberICAO:    
      description: 'ICAO flight identifier'    
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
      description: 'Reference to the aircraft entity'    
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
      description: 'Reference to the aircraft model entity'    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
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
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *flight_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    passengerCount:    
      description: 'Number of flight passengers'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Integer    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
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
      description: 'NGSI Entity type. It has to be Flight'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
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
## Esempi di payload  
#### Volo NGSI-v2 valori-chiave Esempio  
Ecco un esempio di un volo in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### Volo NGSI-v2 normalizzato Esempio  
Ecco un esempio di un volo in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
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
#### Volo NGSI-LD valori-chiave Esempio  
Ecco un esempio di un volo in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### Volo NGSI-LD normalizzato Esempio  
Ecco un esempio di un volo in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
