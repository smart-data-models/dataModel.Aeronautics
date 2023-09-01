/* (Beta) Export of data model FlightNotification of the subject dataModel.Aeronautics for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE state_type AS ENUM ('active', 'inactive', 'completed', 'unknown');CREATE TYPE FlightNotification_type AS ENUM ('FlightNotification');
CREATE TABLE FlightNotification (address json, alternateName text, areaServed text, belongsToFlight text, dataProvider text, dateCreated timestamp, dateIssued timestamp, dateModified timestamp, description text, id text, location json, name text, owner json, seeAlso json, source text, state state_type, type FlightNotification_type);