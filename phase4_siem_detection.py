import requests
import json
import time
from collections import defaultdict
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000"

HEADERS = {
    "X-API-KEY": "dev-key-123"
}

# -----------------------------
# RISK MODEL
# -----------------------------
RISK_WEIGHTS = {
    "missing_api_key": 5,
    "invalid_api_key": 10,
    "unauthorized_vehicle_access": 20,
    "rate_limited": 8,
    "not_found": 3,
    "success": 0
}

ALERT_THRESHOLD = 20
POLL_INTERVAL = 3

# -----------------------------
# STATE
# -----------------------------
identity_events = defaultdict(list)
identity_scores = defaultdict(int)
seen_logs = set()

# ALERT SUPPRESSION (FIX)
alert_cache = {}
ALERT_COOLDOWN = 15 # seconds

# -----------------------------
# FETCH LOGS
# -----------------------------
def fetch_logs():
    try:
        r = requests.get(f"{BASE_URL}/logs", headers=HEADERS)

        print(f"\nSTATUS CODE: {r.status_code}")

        if r.status_code != 200:
            return []

        if not r.text.strip():
            return []

        data = r.json()

        if isinstance(data, dict) and "logs" in data:
            data = data["logs"]

        if not isinstance(data, list):
            return []

        return data

    except Exception as e:
        print(f"[ERROR] {e}")
        return []

# -----------------------------
# NORMALIZE LOG
# -----------------------------
def normalize(log):
    if isinstance(log, str):
        try:
            return json.loads(log)
        except:
            return None

    if isinstance(log, dict):
        return log

    return None

# -----------------------------
# IDENTITY BUILDER
# -----------------------------
def get_identity(log):
    client = log.get("client") or log.get("ip") or log.get("client_ip") or "unknown_client"
    vehicle = log.get("vehicle_id") or "unknown_vehicle"
    return f"{client}|{vehicle}"

# -----------------------------
# SCORING ENGINE
# -----------------------------
def score_event(log):
    if log.get("success") is True:
        return 0

    reason = log.get("failure_reason") or log.get("reason") or "unknown"
    return RISK_WEIGHTS.get(reason, 5)

# -----------------------------
# PROCESS LOGS
# -----------------------------
def process_logs(logs):
    new_events = 0

    for raw in logs:
        log = normalize(raw)

        if not log:
            continue

        fingerprint = json.dumps(log, sort_keys=True)

        if fingerprint in seen_logs:
            continue

        seen_logs.add(fingerprint)
        new_events += 1

        identity = get_identity(log)
        score = score_event(log)

        identity_events[identity].append(log)
        identity_scores[identity] += score

    return new_events

# -----------------------------
# ALERT COOLDOWN CHECK (FIX)
# -----------------------------
def should_alert(identity):
    now = time.time()

    if identity in alert_cache:
        if now - alert_cache[identity] < ALERT_COOLDOWN:
            return False

    alert_cache[identity] = now
    return True

# -----------------------------
# ALERT ENGINE
# -----------------------------
def trigger_alert(identity):
    score = identity_scores[identity]
    events = identity_events[identity]

    severity = (
        "CRITICAL" if score >= 100 else
        "HIGH" if score >= 60 else
        "MEDIUM" if score >= 30 else
        "LOW"
    )

    print("\n🚨 SIEM v4.1 ALERT (ACTIVE DETECTION MODE) 🚨")
    print(f"Time: {datetime.now().strftime('%H:%M:%S')}")
    print(f"Identity: {identity}")
    print(f"Severity: {severity}")
    print(f"Risk Score: {float(score)}")
    print(f"Events: {len(events)}")
    print("-" * 60)

# -----------------------------
# SNAPSHOT
# -----------------------------
def snapshot():
    print("\n--- LIVE SIEM SNAPSHOT (v4.1 ACTIVE MODE) ---")

    if not identity_scores:
        print("[INFO] No identities detected yet.")
        return

    for identity, score in identity_scores.items():
        print(f"{identity} | Score: {float(score)} | Events: {len(identity_events[identity])}")

# -----------------------------
# MAIN LOOP
# -----------------------------
def run():
    print("\n🧠 STARTING SIEM v4.1 — ACTIVE DETECTION MODE\n")

    while True:
        logs = fetch_logs()

        new_events = process_logs(logs)

        print(f"\n[METRICS] New Events: {new_events} | "
              f"Total Identities: {len(identity_scores)} | "
              f"Total Events: {sum(len(v) for v in identity_events.values())}")

        for identity in identity_scores:
            if identity_scores[identity] >= ALERT_THRESHOLD:
                if should_alert(identity):
                    trigger_alert(identity)

        snapshot()

        print(f"\n[HEARTBEAT] {datetime.now().strftime('%H:%M:%S')} | Polling logs...\n")

        time.sleep(POLL_INTERVAL)

# -----------------------------
# ENTRY
# -----------------------------
if __name__ == "__main__":
    run()