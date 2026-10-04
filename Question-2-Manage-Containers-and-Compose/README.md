# Exercise 2: Flask and Redis with Compose

The `/` route increments `page_visits` in Redis and returns the count as JSON.
The `/health` route checks Redis connectivity. Compose puts both services on an
internal network; only Flask is published on the host.

## Start and verify

```bash
docker compose config
docker compose up -d --build
docker compose ps
curl http://localhost:5000/
curl http://localhost:5000/
curl -i http://localhost:5000/health
docker compose logs web redis
```

The count should increase by one for each successful request. The API returns
503 from `/health` if Redis cannot be reached. Redis's healthcheck must pass before
Compose starts the web service.

## Check persistence

```bash
docker compose down
docker compose up -d
curl http://localhost:5000/
```

The counter should continue from its prior value. Redis uses append-only storage
on the `redis-data` volume. `docker compose down -v` explicitly removes that volume;
use it only when you intend to discard this lab's data.

## Container and image lifecycle

```bash
docker ps -a
docker images
docker compose stop
docker compose start
```

To practice a registry push, first build Exercise 1's `flask-sample-app:1.0` image,
replace `YOUR_USERNAME` with your own Docker Hub username, and authenticate:

```bash
docker login
docker tag flask-sample-app:1.0 YOUR_USERNAME/flask-sample-app:v1.0
docker push YOUR_USERNAME/flask-sample-app:v1.0
```

Those commands are instructions, not evidence that an image has been published.
The repository's old push screenshots use placeholders and have not been verified.

## Configuration and limits

The Flask container receives `REDIS_HOST=redis-db` and `REDIS_PORT=6379` through
Compose. The `redis-db` network alias resolves to the Redis service. No host-side
Redis port is required. Stop Exercise 1 before starting this stack, as both use
host port 5000. This remains a local teaching setup using Flask's development server.
