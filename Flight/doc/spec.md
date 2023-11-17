<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: Flight    
==============<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.Aeronautics/blob/master/Flight/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **A description of a generic flight**    
version: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## List of properties    
<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>    
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government      
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivesToAirport[*]`: Reference to the arrival airport entity  - `belongsToAirline[*]`: Reference to the airline entity  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateAIBT[date-time]`: Actual In-Block Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateALDT[date-time]`: Actual Landing Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAOBT[date-time]`: Actual Off-Block Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateATO[date-time]`: Actual Time Over  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateATOT[date-time]`: Actual Take-Off Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAXIT[date-time]`: Actual Taxi-In Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAXOT[date-time]`: Actual Taxi-Out Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateArrival[date-time]`: Arrival date of the flight  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCIBT[date-time]`: Calculated In-Block Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCLDT[date-time]`: Calculated Landing Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCOBT[date-time]`: Calculated Off-Block Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCTO[date-time]`: Calculated Time Over  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCTOT[date-time]`: Calculated Take-Off Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateDeparture[date-time]`: Departure date of the flight  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEIBT[date-time]`: Estimated In-Block Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateELDT[date-time]`: Estimated Landing Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEOBT[date-time]`: Estimated Off-Block Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateETO[date-time]`: Estimated Time Over  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateETOT[date-time]`: Estimated Take-Off Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEXIT[date-time]`: Estimated Taxi-In Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEXOT[date-time]`: Estimated Taxi-Out Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `dateSIBT[date-time]`: Scheduled In-Block Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSLDT[date-time]`: Scheduled Landing Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSOBT[date-time]`: Scheduled Off-Block Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSTOT[date-time]`: Scheduled Take-Off Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTIBT[date-time]`: Target In-Block Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTLDT[date-time]`: Target Landing Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTOBT[date-time]`: Target Off-Block Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTSAT[date-time]`: Target Start Up Approval Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTTOT[date-time]`: Target Take-Off Time  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `departsFromAirport[*]`: Reference to the departure airport entity  - `description[string]`: A description of this item  - `flightNumber[string]`: Flight identifier without information of airline  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightNumberIATA[string]`: IATA flight identifier  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightNumberICAO[string]`: ICAO flight identifier  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightType[string]`: Flight type described as ICAO doc 4444 Appendix 2. Enum:'S, N, G, M, X'  . Model: [http://schema.org/Text](http://schema.org/Text)- `hasAircraft[*]`: Reference to the aircraft entity  - `hasAircraftModel[*]`: Reference to the aircraft model entity  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `passengerCount[number]`: Number of flight passengers  . Model: [http://schema.org/Integer](http://schema.org/Integer)- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `state[string]`: Current state of the flight. Enum:'scheduled, active, unknown, redirected, landed, diverted, cancelled'  . Model: [http://schema.org/Text](http://schema.org/Text)- `type[string]`: NGSI Entity type. It has to be Flight  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Required properties    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Flight entity contains a description of a generic flight with the standard parameters used by the airline industry. This model is based on specifications published by the main organisms of the industry such us [EUROCONTROL](https://www.eurocontrol.int/), [ICAO](https://www.icao.int/) and [IATA](https://www.iata.org/).    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Data Model description of properties    
Sorted alphabetically (click for details)    
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
## Example payloads      
#### Flight NGSI-v2 key-values Example      
Here is an example of a Flight in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
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
#### Flight NGSI-v2 normalized Example      
Here is an example of a Flight in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
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
    "type": "Text",  
    "value": "aircraft-ABCDE"  
  },  
  "hasAircraftModel": {  
    "type": "Text",  
    "value": "aircraftModel-AirbusA310-200"  
  },  
  "departsFromAirport": {  
    "type": "Text",  
    "value": "airport-BMA"  
  },  
  "arrivesToAirport": {  
    "type": "Text",  
    "value": "airport-MAD"  
  },  
  "belongsToAirline": {  
    "type": "Text",  
    "value": "airline-SN"  
  }  
}  
```  
</details>    
#### Flight NGSI-LD key-values Example      
Here is an example of a Flight in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
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
#### Flight NGSI-LD normalized Example      
Here is an example of a Flight in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
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
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
