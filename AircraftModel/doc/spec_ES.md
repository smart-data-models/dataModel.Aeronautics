Entidad: AircraftModel  
======================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Aeronautics/blob/master/AircraftModel/LICENSE.md)  
Descripción global: **Una descripción de un modelo genérico de avión**  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `capacity`: Número de asientos  - `ceiling`: Altitud máxima que el modelo de avión puede alcanzar en metros  - `codeIATA`: Tipo de avión de la IATA  - `codeICAO`: Tipo de aeronave de la OACI  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `height`: Altura del modelo de avión en metros  - `id`: Identificador único de la entidad  - `length`: Longitud del modelo de avión en metros  - `location`:   - `maximumAllowedFuel`: Combustible máximo de la aeronave en kilogramos  - `maximumAllowedSpeed`:  La velocidad máxima de los aviones en kilómetros por hora  - `mtow`:  Peso máximo de despegue de la aeronave en kilogramos  - `name`: El nombre de este artículo.  - `numberOfEngines`: Número de motores  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `type`: Tipo de entidad NGSI. Tiene que ser AircraftModel  - `wingSpan`: La envergadura del modelo de avión en metros    
Propiedades requeridas  
- `id`  - `name`  - `type`  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
## Ejemplo de cargas útiles  
#### AviónModelo NGSI V2 valores clave Ejemplo  
Aquí hay un ejemplo de un modelo de avión en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
#### AircraftModel NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de un AircraftModel en formato JSON como normalizado. Es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
#### AircraftModel NGSI-LD key-values Example  
Aquí hay un ejemplo de un modelo de avión en formato JSON-LD como valores clave. Es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
#### AircraftModel NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de un AircraftModel en formato JSON-LD normalizado. Es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
