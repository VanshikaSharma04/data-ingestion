# data-ingestion
This repository contains data ingestion into influxdbv2.7.10 using Python3.12.

### Prerequisites

1. Install the InfluxDB Python library
2. Make sure that INfluxDB is active.Visit http://localhost:8086.
   
### Steps to write data to InfluxDB with Python
   
1. In your Python Interactive Shell, import the InfluxDB client library.
2. Determine the variables - bucket, organization, and token.
3. Initiate the client.Pass in the named parameters:url, org, and token.
4. The InfluxDBClient object contains a write_api method to configure the writer object.
5. Create a point object and write the data to InfluxDB using the write method of the API writer 
   object. This method requisite three parameters:bucket, org, and record.
