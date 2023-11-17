<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 비행    
=======<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Aeronautics/blob/master/Flight/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **일반 항공편에 대한 설명**    
버전: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `arrivesToAirport[*]`: 도착 공항 법인에 대한 참조  - `belongsToAirline[*]`: 항공사 법인에 대한 참조  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateAIBT[date-time]`: 실제 블록 내 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateALDT[date-time]`: 실제 착륙 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAOBT[date-time]`: 실제 오프 블록 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateATO[date-time]`: 실제 시간 초과  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateATOT[date-time]`: 실제 이륙 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAXIT[date-time]`: 실제 택시 탑승 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateAXOT[date-time]`: 실제 택시 배차 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateArrival[date-time]`: 항공편 도착 날짜  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCIBT[date-time]`: 블록 내 시간 계산  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCLDT[date-time]`: 계산된 착륙 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCOBT[date-time]`: 계산된 오프 블록 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCTO[date-time]`: 계산된 시간 초과  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCTOT[date-time]`: 계산된 이륙 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateDeparture[date-time]`: 항공편 출발일  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEIBT[date-time]`: 예상 인블록 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateELDT[date-time]`: 예상 착륙 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEOBT[date-time]`: 예상 오프블록 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateETO[date-time]`: 예상 시간 초과  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateETOT[date-time]`: 예상 이륙 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEXIT[date-time]`: 예상 택시 도착 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateEXOT[date-time]`: 예상 택시 하차 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateSIBT[date-time]`: 예약된 블록 내 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSLDT[date-time]`: 예약된 착륙 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSOBT[date-time]`: 예약된 오프 블록 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateSTOT[date-time]`: 예약된 이륙 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTIBT[date-time]`: 목표 인블록 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTLDT[date-time]`: 목표 착륙 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTOBT[date-time]`: 목표 오프블록 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTSAT[date-time]`: 목표 시작 승인 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateTTOT[date-time]`: 목표 이륙 시간  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `departsFromAirport[*]`: 출발 공항 법인에 대한 참조  - `description[string]`: 이 항목에 대한 설명  - `flightNumber[string]`: 항공사 정보가 없는 항공편 식별자  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightNumberIATA[string]`: IATA 항공편 식별자  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightNumberICAO[string]`: ICAO 비행 식별자  . Model: [http://schema.org/Text](http://schema.org/Text)- `flightType[string]`: ICAO 문서 4444 부록 2에 설명된 비행 유형입니다. 열거형:'S, N, G, M, X'  . Model: [http://schema.org/Text](http://schema.org/Text)- `hasAircraft[*]`: 항공기 엔티티에 대한 참조  - `hasAircraftModel[*]`: 항공기 모델 엔티티에 대한 참조  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `passengerCount[number]`: 항공편 승객 수  . Model: [http://schema.org/Integer](http://schema.org/Integer)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `state[string]`: 항공편의 현재 상태. Enum:'예정, 활성, 알 수 없음, 리디렉션, 착륙, 우회, 취소'  . Model: [http://schema.org/Text](http://schema.org/Text)- `type[string]`: NGSI 엔티티 유형. 항공편이어야 합니다.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
항공편 엔티티에는 항공 업계에서 사용하는 표준 매개 변수가 있는 일반 항공편에 대한 설명이 포함되어 있습니다. 이 모델은 [EUROCONTROL](https://www.eurocontrol.int/), [ICAO](https://www.icao.int/) 및 [IATA](https://www.iata.org/)와 같은 업계의 주요 기관에서 발행한 사양을 기반으로 합니다.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
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
## 페이로드 예시    
#### 비행 NGSI-v2 키 값 예시    
다음은 JSON-LD 형식의 항공편을 키값으로 사용하는 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### 비행 NGSI-v2 정규화 예시    
다음은 정규화된 JSON-LD 형식의 항공편 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### 항공편 NGSI-LD 키 값 예시    
다음은 JSON-LD 형식의 항공편을 키값으로 사용하는 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### 비행 NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 항공편 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
