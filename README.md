# Docker and Compose lab

Two containerization exercises: a standalone Flask service, followed by a
Flask/Redis application managed with Docker Compose. The repository includes
source code, commands and historical submission reports.

The original assignment title mentions Kubernetes, but this repository contains
no Kubernetes manifests or Kubernetes deployment exercise.

## Requirements

- Docker Engine or Docker Desktop, running with Linux containers
- Docker Compose v2 (`docker compose version`)
- Port 5000 available on the host

Python 3.11 is provided by the Docker images. A local Python installation is only
needed if you want to run the Flask route tests without Docker.

## Exercises

| Directory | Task | Expected response |
|---|---|---|
| [Question 1](Question-1-Containerize-Application/README.md) | Build and run a Flask image; inspect layers and logs | JSON status, hostname and timestamp |
| [Question 2](Question-2-Manage-Containers-and-Compose/README.md) | Run Flask and Redis together; exercise volumes and lifecycle commands | JSON visit count backed by Redis |

Run one exercise at a time because both bind host port 5000. Each directory has
its own Dockerfile and requirements file; build from that directory.

## Quick start: Compose

```bash
cd Question-2-Manage-Containers-and-Compose
docker compose up -d --build
docker compose ps
curl http://localhost:5000/
curl http://localhost:5000/
curl http://localhost:5000/health
docker compose logs web
docker compose down
```

The two requests should return increasing counts. Redis uses a named volume and
append-only persistence. `docker compose down` retains the volume; adding `-v`
deletes it and resets the stored counter.

## Source checks

```bash
python -m venv .venv
# Activate your environment, then:
python -m pip install -r Question-2-Manage-Containers-and-Compose/requirements.txt
python -m pytest -q
```

Install `pytest` separately. Tests use Flask's test client and a mocked Redis
connection; they do not establish that Docker image builds or registry pushes
have succeeded. Exercise 2's health endpoint returns 503 when Redis is unavailable.

## Reports and screenshots

The PDF, Word, PNG and ZIP files are historical submission artifacts. Their
embedded terminal outputs have not been independently verified as execution
evidence; some use placeholder registry names and identifiers. Re-run the commands
and capture fresh output on your own machine before treating them as proof.
The source and Markdown instructions are the maintained reference for this lab.

## Limitations

The services use Flask's development server and are intended for local coursework.
No Kubernetes configuration, production deployment, authentication or hosted
registry image is supplied. Keep Redis reachable only on the internal Compose
network unless you have a specific reason to expose it.

If Docker cannot connect, start the engine. If port 5000 is occupied, stop the other
exercise or change the host-side port mapping. If the visit counter resets, check
whether the volume was removed and whether Redis persistence was enabled.
