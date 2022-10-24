<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティフライト  
==========<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Aeronautics/blob/master/Flight/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です。**一般的なフライトの説明**  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivesToAirport[*]`: 到着空港のエンティティへの参照  - `belongsToAirline[*]`: 航空会社のエンティティへの参照  - `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateAIBT[string]`: 実際のインブロック時間  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateALDT[string]`: 実際の着陸時間  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAOBT[string]`: 実際のオフ・ブロック時間  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateATO[string]`: 実際のタイムオーバー  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateATOT[string]`: 実際の離陸時間  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAXIT[string]`: 実際のタクシーインタイム  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAXOT[string]`: 実際のタクシー出動時間  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateArrival[string]`: フライトの到着日  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCIBT[string]`: 計算されたインブロック時間  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCLDT[string]`: 計算された着陸時間  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCOBT[string]`: 計算されたオフ・ブロック時間  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCTO[string]`: 計算されたタイムオーバー  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCTOT[string]`: 離陸時間の計算  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateDeparture[string]`: フライトの出発日  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEIBT[string]`: 推定インブロック時間  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateELDT[string]`: 着陸予定時刻  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEOBT[string]`: オフ・ブロックの推定時間  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateETO[string]`: 予想される時間  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateETOT[string]`: 離陸予定時刻  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEXIT[string]`: タクシー到着予定時刻  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEXOT[string]`: タクシー出庫予定時刻  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateSIBT[string]`: インブロック予定時間  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSLDT[string]`: 着陸予定時刻  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSOBT[string]`: オフ・ブロックの予定時間  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSTOT[string]`: 離陸予定時刻  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTIBT[string]`: ターゲットインブロック時間  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTLDT[string]`: 目標着陸時刻  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTOBT[string]`: 目標オフ・ブロック時間  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTSAT[string]`: 目標起動承認時間  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTTOT[string]`: 目標離陸時刻  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `departsFromAirport[*]`: 出発空港の実体への言及  - `description[string]`: このアイテムの説明  - `flightNumber[string]`: 航空会社の情報がないフライトの識別情報  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightNumberIATA[string]`: IATAフライト識別子  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightNumberICAO[string]`: ICAOフライト識別子  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightType[string]`: ICAO doc 4444 Appendix 2 として記述されたフライトタイプ。Enum:'S, N, G, M, X'の略。  . Model: [http://schema.org/Text](http://schema.org/Text)- `hasAircraft[*]`: 航空機の実体への参照  - `hasAircraftModel[*]`: 航空機モデルの実体への参照  - `id[*]`: エンティティの一意な識別子  - `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリスト  - `passengerCount[integer]`: 搭乗者数  . Model: [http://schema.org/Integer](http://schema.org/Integer)- `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `state[string]`: 現在のフライトの状態。Enum:'scheduled, active, unknown, redirected, landed, diverted, cancelled'（予定通り、アクティブ、不明、着陸、迂回、キャンセル  . Model: [http://schema.org/Text](http://schema.org/Text)- `type[string]`: NGSI Entity タイプ。これはフライトでなければなりません。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
フライトエンティティには、航空業界で使用される標準的なパラメータを持つ一般的なフライトの記述が含まれます。このモデルは、[EUROCONTROL](https://www.eurocontrol.int/), [ICAO](https://www.icao.int/) および [IATA](https://www.iata.org/) などの航空業界の主要機関が発行する仕様に基づいています。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
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
## ペイロードの例  
#### フライトNGSI-v2キーバリューの例  
ここでは、FlightをJSON-LD形式でkey-valuesとした場合の例を示す。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返される。  
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
#### フライト NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のFlightの例である。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### フライトNGSI-LDのキー値例  
ここでは、FlightをJSON-LD形式でkey-valuesとした場合の例を示します。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータが返されます。  
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
#### フライト NGSI-LD 正規化例  
以下は、正規化されたJSON-LD形式のFlightの例である。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
