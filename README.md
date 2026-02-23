# Todo DevOps Project

A production-style DevOps project built entirely on a local machine.

## Tech Stack
- Python Flask - Web application
- Docker - Containerization
- Kubernetes (Minikube) - Container orchestration
- Terraform - Infrastructure as Code
- PostgreSQL - Database
- Prometheus + Grafana - Monitoring
- GitHub Actions - CI/CD Pipeline

## Architecture
```
Code → Docker Image → Kubernetes Cluster
                          ├── todo-app (2 replicas)
                          ├── postgres (1 replica)
                          └── monitoring namespace
                                ├── Prometheus
                                └── Grafana
```

## Features
- Containerized Flask app with Docker
- Kubernetes deployment with 2 replicas and health checks
- PostgreSQL database with persistent storage
- Namespace and ConfigMap managed by Terraform
- Rolling updates and rollback capability
- Real-time monitoring with Prometheus and Grafana
- Automated CI/CD pipeline with GitHub Actions

## Prerequisites
- Docker Desktop
- Minikube
- kubectl
- Terraform
- Helm
- Git Bash / WSL2

## Quick Start

### 1. Start Minikube
```bash
minikube start
eval $(minikube docker-env)
```

### 2. Build Docker Image
```bash
docker build -t todo-app:v3 ./app
```

### 3. Apply Terraform
```bash
cd terraform
terraform init
terraform apply
cd ..
```

### 4. Deploy to Kubernetes
```bash
kubectl apply -f kubernetes/postgres-secret.yaml
kubectl apply -f kubernetes/postgres-deployment.yaml
kubectl apply -f kubernetes/postgres-service.yaml
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

### 5. Access the App
```bash
minikube service todo-service -n todo-app
```

### 6. Setup Monitoring
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
kubectl create namespace monitoring
helm install monitoring prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --set grafana.adminPassword=admin123
```

Access Grafana at http://localhost:3000 (admin/admin123)
```bash
kubectl port-forward svc/monitoring-grafana 3000:80 -n monitoring
```

## CI/CD
Every push to main branch automatically:
1. Installs Python dependencies
2. Tests the application
3. Builds Docker image
4. Verifies the build

## What I Learned
- Containerizing applications with Docker
- Managing Kubernetes deployments, services, and namespaces
- Infrastructure as Code with Terraform
- Database persistence with PostgreSQL in Kubernetes
- Monitoring with Prometheus and Grafana
- Automating pipelines with GitHub Actions