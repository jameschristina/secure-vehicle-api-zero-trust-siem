# 🚗 Secure Vehicle API: Zero Trust + SIEM Simulation

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Zero Trust](https://img.shields.io/badge/Zero%20Trust-Architecture-green)
![SIEM](https://img.shields.io/badge/SIEM-Analytics-red)
![UEBA](https://img.shields.io/badge/UEBA-Behavioral%20Analytics-orange)

---

## 🚀 Overview

Secure Vehicle API: Zero Trust SIEM is a cybersecurity simulation demonstrating how a vulnerable connected vehicle API can be progressively secured through authentication, authorization, least-privilege enforcement, and behavioral detection. This simulation highlights how weak trust assumptions can create cyber-physical risk and how Zero Trust principles can reduce that risk through identity-centric security controls.

The project evolves through four security maturity phases:

1. Vulnerable Baseline
2. Authentication + Rate Limiting
3. Authorization + Least Privilege
4. SIEM / UEBA Detection

Across four phases, the project introduces authentication, authorization, least-privilege enforcement, and SIEM-style detections that identify identity misuse and behavioral anomalies. The goal is to illustrate how IAM and Zero Trust principles can be applied within a cyber-physical environment while showing how API activity can become meaningful security telemetry.


---

## 🧭 Project Inspiration

Modern vehicles are increasingly connected systems. Security failures can have consequences beyond data loss and directly impact physical safety.

This project was inspired by real-world vehicle security discussions and explores how identity validation, authorization controls, behavioral monitoring, and security analytics can be applied to connected systems.

---

## 🔄 Security Evolution

```text
Vehicle API
      ↓
Authentication
      ↓
Authorization
      ↓
Security Logging
      ↓
SIEM / UEBA Detection
      ↓
Visualization & Reporting
```

---

## 🎯 Project Objectives

This project demonstrates practical cybersecurity concepts including:

* API Security
* Authentication
* Authorization
* Zero Trust Architecture
* Least Privilege Enforcement
* Security Logging
* Detection Engineering
* SIEM Analytics
* UEBA Behavioral Monitoring
* Risk Scoring
* Security Visualization

---

## 🛡️ Project Phases

### Phase 1 — Vulnerable Baseline

#### Implementation

* Flask API with unrestricted access
* Endpoints:

  * /status
  * /unlock
  * /start
* Access controlled only by vehicle identifiers
* No authentication
* No authorization
* No rate limiting

#### Security Weaknesses Demonstrated

* Broken access control
* Predictable identifiers
* Unauthenticated API access
* Lack of observability

---

### Phase 2 — Authentication + Rate Limiting

#### Implementation

* API key authentication
* Request rate limiting
* Structured security logging
* Security response headers

#### Security Concepts

* Identity validation
* API hardening
* Abuse prevention
* Request attribution

---

### Phase 3 — Authorization + Least Privilege

#### Implementation

* Entitlement enforcement
* Identity-to-vehicle mapping
* Authorization-aware logging
* Cross-vehicle access prevention

#### Security Concepts

* Authentication vs Authorization
* Least Privilege
* Entitlement Enforcement
* Zero Trust Architecture

---

### Phase 4 — SIEM / UEBA Detection

#### Implementation

* SIEM-style polling engine
* Weighted risk scoring
* Identity risk aggregation
* Alert classification
* Event correlation
* Behavioral detection
* Alert suppression logic

#### Security Concepts

* Behavioral Analytics
* Identity-Centric Monitoring
* Event Correlation
* Risk Aggregation
* SIEM / UEBA Observability

---

## 📊 Visualization Layer

### visualizations.py

Original visualization implementation.

### visualizations_v2.py

Enhanced visualization implementation with PNG export support.

Current visualizations include:

* Requests per Endpoint
* Requests per Vehicle ID

---

## 💼 Skills Demonstrated

* Zero Trust Architecture
* API Security
* Identity Security
* Authentication
* Authorization
* Detection Engineering
* SIEM Analytics
* UEBA Monitoring
* Security Logging
* Risk Scoring
* Python Development
* Security Visualization

---

## 📂 Repository Structure

```text
docs/

phase1_vulnerable_api.py
phase2_authenticated_api.py
phase3_authorization_api.py
phase4_siem_detection.py

visualizations.py
visualizations_v2.py

README.md
requirements.txt
.gitignore
```

---

## ⚙️ Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```bash
python phase1_vulnerable_api.py
python phase2_authenticated_api.py
python phase3_authorization_api.py
python phase4_siem_detection.py
```

---

## Collaboration Acknowledgement

Secure Vehicle API: Zero Trust SIEM represents my contribution across four project phases focused on API security, IAM principles, and SIEM while acknowledging the collaborative effort and shared vision that served as the foundation for a broader security platform.

This repository focused on demonstrating the progression from implicit vehicle trust to Zero Trust API security through authentication, authorization, entitlement enforcement, and SIEM detection concepts. It began with discussions surrounding vehicle theft, cyber-physical risk, and the real-world consequences of weak trust models.

Through collaboration with contributor, Chukwuemeke Ikpeasonim, the original concept evolved into a larger 20-phase security operations simulation exploring advanced topics such as threat hunting, SOAR automation, incident response, and SOC workflows.

The full Secure Vehicle API: Zero Trust Security Operations Platform can be found at: [https://github.com/ikpeasonim/secure-vehicle-api-zero-trust].

## 👥 Project Contributors

### Christina James

Security Architecture | Identity & Access Management | Zero Trust Security

LinkedIn: www.linkedin.com/in/christinanjames

GitHub: www.github.com/jameschristina

### Chukwuemeke Ikpeasonim

Cybersecurity Engineering | Detection Engineering | SOC Operations | Zero Trust Security

LinkedIn: www.linkedin.com/in/chukwuemeke-ikpeasonim

GitHub: www.github.com/switice

---
## ⭐ Security Engineering Outcomes

This project demonstrates the ability to:

* Secure API-driven systems using Zero Trust principles
* Implement authentication and authorization controls
* Build behavioral detection workflows
* Develop SIEM-style monitoring pipelines
* Correlate identity activity with security telemetry
* Generate actionable security reporting
* Progress a vulnerable application toward a mature security architecture
