<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: AircraftModel    
======================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.Aeronautics/blob/master/AircraftModel/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Descripción de un modelo genérico de aeronave**    
versión: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local      
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `capacity[number]`: Número de plazas  . Model: [http://schema.org/Integer](http://schema.org/Integer)- `ceiling[number]`: Altitud máxima que puede alcanzar el modelo de avión en metros  . Model: [http://schema.org/Number](http://schema.org/Number)- `codeIATA[string]`: Tipo de avión IATA  . Model: [http://schema.org/Text](http://schema.org/Text)- `codeICAO[string]`: Tipo de aeronave OACI  . Model: [http://schema.org/Text](http://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `height[number]`: Altura del modelo de avión en metros  . Model: [http://schema.org/Number](http://schema.org/Number)- `id[*]`: Identificador único de la entidad  - `length[number]`: Longitud del modelo de avión en metros  . Model: [http://schema.org/Number](http://schema.org/Number)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `maximumAllowedFuel[number]`: Combustible máximo del avión en kilogramos  . Model: [http://schema.org/Number](http://schema.org/Number)- `maximumAllowedSpeed[number]`:  Velocidad máxima del avión en kilómetros por hora  . Model: [http://schema.org/Number](http://schema.org/Number)- `mtow[number]`:  Peso máximo al despegue del avión en kilogramos  . Model: [http://schema.org/Number](http://schema.org/Number)- `name[string]`: El nombre de este artículo  - `numberOfEngines[number]`: Número de motores  . Model: [http://schema.org/Integer](http://schema.org/Integer)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Tipo de entidad NGSI. Tiene que ser AircraftModel  - `wingSpan[number]`: Envergadura del modelo de avión en metros  . Model: [http://schema.org/Number](http://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
La entidad AircraftModel contiene una descripción de un modelo genérico de aeronave con los parámetros estándar utilizados por la industria aeronáutica.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
AircraftModel:      
  description: A description of a generic aircraft model      
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
    capacity:      
      description: Number of seatings      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/Integer      
        type: Property      
    ceiling:      
      description: Maximum altitude the aircraft model can reach in metres      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: metres      
    codeIATA:      
      description: IATA aircraft type      
      pattern: ^[A-Z0-9]{3}$      
      type: string      
      x-ngsi:      
        model: http://schema.org/Text      
        type: Property      
    codeICAO:      
      description: ICAO aircraft type      
      pattern: ^[A-Z]{1}[A-Z0-9]{3}$      
      type: string      
      x-ngsi:      
        model: http://schema.org/Text      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    height:      
      description: Aircraft model height in metres      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: metres      
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
    length:      
      description: Aircraft model length in metres      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: metres      
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
    maximumAllowedFuel:      
      description: Aircraft maximum fuel in kilograms      
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
        units: kilometers per hour      
    mtow:      
      description: ' Aircraft maximum takeoff weight in kilograms'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: kilograms      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    numberOfEngines:      
      description: Number of engines      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: http://schema.org/Integer      
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
    type:      
      description: NGSI Entity type. It has to be AircraftModel      
      enum:      
        - AircraftModel      
      type: string      
      x-ngsi:      
        type: Property      
    wingSpan:      
      description: Aircraft model wingspan in metres      
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
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Aeronautics/blob/master/AircraftModel/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Aeronautics/AircraftModel/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Ejemplo de carga útil    
#### AircraftModel NGSI-v2 key-values Ejemplo    
Aquí hay un ejemplo de un AircraftModel en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
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
</details>    
#### AircraftModel NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de un AircraftModel en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "aircraftModel-AirbusA310-200",  
  "type": "AircraftModel",  
  "codeIATA": {  
    "type": "Text",  
    "value": "312"  
  },  
  "codeICAO": {  
    "type": "Text",  
    "value": "A310"  
  },  
  "name": {  
    "type": "Text",  
    "value": "Airbus A310-200"  
  },  
  "length": {  
    "type": "Number",  
    "value": 46.66  
  },  
  "wingSpan": {  
    "type": "Number",  
    "value": 43.9  
  },  
  "height": {  
    "type": "Number",  
    "value": 15.8  
  },  
  "mtow": {  
    "type": "Number",  
    "value": 144000  
  },  
  "maximumAllowedSpeed": {  
    "type": "Number",  
    "value": 850  
  },  
  "maximumAllowedFuel": {  
    "type": "Number",  
    "value": 47940  
  },  
  "ceiling": {  
    "type": "Number",  
    "value": 12527  
  },  
  "numberOfEngines": {  
    "type": "Number",  
    "value": 12527  
  },  
  "capacity": {  
    "type": "Number",  
    "value": 12527  
  }  
}  
```  
</details>    
#### AircraftModel NGSI-LD key-values Ejemplo    
Aquí hay un ejemplo de un AircraftModel en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AircraftModel:aircraftModel-AirbusA310-200",  
  "type": "AircraftModel",  
  "capacity": 150,  
  "ceiling": 12527,  
  "codeIATA": "312",  
  "codeICAO": "A310",  
  "height": 15.8,  
  "length": 46.66,  
  "maximumAllowedFuel": 47940,  
  "maximumAllowedSpeed": 850,  
  "mtow": 144000,  
  "name": "Airbus A310-200",  
  "numberOfEngines": 4,  
  "wingSpan": 43.9,  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Aeronautics/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### AircraftModel NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de un AircraftModel en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:AircraftModel:aircraftModel-AirbusA310-200",  
    "type": "AircraftModel",  
    "capacity": {  
        "type": "Property",  
        "value": 150  
    },  
    "ceiling": {  
        "type": "Property",  
        "value": 12527  
    },  
    "codeIATA": {  
        "type": "Property",  
        "value": "312"  
    },  
    "codeICAO": {  
        "type": "Property",  
        "value": "A310"  
    },  
    "height": {  
        "type": "Property",  
        "value": 15.8  
    },  
    "length": {  
        "type": "Property",  
        "value": 46.66  
    },  
    "maximumAllowedFuel": {  
        "type": "Property",  
        "value": 47940  
    },  
    "maximumAllowedSpeed": {  
        "type": "Property",  
        "value": 850  
    },  
    "mtow": {  
        "type": "Property",  
        "value": 144000  
    },  
    "name": {  
        "type": "Property",  
        "value": "Airbus A310-200"  
    },  
    "numberOfEngines": {  
        "type": "Property",  
        "value": 4  
    },  
    "wingSpan": {  
        "type": "Property",  
        "value": 43.9  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
