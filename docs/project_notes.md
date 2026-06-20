# Project Notes

## Phase 1 – Vulnerable Baseline
- Built simple Flask API
- Endpoints: /status, /unlock, /start
- Access based only on vehicle_id
- No authentication
- No authorization
- No rate limiting
- Added basic logging

## Key Decisions
- Keep system intentionally vulnerable
- Use in-memory data (no database)

## Assumptions
- vehicle_id is predictable
- no user identity exists
- unrestricted endpoint access

---

## Phase 2 – Authentication + Rate Limiting
- Added API key authentication
- Added request rate limiting
- Added structured security logging
- Added security response headers
- Added request attribution

## Security Goals
- Prevent unrestricted access
- Introduce authenticated identities
- Reduce automated abuse attempts
- Improve observability

---

## Phase 3 – Authorization + Least Privilege
- Added entitlement enforcement
- Mapped identities to authorized vehicles
- Implemented authorization validation
- Blocked cross-vehicle access attempts
- Added unauthorized access logging

## Security Concepts
- Authentication vs authorization
- Least privilege
- Zero Trust identity validation
- Entitlement-based access control

---

## Phase 4 – SIEM / UEBA-Style Detection
- Built live SIEM-style polling engine
- Added weighted risk scoring
- Added identity-based event tracking
- Added cumulative risk scoring
- Added alert classification
- Added live detection snapshots
- Added alert suppression cooldowns

## Detection Concepts
- Behavioral anomaly detection
- Identity-centric monitoring
- Risk aggregation
- Security event correlation
- SIEM/UEBA-style observability

---

## Visualization Layer
- Added visualization scripts
- Added PNG export support
- Added event/risk visualization refinement

---

## Metrics Captured
- successful requests
- failed requests
- unauthorized access attempts
- rate-limit violations
- cumulative risk score
- event frequency
- identity event distribution