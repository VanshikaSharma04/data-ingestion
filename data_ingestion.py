import influxdb_client, time
from influxdb_client import InfluxDBClient, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# Authentication details for the InfluxDB instance
token = "INSERT_YOUR_TOKEN_HERE"
org = "workspace"  
url = "http://localhost:8086"  

# Initialize the InfluxDB client
write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket = "bucket_new"  # Bucket where the data will be stored

# Configure the write API with synchronous writing mode
write_api = write_client.write_api(write_options=SYNCHRONOUS)

# Generate a list of IoT sensor data points in InfluxDB's line protocol format
# Each data point includes:
# - Measurement ("home")
# - Tag ("room" with values like "living_room" or "kitchen")
# - Field values (temperature, humidity, and CO level)
# - Timestamp (current time in nanoseconds)
data = [
    f"home,room=living_room temp=21.1,hum=35.9,co=0i {int(time.time() * 1_000_000_000)}",
    f"home,room=kitchen temp=21.0,hum=35.9,co=0i {int(time.time() * 1_000_000_000)}",
    f"home,room=living_room temp=21.4,hum=35.9,co=0i {int(time.time() * 1_000_000_000)}",
    f"home,room=kitchen temp=23.0,hum=36.2,co=0i {int(time.time() * 1_000_000_000)}",
    f"home,room=living_room temp=21.8,hum=36.0,co=0i {int(time.time() * 1_000_000_000)}",
    f"home,room=kitchen temp=22.7,hum=36.1,co=0i {int(time.time() * 1_000_000_000)}",
    f"home,room=living_room temp=22.2,hum=36.0,co=0i {int(time.time() * 1_000_000_000)}",
    f"home,room=kitchen temp=22.4,hum=36.0,co=1i {int(time.time() * 1_000_000_000)}",
    f"home,room=living_room temp=22.2,hum=35.9,co=0i {int(time.time() * 1_000_000_000)}",
    f"home,room=kitchen temp=22.5,hum=36.0,co=0i {int(time.time() * 1_000_000_000)}",
    f"home,room=living_room temp=22.4,hum=36.0,co=0i {int(time.time() * 1_000_000_000)}",
    f"home,room=kitchen temp=22.8,hum=35.5,co=0i {int(time.time() * 1_000_000_000)}",
    f"home,room=living_room temp=22.3,hum=35.9,co=2i {int(time.time() * 1_000_000_000)}",
    f"home,room=kitchen temp=22.8,hum=37.9,co=3i {int(time.time() * 1_000_000_000)}",
    f"home,room=living_room temp=22.3,hum=35.9,co=17i {int(time.time() * 1_000_000_000)}",
    f"home,room=kitchen temp=22.7,hum=36.1,co=12i {int(time.time() * 1_000_000_000)}",
    f"home,room=living_room temp=22.4,hum=30.9,co=7i {int(time.time() * 1_000_000_000)}",
    f"home,room=kitchen temp=22.4,hum=35.9,co=0i {int(time.time() * 1_000_000_000)}",
    f"home,room=living_room temp=22.6,hum=35.9,co=4i {int(time.time() * 1_000_000_000)}",
    f"home,room=kitchen temp=22.7,hum=36.2,co=0i {int(time.time() * 1_000_000_000)}",
    f"home,room=living_room temp=22.8,hum=35.5,co=26i {int(time.time() * 1_000_000_000)}",
    f"home,room=kitchen temp=23.3,hum=35.9,co=0i {int(time.time() * 1_000_000_000)}",
    f"home,room=living_room temp=22.5,hum=35.3,co=1i {int(time.time() * 1_000_000_000)}",
    f"home,room=kitchen temp=23.1,hum=36.9,co=0i {int(time.time() * 1_000_000_000)}",
    f"home,room=living_room temp=22.2,hum=36.0,co=4i {int(time.time() * 1_000_000_000)}",
    f"home,room=kitchen temp=22.7,hum=35.9,co=5i {int(time.time() * 1_000_000_000)}",
]

# Write the data to the specified bucket in InfluxDB
try:
    write_api.write(bucket=bucket, org=org, record=data)
    print("IoT sensor data inserted successfully.")
except Exception as e:
    print(f"Error inserting data: {e}")

# Close the client connection
write_client.close()
