# Generative AI CI/CD Deployment – Weekly Assignment Week 4

## Instructions
This assignment requires deploying a Generative AI model using CI/CD practices. The goal is to use the tools and methods learned in Week 4, obtain a working endpoint URL, and manage GCP cloud costs effectively.

---

## Objective
Deploy a simple Generative AI model by applying automated CI/CD pipeline principles using Google Cloud Build and GKE, and create a budget alert on GCP to control resource usage.

---

## Tasks

### 1. Budget Alert (GCP Billing)
- Created a budget alert in **GCP Billing > Budgets & Alerts**
- Thresholds set at 50%, 90%, and 100%
- Notifications sent via email
- Screenshot of the alert is available in the `/proof/` folder

### 2. CI/CD Pipeline & Deployment to GKE

**CI/CD Flow Overview**:
- **Docker Build & Push**: The app is built using Docker and pushed to Container Registry
- **Deployment**: Cloud Build automatically deploys the app to GKE using `kubectl`
- **Kubernetes Service**: Configured as `LoadBalancer` to expose a public IP
- **Endpoint**: Accessible via browser after deployment

**Tools used**:
- Google Cloud Build
- Google Kubernetes Engine (Standard mode)
- Docker
- Kubernetes YAMLs
- Cloud Monitoring & Billing

**Trigger**:
- Connected to GitHub repo using Developer Connect
- Trigger is set to run on `push to main`

### 3. Documentation
All steps and components are included:
- `cloudbuild.yaml`: Pipeline definition
- `Dockerfile`: Container spec
- `kubernetes/`: Contains deployment and service YAMLs
- `app/`: Source code of the lightweight Generative AI model
- `README.md`: This file
- `/proof/`: Contains billing alert screenshot and deployment verification 

---

## Endpoint URL
> Accessible at: http://34.126.77.177/


---

## Project Structure

```
├── app/
│   ├── model.py
│   └── main.py
├── cloudbuild.yaml
├── Dockerfile
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
├── requirements.txt
├── proof/
│   └── budget_alert_screenshot.png
└── README.md
```

---

## Notes
- Cluster created: `genai-cluster` (Standard mode, 1 node, region: asia-southeast1)
- Budget alert ensures GCP usage stays within safe limits
- The model is a lightweight text generator using Markov Chain

---

## Status
✔️ Deployment successful  
✔️ Budget alert active  
✔️ Endpoint accessible  
✔️ CI/CD pipeline working via GitHub trigger