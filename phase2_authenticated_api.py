from flask import Flask, request, jsonify
from datetime import datetime, timezone, timedelta
from functools import wraps
import hashlib

app = Flask(__name__)

# =========================================================
# CONFIGURATION (Phase 2 Controls)
# =========================================================

API_KEYS = {
    hashlib.sha256(b"dev-key-123").hexdigest(): "developer",
}

RATE_LIMIT = 5
TIME_WINDOW = timedelta(seconds=10)

# =========================================================
# STATE (In-memory for testing baseline)
# =========================================================

vehicles = {
    "CAR123": "locked",
    "CAR456": "locked"
}

logs = []

rate_limit_store = {}
# identity -> [timestamps]

# =========================================================
# SECURITY HELPERS
# =========================================================

def get_client_identity():
    ip = request.remote_addr or "unknown"
    api_key = request.headers.get("X-API-KEY", "")
    key_hash = hashlib.sha256(api_key.encode()).hexdigest() if api_key else "no-key"
    return f"{ip}|{key_hash}"


def require_api_key(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get("X-API-KEY")

        if not api_key:
            return jsonify({"error": "missing API key"}), 401

        hashed = hashlib.sha256(api_key.encode()).hexdigest()

        if hashed not in API_KEYS:
            return jsonify({"error": "invalid API key"}), 403

        return f(*args, **kwargs)

    return wrapper


# =========================================================
# RATE LIMITING (Phase 2 Control)
# =========================================================

def is_rate_limited(identity):
    now = datetime.now(timezone.utc)

    if identity not in rate_limit_store:
        rate_limit_store[identity] = []

    # remove expired timestamps
    rate_limit_store[identity] = [
        t for t in rate_limit_store[identity]
        if now - t < TIME_WINDOW
    ]

    if len(rate_limit_store[identity]) >= RATE_LIMIT:
        return True

    rate_limit_store[identity].append(now)
    return False


# =========================================================
# LOGGING
# =========================================================

def log_event(endpoint, vehicle_id, action, success, reason=None):
    logs.append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "endpoint": endpoint,
        "vehicle_id": vehicle_id,
        "action": action,
        "success": success,
        "reason": reason,
        "client": get_client_identity()
    })


# =========================================================
# SECURITY HEADERS
# =========================================================

@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response


# =========================================================
# BASE ENDPOINT
# =========================================================

@app.route("/")
def home():
    return jsonify({
        "service": "Secure Vehicle API",
        "phase": "Phase 2 - Rate Limiting + API Auth",
        "endpoints": ["/status", "/unlock", "/start", "/logs"]
    })


# =========================================================
# STATUS (CONTROLLED ENDPOINT)
# =========================================================

@app.route("/status")
@require_api_key
def status():
    vehicle_id = request.args.get("vehicle_id")
    identity = get_client_identity()

    if not vehicle_id:
        log_event("/status", None, "status_check", False, "missing_vehicle_id")
        return jsonify({"error": "vehicle_id required"}), 400

    if is_rate_limited(identity):
        log_event("/status", vehicle_id, "status_check", False, "rate_limited")
        return jsonify({"error": "rate limit exceeded"}), 429

    if vehicle_id not in vehicles:
        log_event("/status", vehicle_id, "status_check", False, "not_found")
        return jsonify({"error": "vehicle not found"}), 404

    log_event("/status", vehicle_id, "status_check", True)

    return jsonify({
        "vehicle_id": vehicle_id,
        "status": vehicles[vehicle_id]
    })


# =========================================================
# UNLOCK
# =========================================================

@app.route("/unlock", methods=["POST"])
@require_api_key
def unlock():
    data = request.get_json(silent=True) or {}
    vehicle_id = data.get("vehicle_id")

    if vehicle_id not in vehicles:
        log_event("/unlock", vehicle_id, "unlock", False, "not_found")
        return jsonify({"error": "vehicle not found"}), 404

    vehicles[vehicle_id] = "unlocked"

    log_event("/unlock", vehicle_id, "unlock", True)

    return jsonify({
        "message": "vehicle unlocked",
        "vehicle_id": vehicle_id
    })


# =========================================================
# START
# =========================================================

@app.route("/start", methods=["POST"])
@require_api_key
def start():
    data = request.get_json(silent=True) or {}
    vehicle_id = data.get("vehicle_id")

    if vehicle_id not in vehicles:
        log_event("/start", vehicle_id, "start", False, "not_found")
        return jsonify({"error": "vehicle not found"}), 404

    log_event("/start", vehicle_id, "start", True)

    return jsonify({
        "message": "vehicle started",
        "vehicle_id": vehicle_id
    })


# =========================================================
# LOGS
# =========================================================

@app.route("/logs")
@require_api_key
def get_logs():
    return jsonify({
        "count": len(logs),
        "logs": logs[-100:]
    })


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":
    app.run(debug=False)