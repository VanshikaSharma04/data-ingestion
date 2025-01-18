import influxdb_client
from influxdb_client import InfluxDBClient, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import time

# Function to create InfluxDB client
def create_client(url, token, org):
    """
    Create an instance of the InfluxDB client.
    
    Args:
        url (str): The URL of the InfluxDB instance.
        token (str): The authentication token for the InfluxDB instance.
        org (str): The organization name.
        
    Returns:
        InfluxDBClient: Configured client instance.
    """
    return influxdb_client.InfluxDBClient(url=url, token=token, org=org)

# Function to generate timestamp in nanoseconds
def get_current_timestamp_ns():
    """
    Generate the current timestamp in nanoseconds.
    
    Returns:
        int: Current time in nanoseconds.
    """
    return int(time.time() * 1_000_000_000)

# Function to prepare data for insertion
def prepare_data(timestamp_ns):
    """
    Prepare IoT sensor data in line protocol format.
    
    Args:
        timestamp_ns (int): The timestamp in nanoseconds.
        
    Returns:
        tuple: Tuple of data points formatted in line protocol.
    """
    return (
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

# Main function
def main():
    """
    Main function to connect to InfluxDB and write IoT sensor data.
    """
    # Configuration
    url = "http://localhost:8086"
    token = "INSERT_YOUR_TOKEN_HERE"
    org = "workspace"
    bucket = "bucket_new"
    
    # Create client
    client = create_client(url, token, org)
    
    # Write API
    write_api = client.write_api(write_options=SYNCHRONOUS)
    
    # Get current timestamp
    timestamp_ns = get_current_timestamp_ns()
    
    # Prepare data
    data = prepare_data(timestamp_ns)
    
    # Write data to InfluxDB
    try:
        write_api.write(bucket=bucket, org=org, record=data)
        print("IoT sensor data inserted successfully.")
    except Exception as e:
        print(f"Error writing data: {e}")
    finally:
        # Close client connection
        client.close()

# Entry point
if __name__ == "__main__":
    main()
