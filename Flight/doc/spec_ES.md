<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: Vuelo    
==============<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.Aeronautics/blob/master/Flight/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Descripción de un vuelo genérico**    
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
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivesToAirport[*]`: Referencia a la entidad del aeropuerto de llegada  - `belongsToAirline[*]`: Referencia a la entidad de la compañía aérea  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateAIBT[date-time]`: Tiempo real en bloque  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateALDT[date-time]`: Tiempo real de aterrizaje  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAOBT[date-time]`: Tiempo real fuera de bloque  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateATO[date-time]`: Tiempo real superado  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateATOT[date-time]`: Tiempo real de despegue  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAXIT[date-time]`: Hora real de llegada  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAXOT[date-time]`: Tiempo real de salida en taxi  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateArrival[date-time]`: Fecha de llegada del vuelo  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCIBT[date-time]`: Tiempo en bloque calculado  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCLDT[date-time]`: Tiempo de aterrizaje calculado  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCOBT[date-time]`: Tiempo calculado fuera de bloque  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCTO[date-time]`: Tiempo calculado  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCTOT[date-time]`: Tiempo de despegue calculado  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateDeparture[date-time]`: Fecha de salida del vuelo  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEIBT[date-time]`: Tiempo estimado en bloque  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateELDT[date-time]`: Tiempo estimado de aterrizaje  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEOBT[date-time]`: Tiempo estimado fuera de bloque  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateETO[date-time]`: Tiempo estimado  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateETOT[date-time]`: Tiempo estimado de despegue  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEXIT[date-time]`: Hora estimada de llegada  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEXOT[date-time]`: Tiempo estimado de salida en taxi  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `dateSIBT[date-time]`: Tiempo en bloque programado  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSLDT[date-time]`: Hora prevista de aterrizaje  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSOBT[date-time]`: Tiempo de descanso programado  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSTOT[date-time]`: Hora programada de despegue  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTIBT[date-time]`: Tiempo objetivo en bloque  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTLDT[date-time]`: Tiempo objetivo de aterrizaje  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTOBT[date-time]`: Tiempo objetivo fuera de bloque  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTSAT[date-time]`: Plazo de aprobación de la puesta en marcha  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTTOT[date-time]`: Hora objetivo de despegue  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `departsFromAirport[*]`: Referencia a la entidad del aeropuerto de salida  - `description[string]`: Descripción de este artículo  - `flightNumber[string]`: Identificador de vuelo sin información de la compañía aérea  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightNumberIATA[string]`: Identificador de vuelo IATA  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightNumberICAO[string]`: Identificador de vuelo OACI  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightType[string]`: Tipo de vuelo descrito según el doc. 4444, apéndice 2, de la OACI. Enum:'S, N, G, M, X'  . Model: [http://schema.org/Text](http://schema.org/Text)- `hasAircraft[*]`: Referencia a la entidad de la aeronave  - `hasAircraftModel[*]`: Referencia a la entidad modelo de la aeronave  - `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `passengerCount[number]`: Número de pasajeros  . Model: [http://schema.org/Integer](http://schema.org/Integer)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `state[string]`: Estado actual del vuelo. Enum:'programado, activo, desconocido, redirigido, aterrizado, desviado, cancelado'.  . Model: [http://schema.org/Text](http://schema.org/Text)- `type[string]`: Tipo de entidad NGSI. Tiene que ser Vuelo  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
La entidad Vuelo contiene la descripción de un vuelo genérico con los parámetros estándar utilizados por la industria aérea. Este modelo se basa en las especificaciones publicadas por los principales organismos del sector, como [EUROCONTROL](https://www.eurocontrol.int/), [ICAO](https://www.icao.int/) e [IATA](https://www.iata.org/).    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
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
## Ejemplo de carga útil    
#### Vuelo NGSI-v2 key-values Ejemplo    
Aquí hay un ejemplo de un Vuelo en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
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
#### Vuelo NGSI-v2 normalizado Ejemplo    
Aquí hay un ejemplo de un Vuelo en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
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
#### Vuelo NGSI-LD valores-clave Ejemplo    
Aquí hay un ejemplo de un Vuelo en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
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
#### Vuelo NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de un Vuelo en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
