import json

with open("logs.json", "r") as file:
    logs = json.load(file)

total_requests = len(logs)
successful_requests = 0
failed_requests = 0
endpoint_counts = {}

for log in logs:
    if log["success"] == True:
        successful_requests += 1
    else:
        failed_requests += 1

    endpoint = log["endpoint"]
    endpoint_counts[endpoint] = endpoint_counts.get(endpoint, 0) + 1

if total_requests > 0:
    success_rate = (successful_requests / total_requests) * 100
else:
    success_rate = 0

print("\n--- BASELINE METRICS ---\n")
print(f"Total Requests: {total_requests}")
print(f"Successful Requests: {successful_requests}")
print(f"Failed Requests: {failed_requests}")
print(f"Success Rate: {success_rate:.2f}%")

print("\nRequests by Endpoint:")
for endpoint, count in endpoint_counts.items():
    print(f"{endpoint}: {count}")