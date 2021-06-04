Entity: Flight  
==============  
[Open License](https://github.com/smart-data-models//dataModel.Aeronautics/blob/master/Flight/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **A description of a generic flight**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `arrivesToAirport`: Reference to the arrival airport entity  - `belongsToAirline`: Reference to the airline entity  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateAIBT`: Actual In-Block Time  - `dateALDT`: Actual Landing Time  - `dateAOBT`: Actual Off-Block Time  - `dateATO`: Actual Time Over  - `dateATOT`: Actual Take-Off Time  - `dateAXIT`: Actual Taxi-In Time  - `dateAXOT`: Actual Taxi-Out Time  - `dateArrival`: Arrival date of the flight  - `dateCIBT`: Calculated In-Block Time  - `dateCLDT`: Calculated Landing Time  - `dateCOBT`: Calculated Off-Block Time  - `dateCTO`: Calculated Time Over  - `dateCTOT`: Calculated Take-Off Time  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateDeparture`: Departure date of the flight  - `dateEIBT`: Estimated In-Block Time  - `dateELDT`: Estimated Landing Time  - `dateEOBT`: Estimated Off-Block Time  - `dateETO`: Estimated Time Over  - `dateETOT`: Estimated Take-Off Time  - `dateEXIT`: Estimated Taxi-In Time  - `dateEXOT`: Estimated Taxi-Out Time  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `dateSIBT`: Scheduled In-Block Time  - `dateSLDT`: Scheduled Landing Time  - `dateSOBT`: Scheduled Off-Block Time  - `dateSTOT`: Scheduled Take-Off Time  - `dateTIBT`: Target In-Block Time  - `dateTLDT`: Target Landing Time  - `dateTOBT`: Target Off-Block Time  - `dateTSAT`: Target Start Up Approval Time  - `dateTTOT`: Target Take-Off Time  - `departsFromAirport`: Reference to the departure airport entity  - `description`: A description of this item  - `flightNumber`: Flight identifier without information of airline  - `flightNumberIATA`: IATA flight identifier  - `flightNumberICAO`: ICAO flight identifier  - `flightType`: Flight type described as ICAO doc 4444 Appendix 2. Enum:'S, N, G, M, X'  - `hasAircraft`: Reference to the aircraft entity  - `hasAircraftModel`: Reference to the aircraft model entity  - `id`: Unique identifier of the entity  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `passengerCount`: Number of flight passengers  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `state`: Current state of the flight. Enum:'scheduled, active, unknown, redirected, landed, diverted, cancelled'  - `type`: NGSI Entity type. It has to be Flight    
Required properties  
- `id`  - `type`    
Flight entity contains a description of a generic flight with the standard parameters used by the airline industry. This model is based on specifications published by the main organisms of the industry such us [EUROCONTROL](https://www.eurocontrol.int/), [ICAO](https://www.icao.int/) and [IATA](https://www.iata.org/).  
## Data Model description of properties  
Sorted alphabetically (click for details)  
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
## Example payloads    
#### Flight NGSI-v2 key-values Example    
Here is an example of a Flight in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### Flight NGSI-v2 normalized Example    
Here is an example of a Flight in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
#### Flight NGSI-LD key-values Example    
Here is an example of a Flight in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### Flight NGSI-LD normalized Example    
Here is an example of a Flight in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
