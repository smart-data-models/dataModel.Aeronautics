<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : Vol    
============<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Aeronautics/blob/master/Flight/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Description d'un vol générique**    
version : 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.      
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivesToAirport[*]`: Référence à l'entité de l'aéroport d'arrivée  - `belongsToAirline[*]`: Référence à l'entité compagnie aérienne  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateAIBT[date-time]`: Temps réel dans le bloc  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateALDT[date-time]`: Heure d'atterrissage réelle  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAOBT[date-time]`: Temps réel hors bloc  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateATO[date-time]`: Temps réel dépassé  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateATOT[date-time]`: Heure de décollage réelle  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAXIT[date-time]`: Heure d'arrivée effective du taxi  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAXOT[date-time]`: Temps réel de sortie du taxi  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateArrival[date-time]`: Date d'arrivée du vol  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCIBT[date-time]`: Durée calculée dans le bloc  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCLDT[date-time]`: Heure d'atterrissage calculée  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCOBT[date-time]`: Temps hors bloc calculé  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCTO[date-time]`: Temps écoulé calculé  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCTOT[date-time]`: Heure de décollage calculée  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateDeparture[date-time]`: Date de départ du vol  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEIBT[date-time]`: Durée estimée du blocage  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateELDT[date-time]`: Heure d'atterrissage estimée  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEOBT[date-time]`: Estimation de la durée hors bloc  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateETO[date-time]`: Estimation du temps écoulé  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateETOT[date-time]`: Heure de décollage estimée  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEXIT[date-time]`: Estimation de l'heure d'arrivée des taxis  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEXOT[date-time]`: Estimation du temps de sortie en taxi  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `dateSIBT[date-time]`: Temps de blocage programmé  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSLDT[date-time]`: Heure d'atterrissage prévue  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSOBT[date-time]`: Temps hors bloc programmé  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSTOT[date-time]`: Heure de décollage prévue  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTIBT[date-time]`: Temps cible dans le bloc  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTLDT[date-time]`: Heure d'atterrissage visée  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTOBT[date-time]`: Temps hors bloc cible  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTSAT[date-time]`: Délai d'approbation du démarrage de l'objectif  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTTOT[date-time]`: Heure cible de décollage  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `departsFromAirport[*]`: Référence à l'entité de l'aéroport de départ  - `description[string]`: Une description de l'article  - `flightNumber[string]`: Identifiant de vol sans information sur la compagnie aérienne  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightNumberIATA[string]`: Identifiant de vol IATA  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightNumberICAO[string]`: Identifiant de vol OACI  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightType[string]`: Type de vol décrit dans le document 4444 de l'OACI, appendice 2. Enum : "S, N, G, M, X".  . Model: [http://schema.org/Text](http://schema.org/Text)- `hasAircraft[*]`: Référence à l'entité aéronef  - `hasAircraftModel[*]`: Référence à l'entité modèle d'aéronef  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `passengerCount[number]`: Nombre de passagers  . Model: [http://schema.org/Integer](http://schema.org/Integer)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `state[string]`: État actuel du vol. Enum : "prévu, actif, inconnu, redirigé, atterri, détourné, annulé  . Model: [http://schema.org/Text](http://schema.org/Text)- `type[string]`: Type d'entité NGSI. Il doit s'agir de Flight  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propriétés requises    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
L'entité "vol" contient une description d'un vol générique avec les paramètres standard utilisés par l'industrie du transport aérien. Ce modèle est basé sur les spécifications publiées par les principaux organismes du secteur tels que [EUROCONTROL](https://www.eurocontrol.int/), [ICAO](https://www.icao.int/) et [IATA](https://www.iata.org/).    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modèle de données description des propriétés    
Classés par ordre alphabétique (cliquez pour plus de détails)    
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
## Exemples de charges utiles    
#### Flight NGSI-v2 key-values Exemple    
Voici un exemple de vol au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
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
#### Vol NGSI-v2 normalisé Exemple    
Voici un exemple de vol au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
#### Valeurs clés de l'INS-LD pour le vol Exemple    
Voici un exemple de vol au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
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
#### Vol NGSI-LD normalisé Exemple    
Voici un exemple de vol au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
