from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class FlightType(Enum):
    S = 'S'
    N = 'N'
    G = 'G'
    M = 'M'
    X = 'X'


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class State(Enum):
    scheduled = 'scheduled'
    active = 'active'
    unknown = 'unknown'
    redirected = 'redirected'
    landed = 'landed'
    diverted = 'diverted'
    cancelled = 'cancelled'


class Type6(Enum):
    Flight = 'Flight'


class Flight(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    arrivesToAirport: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Reference to the arrival airport entity')
    belongsToAirline: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Reference to the airline entity')
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateAIBT: Optional[AwareDatetime] = Field(None, description='Actual In-Block Time')
    dateALDT: Optional[AwareDatetime] = Field(None, description='Actual Landing Time')
    dateAOBT: Optional[AwareDatetime] = Field(None, description='Actual Off-Block Time')
    dateATO: Optional[AwareDatetime] = Field(None, description='Actual Time Over')
    dateATOT: Optional[AwareDatetime] = Field(None, description='Actual Take-Off Time')
    dateAXIT: Optional[AwareDatetime] = Field(None, description='Actual Taxi-In Time')
    dateAXOT: Optional[AwareDatetime] = Field(None, description='Actual Taxi-Out Time')
    dateArrival: Optional[AwareDatetime] = Field(
        None, description='Arrival date of the flight'
    )
    dateCIBT: Optional[AwareDatetime] = Field(
        None, description='Calculated In-Block Time'
    )
    dateCLDT: Optional[AwareDatetime] = Field(
        None, description='Calculated Landing Time'
    )
    dateCOBT: Optional[AwareDatetime] = Field(
        None, description='Calculated Off-Block Time'
    )
    dateCTO: Optional[AwareDatetime] = Field(None, description='Calculated Time Over')
    dateCTOT: Optional[AwareDatetime] = Field(
        None, description='Calculated Take-Off Time'
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateDeparture: Optional[AwareDatetime] = Field(
        None, description='Departure date of the flight'
    )
    dateEIBT: Optional[AwareDatetime] = Field(
        None, description='Estimated In-Block Time'
    )
    dateELDT: Optional[AwareDatetime] = Field(
        None, description='Estimated Landing Time'
    )
    dateEOBT: Optional[AwareDatetime] = Field(
        None, description='Estimated Off-Block Time'
    )
    dateETO: Optional[AwareDatetime] = Field(None, description='Estimated Time Over')
    dateETOT: Optional[AwareDatetime] = Field(
        None, description='Estimated Take-Off Time'
    )
    dateEXIT: Optional[AwareDatetime] = Field(
        None, description='Estimated Taxi-In Time'
    )
    dateEXOT: Optional[AwareDatetime] = Field(
        None, description='Estimated Taxi-Out Time'
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    dateSIBT: Optional[AwareDatetime] = Field(
        None, description='Scheduled In-Block Time'
    )
    dateSLDT: Optional[AwareDatetime] = Field(
        None, description='Scheduled Landing Time'
    )
    dateSOBT: Optional[AwareDatetime] = Field(
        None, description='Scheduled Off-Block Time'
    )
    dateSTOT: Optional[AwareDatetime] = Field(
        None, description='Scheduled Take-Off Time'
    )
    dateTIBT: Optional[AwareDatetime] = Field(None, description='Target In-Block Time')
    dateTLDT: Optional[AwareDatetime] = Field(None, description='Target Landing Time')
    dateTOBT: Optional[AwareDatetime] = Field(None, description='Target Off-Block Time')
    dateTSAT: Optional[AwareDatetime] = Field(
        None, description='Target Start Up Approval Time'
    )
    dateTTOT: Optional[AwareDatetime] = Field(None, description='Target Take-Off Time')
    departsFromAirport: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Reference to the departure airport entity')
    description: Optional[str] = Field(None, description='A description of this item')
    flightNumber: Optional[constr(pattern=r'^[A-Z0-9]{1,}$')] = Field(
        None, description='Flight identifier without information of airline'
    )
    flightNumberIATA: Optional[constr(pattern=r'^[A-Z0-9]{3,}$')] = Field(
        None, description='IATA flight identifier'
    )
    flightNumberICAO: Optional[constr(pattern=r'^[A-Z]{3}[A-Z0-9]{1,}$')] = Field(
        None, description='ICAO flight identifier'
    )
    flightType: Optional[FlightType] = Field(
        None,
        description="Flight type described as ICAO doc 4444 Appendix 2. Enum:'S, N, G, M, X'",
    )
    hasAircraft: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Reference to the aircraft entity')
    hasAircraftModel: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Reference to the aircraft model entity')
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    passengerCount: Optional[confloat(ge=0.0)] = Field(
        None, description='Number of flight passengers'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    state: Optional[State] = Field(
        None,
        description="Current state of the flight. Enum:'scheduled, active, unknown, redirected, landed, diverted, cancelled'",
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be Flight'
    )
