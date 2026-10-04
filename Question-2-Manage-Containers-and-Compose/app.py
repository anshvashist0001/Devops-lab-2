import os
from flask import Flask, jsonify
import redis

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST', 'redis-db')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def index():
    visits = r.incr('page_visits')
    return jsonify({
        "message": "Welcome to the Multi-Container Docker Compose App!",
        "visit_count": visits,
        "database": "Redis"
    })

@app.route('/health')
def health():
    try:
        r.ping()
        return jsonify({"status": "healthy"}), 200
    except redis.RedisError:
        return jsonify({"status": "unhealthy", "dependency": "redis"}), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
