# IoT Sensor Data Ingestion to InfluxDB
This repository demonstrates how to ingest IoT sensor data into influxdb using Python3.12.

### Prerequisites

1. Install and run influxDB(v2.x).
2. Install Python 3.7 or later.
3. Install the official InfluxDB Python client library.
   
### Configuration
1. Set up an InfluxDB bucket and organization.
2. Obtain the InfluxDB API token from the InfluxDB UI.
3. Update the following variables in the script with your configuration:
   i)   url: URL of your InfluxDB instance (e.g., http://localhost:8086).
   ii)  token: Your InfluxDB API token.
   iii)  org: Your organization name.
   iv)   bucket: Your bucket name.

### Steps to execute the project
   
1. Ensure your InfluxDB
2. Execute the script to ingest data.
3. Log in to the InfluxDB web interface.
4. Navigate to the Data Explorer and query your bucket to confirm the data ingestion.
