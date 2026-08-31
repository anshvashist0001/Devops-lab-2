# Task 2: Manage Docker Containers, Images & Docker Compose (5 Marks)

## 📌 Overview
This directory contains the complete solution for **Question 2**:
- Container lifecycle commands (listing, starting, stopping, removing).
- Image tagging and pushing to a remote registry (Docker Hub).
- Multi-container application orchestration using **Docker Compose** (Flask Web Service + Redis Cache Database).

## 🚀 Commands

### 1. Container & Image Lifecycle
```bash
docker ps
docker ps -a
docker images
docker stop my-flask-container
docker start my-flask-container
docker rm my-flask-container
docker rmi flask-sample-app:1.0
docker system prune -f
```

### 2. Tag & Push to Docker Hub Registry
```bash
docker login
docker tag flask-sample-app:1.0 <username>/flask-sample-app:v1.0
docker push <username>/flask-sample-app:v1.0
```

### 3. Multi-Container Orchestration (Docker Compose)
```bash
# Start full stack
docker compose up -d --build

# View stack status
docker compose ps

# Test persistent hit counter
curl http://localhost:5000/

# Teardown stack
docker compose down -v
```

## 📸 Screenshots Included
- `screenshots/01_container_lifecycle.png`: Lifecycle operations (`ps`, `stop`, `start`, `rm`).
- `screenshots/02_docker_tag_and_push.png`: Docker Hub registry login, tagging, and pushing.
- `screenshots/03_compose_build_and_up.png`: Multi-container build, network creation, and start.
- `screenshots/04_compose_testing_and_down.png`: Testing Redis persistence and stack teardown.
