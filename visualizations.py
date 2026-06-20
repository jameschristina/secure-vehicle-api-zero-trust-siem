import requests
from collections import Counter
import matplotlib.pyplot as plt

BASE_URL = "http://127.0.0.1:5000"

# -----------------------------
# Fetch logs safely
# -----------------------------
try:
    response = requests.get(f"{BASE_URL}/logs")

    if response.status_code != 200:
        print("Failed to fetch logs from server")
        logs = []
    else:
        logs = response.json()

except Exception as e:
    print(f"Error connecting to server: {e}")
    logs = []

# -----------------------------
# Counters
# -----------------------------
endpoint_counter = Counter()
vehicle_counter = Counter()

for log in logs:
    endpoint = log.get("endpoint", "unknown")
    vehicle_id = log.get("vehicle_id", "unknown")

    endpoint_counter[endpoint] += 1

    if vehicle_id:
        vehicle_counter[vehicle_id] += 1

# -----------------------------
# Visualization: Endpoint Usage
# -----------------------------
if endpoint_counter:
    endpoints = list(endpoint_counter.keys())
    counts = list(endpoint_counter.values())

    plt.figure()
    plt.bar(endpoints, counts)
    plt.title("Requests per Endpoint")
    plt.xlabel("Endpoint")
    plt.ylabel("Number of Requests")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# -----------------------------
# Visualization: Vehicle Usage
# -----------------------------
if vehicle_counter:
    vehicles = list(vehicle_counter.keys())
    counts = list(vehicle_counter.values())

    plt.figure()
    plt.bar(vehicles, counts)
    plt.title("Requests per Vehicle ID")
    plt.xlabel("Vehicle ID")
    plt.ylabel("Number of Requests")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()