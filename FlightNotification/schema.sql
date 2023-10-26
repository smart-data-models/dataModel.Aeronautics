/* (Beta) Export of data model FlightNotification of the subject dataModel.Aeronautics for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE state_type AS ENUM ('active','inactive','completed','unknown');CREATE TYPE FlightNotification_type AS ENUM ('FlightNotification');
CREATE TABLE FlightNotification (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateIssued TIMESTAMP, dateModified TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, location JSON, name TEXT, owner JSON, seeAlso JSON, source TEXT, state state_type, type FlightNotification_type);