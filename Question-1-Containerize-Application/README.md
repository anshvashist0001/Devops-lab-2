# Task 1: Containerize a Sample Application Using Docker (5 Marks)

## 📌 Overview
This directory contains the complete solution for **Question 1**:
- Containerizing a Python Flask web application.
- Optimized multi-layer `Dockerfile` with layer caching.
- Documenting image layer hierarchy via `docker history`.
- Documenting container runtime behavior and resource monitoring.

## 🚀 Commands
```bash
# 1. Build the Docker Image
docker build -t flask-sample-app:1.0 .

# 2. Run Container (Detached mode with port 5000 mapping)
docker run -d -p 5000:5000 --name my-flask-container flask-sample-app:1.0

# 3. Test Application Response
curl http://localhost:5000/
curl http://localhost:5000/health

# 4. Inspect Image Layers
docker history flask-sample-app:1.0

# 5. Inspect Container Runtime Behavior & Stats
docker logs my-flask-container
docker stats my-flask-container --no-stream
```

## 📸 Screenshots Included
- `screenshots/01_docker_build.png`: Build step execution and layer export.
- `screenshots/02_docker_run_and_test.png`: Detached container execution and `curl` JSON response.
- `screenshots/03_image_layers_history.png`: Layer composition via `docker history`.
- `screenshots/04_container_logs_and_stats.png`: Runtime logs and resource metrics.
