# Exercise 1: containerize Flask

This service exposes `/` with a JSON message, container hostname and UTC timestamp,
and `/health` with a 200 status. The Dockerfile copies dependencies before source
so an application-only edit can reuse the dependency-install layer.

## Build and run

From this directory, with Docker running:

```bash
docker build -t flask-sample-app:1.0 .
docker run -d -p 5000:5000 --name my-flask-container flask-sample-app:1.0
curl http://localhost:5000/
curl -i http://localhost:5000/health
docker logs my-flask-container
docker stats my-flask-container --no-stream
docker history flask-sample-app:1.0
```

The hostname should match the running container's hostname. The timestamp changes
between requests. On Windows PowerShell, use `curl.exe` if `curl` resolves to a
PowerShell alias.

## Inspect and clean up

```bash
docker inspect my-flask-container
docker stop my-flask-container
docker rm my-flask-container
```

Remove the image with `docker rmi flask-sample-app:1.0` when you no longer need it.
If the container name is already taken, remove the old lab container first.

## Files and scope

`app.py` contains the service; `requirements.txt` pins Flask; `Dockerfile` defines
the Python 3.11 image. `.dockerignore` keeps reports and screenshots out of the
build context. The accompanying reports are historical and unverified; see the
[repository README](../README.md).

This is a single-stage, layer-cached Dockerfile. Flask's development server is
appropriate for this local exercise, not a production serving configuration.
