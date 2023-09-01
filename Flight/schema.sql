/* (Beta) Export of data model Flight of the subject dataModel.Aeronautics for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE flightType_type AS ENUM ('S', 'N', 'G', 'M', 'X');CREATE TYPE state_type AS ENUM ('scheduled', 'active', 'unknown', 'redirected', 'landed', 'diverted', 'cancelled');CREATE TYPE Flight_type AS ENUM ('Flight');
CREATE TABLE Flight (address json, alternateName text, areaServed text, arrivesToAirport text, belongsToAirline text, dataProvider text, dateAIBT timestamp, dateALDT timestamp, dateAOBT timestamp, dateATO timestamp, dateATOT timestamp, dateAXIT timestamp, dateAXOT timestamp, dateArrival timestamp, dateCIBT timestamp, dateCLDT timestamp, dateCOBT timestamp, dateCTO timestamp, dateCTOT timestamp, dateCreated timestamp, dateDeparture timestamp, dateEIBT timestamp, dateELDT timestamp, dateEOBT timestamp, dateETO timestamp, dateETOT timestamp, dateEXIT timestamp, dateEXOT timestamp, dateModified timestamp, dateSIBT timestamp, dateSLDT timestamp, dateSOBT timestamp, dateSTOT timestamp, dateTIBT timestamp, dateTLDT timestamp, dateTOBT timestamp, dateTSAT timestamp, dateTTOT timestamp, departsFromAirport text, description text, flightNumber text, flightNumberIATA text, flightNumberICAO text, flightType flightType_type, hasAircraft text, hasAircraftModel text, id text, location json, name text, owner json, passengerCount integer, seeAlso json, source text, state state_type, type Flight_type);