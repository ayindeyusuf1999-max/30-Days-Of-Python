# GitOps Deployment with ArgoCD

A complete GitOps deployment pipeline built with ArgoCD on a local Kubernetes cluster (Minikube).

## What I Built
- Installed and configured ArgoCD on a Minikube Kubernetes cluster
- Deployed a Guestbook app via GitOps (auto-synced from GitHub)
- Containerized an AI Chatbot (Python/Flask + Anthropic API) with Docker
- Pushed Docker image to Docker Hub
- Deployed AI Chatbot to Kubernetes via ArgoCD GitOps pipeline

## Tech Stack
- Kubernetes (Minikube)
- ArgoCD v3.4.3
- Docker + Docker Hub
- Python + Flask
- GitHub (source of truth)

## Project Structure
\\\
k8s/
└── ai-chatbot/
    ├── deployment.yaml
    ├── service.yaml
    └── kustomization.yaml
\\\

## How It Works
1. Kubernetes manifests live in this GitHub repo
2. ArgoCD watches the repo for changes
3. On every push, ArgoCD automatically syncs the cluster to match the desired state
4. No manual kubectl apply needed — GitHub IS the source of truth

## Screenshots
- ArgoCD UI showing Healthy + Synced status
- Guestbook app running at localhost:9090
- AI Chatbot running at localhost:9091
