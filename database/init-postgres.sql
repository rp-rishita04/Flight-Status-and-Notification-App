CREATE DATABASE flightstatus;
CREATE USER flightuser WITH ENCRYPTED PASSWORD 'flightpass';
GRANT ALL PRIVILEGES ON DATABASE flightstatus TO flightuser;
