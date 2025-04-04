import json
import random
import string
import os
from datetime import datetime, timedelta, timezone

def generate_random_timestamp_2025():
    # Define the start and end of the year 2025
    start_date = datetime(2025, 1, 1, tzinfo=timezone(timedelta(hours=1)))
    end_date = datetime(2025, 12, 31, 23, 59, 59, 999999, tzinfo=timezone(timedelta(hours=1)))

    # Generate a random timedelta within the year 2025
    random_seconds = random.randint(0, int((end_date - start_date).total_seconds()))
    random_timestamp = start_date + timedelta(seconds=random_seconds)

    # Format the timestamp as "YYYY-MM-DDTHH:MM:SS.SSS+01:00"
    return random_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+01:00"

# Generate a unique 5-character alphanumerical string
def generate_unique_code(length=5):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Define file paths
input_file = "BatteryPassDemo.json"
output_file = "BatteryPass"

# Check if the input file exists
if not os.path.exists(input_file):
    print(f"Error: File '{input_file}' not found in the current directory.")
else:
    # Read JSON data from the file
    with open(input_file, "r") as file:
        data = json.load(file)

    unique_identifier = generate_unique_code()
    data["identification"]["idDmc"] = unique_identifier

        # Export modified data back to a JSON file
    with open(output_file+unique_identifier+".json", "w") as file:
        json.dump(data, file, indent=2)

    print(f"Modified JSON data saved to '{output_file}'")
