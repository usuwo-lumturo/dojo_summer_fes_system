from fastapi import FastAPI
import redis

app = FastAPI()
redis_client = redis.Redis(host = 'redis1', port = 6379)


@app.get("/")
def read_root():
    position = redis_client.get('position')
    return position