import influxdb_client, os,time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
  
token = "B56rb9zZWZ7HlUbV6wUh5QkQzPNdVtJgVqrvy5vLnbVO3IIv_y2hhseoomGJkeDu-v-3N8yzmuTHOiW8tkZClA=="
org = "workspace"
url = "http://localhost:8086"
  
write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket="bucket_5"
  
write_api = write_client.write_api(write_options=SYNCHRONOUS)
timestamp_ns = int(time.time() * 1_000_000_000)    
data= (
   f"home,room=living_room temp=21.1,hum=35.9,co=0i {timestamp_ns}",
   f"home,room=kitchen temp=21.0,hum=35.9,co=0i {timestamp_ns}",
   f"home,room=living_room temp=21.4,hum=35.9,co=0i {timestamp_ns}",
   f"home,room=kitchen temp=23.0,hum=36.2,co=0i {timestamp_ns}",
   f"home,room=living_room temp=21.8,hum=36.0,co=0i {timestamp_ns}",
   f"home,room=kitchen temp=22.7,hum=36.1,co=0i {timestamp_ns}",
   f"home,room=living_room temp=22.2,hum=36.0,co=0i {timestamp_ns}",
   f"home,room=kitchen temp=22.4,hum=36.0,co=1i {timestamp_ns}",
   f"home,room=living_room temp=22.2,hum=35.9,co=0i {timestamp_ns}",
   f"home,room=kitchen temp=22.5,hum=36.0,co=0i {timestamp_ns}",
   f"home,room=living_room temp=22.4,hum=36.0,co=0i {timestamp_ns}",
   f"home,room=kitchen temp=22.8,hum=35.5,co=0i {timestamp_ns}",
   f"home,room=living_room temp=22.3,hum=35.9,co=2i {timestamp_ns}",
   f"home,room=kitchen temp=22.8,hum=37.9,co=3i {timestamp_ns}",
   f"home,room=living_room temp=22.3,hum=35.9,co=17i {timestamp_ns}",
   f"home,room=kitchen temp=22.7,hum=36.1,co=12i {timestamp_ns}",
   f"home,room=living_room temp=22.4,hum=30.9,co=7i {timestamp_ns}",
   f"home,room=kitchen temp=22.4,hum=35.9,co=0i {timestamp_ns}",
   f"home,room=living_room temp=22.6,hum=35.9,co=4i {timestamp_ns}",
   f"home,room=kitchen temp=22.7,hum=36.2,co=0i {timestamp_ns}",
   f"home,room=living_room temp=22.8,hum=35.5,co=26i {timestamp_ns}",
   f"home,room=kitchen temp=23.3,hum=35.9,co=0i {timestamp_ns}",
   f"home,room=living_room temp=22.5,hum=35.3,co=1i {timestamp_ns}",
   f"home,room=kitchen temp=23.1,hum=36.9,co=0i {timestamp_ns}",
   f"home,room=living_room temp=22.2,hum=36.0,co=4i {timestamp_ns}",
   f"home,room=kitchen temp=22.7,hum=35.9,co=5i {timestamp_ns}",
    )
write_api.write(bucket=bucket, org="workspace", record=data)
write_client.close()
print("IoT sensor data inserted successfully.")
