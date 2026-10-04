import importlib.util
from pathlib import Path
from unittest.mock import Mock
import redis

ROOT=Path(__file__).parent


def load(name,directory):
    spec=importlib.util.spec_from_file_location(name,ROOT/directory/'app.py')
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_single_container_endpoints():
    module=load('q1','Question-1-Containerize-Application')
    with module.app.test_client() as client:
        assert client.get('/').json['status']=='success'
        assert client.get('/health').status_code==200


def test_redis_counter_and_health():
    module=load('q2','Question-2-Manage-Containers-and-Compose')
    module.r=Mock()
    module.r.incr.side_effect=[1,2]
    with module.app.test_client() as client:
        assert client.get('/').json['visit_count']==1
        assert client.get('/').json['visit_count']==2
        module.r.ping.return_value=True
        assert client.get('/health').status_code==200
        module.r.ping.side_effect=redis.RedisError('offline')
        assert client.get('/health').status_code==503
