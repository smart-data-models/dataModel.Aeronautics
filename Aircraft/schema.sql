/* (Beta) Export of data model Aircraft of the subject dataModel.Aeronautics for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Aircraft_type AS ENUM ('Aircraft');
CREATE TABLE Aircraft (address JSON, alternateName TEXT, areaServed TEXT, dataProvider TEXT, dateCreated TIMESTAMP, dateIssued TIMESTAMP, dateModified TIMESTAMP, description TEXT, heading NUMERIC, isOnGround BOOLEAN, name TEXT, owner JSON, registration TEXT, source TEXT, speed NUMERIC, type Aircraft_type, verticalSpeed NUMERIC);