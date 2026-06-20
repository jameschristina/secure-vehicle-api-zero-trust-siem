import requests
from collections import Counter

BASE_URL = "http://127.0.0.1:5000"

# Fetch logs safely
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
# Metrics initialization
# -----------------------------
total_requests = len(logs)
success_count = 0
fail_count = 0

endpoint_counter = Counter()
vehicle_counter = Counter()

# -----------------------------
# Log processing
# -----------------------------
for log in logs:
    endpoint = log.get("endpoint", "unknown")
    vehicle_id = log.get("vehicle_id", "unknown")
    success = log.get("success", False)

    endpoint_counter[endpoint] += 1

    if vehicle_id:
        vehicle_counter[vehicle_id] += 1

    if success:
        success_count += 1
    else:
        fail_count += 1

# -----------------------------
# Output
# -----------------------------
print("\n--- LOG ANALYSIS (PHASE 1) ---\n")

print(f"Total Requests: {total_requests}")
print(f"Successful Requests: {success_count}")
print(f"Failed Requests: {fail_count}")

if total_requests > 0:
    print(f"Request Success Rate: {(success_count / total_requests) * 100:.2f}%")
else:
    print("Request Success Rate: N/A")

print("\nRequests per Endpoint:")
for endpoint, count in endpoint_counter.most_common():
    print(f"{endpoint}: {count}")

print("\nRequests per Vehicle ID:")
for vid, count in vehicle_counter.most_common():
    print(f"{vid}: {count}")