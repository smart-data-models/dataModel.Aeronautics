Entity: AircraftModel  
=====================  
[Open License](https://github.com/smart-data-models//dataModel.Aeronautics/blob/master/AircraftModel/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **A description of a generic aircraft model**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `capacity`: Number of seatings  - `ceiling`: Maximum altitude the aircraft model can reach in metres  - `codeIATA`: IATA aircraft type  - `codeICAO`: ICAO aircraft type  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `height`: Aircraft model height in metres  - `id`: Unique identifier of the entity  - `length`: Aircraft model length in metres  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `maximumAllowedFuel`: Aircraft maximum fuel in kilograms  - `maximumAllowedSpeed`:  Aircraft maximum speed in kilometers per hour  - `mtow`:  Aircraft maximum takeoff weight in kilograms  - `name`: The name of this item.  - `numberOfEngines`: Number of engines  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI Entity type. It has to be AircraftModel  - `wingSpan`: Aircraft model wingspan in metres    
Required properties  
- `id`  - `name`  - `type`    
AircraftModel entity contains a description of a generic aircraft model with the standard parameters used by the airline industry.  
## Data Model description of properties  
Sorted alphabetically (click for details)  
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
    capacity:    
      description: 'Number of seatings'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Integer    
        type: Property    
    ceiling:    
      description: 'Maximum altitude the aircraft model can reach in metres'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: metres    
    codeIATA:    
      description: 'IATA aircraft type'    
      pattern: ^[A-Z0-9]{3}$    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    codeICAO:    
      description: 'ICAO aircraft type'    
      pattern: ^[A-Z]{1}[A-Z0-9]{3}$    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    height:    
      description: 'Aircraft model height in metres'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
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
      x-ngsi:    
        type: Property    
    length:    
      description: 'Aircraft model length in metres'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
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
      x-ngsi:    
        type: Geoproperty    
    maximumAllowedFuel:    
      description: 'Aircraft maximum fuel in kilograms'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: kilograms    
    maximumAllowedSpeed:    
      description: ' Aircraft maximum speed in kilometers per hour'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'kilometers per hour'    
    mtow:    
      description: ' Aircraft maximum takeoff weight in kilograms'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: kilograms    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    numberOfEngines:    
      description: 'Number of engines'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Integer    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *aircraftmodel_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
    type:    
      description: 'NGSI Entity type. It has to be AircraftModel'    
      enum:    
        - AircraftModel    
      type: string    
      x-ngsi:    
        type: Property    
    wingSpan:    
      description: 'Aircraft model wingspan in metres'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: metres    
  required:    
    - id    
    - type    
    - name    
  type: object    
```  
</details>    
## Example payloads    
#### AircraftModel NGSI-v2 key-values Example    
Here is an example of a AircraftModel in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### AircraftModel NGSI-v2 normalized Example    
Here is an example of a AircraftModel in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
Here is an example of a AircraftModel in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### AircraftModel NGSI-LD normalized Example    
Here is an example of a AircraftModel in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
