from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import redis
import json
import traceback

app = FastAPI()
redis_client = redis.Redis(host = 'redis1', port = 6379)

origins = [ 
    "https://dojo-summer.marpyong.work",
    "https://gpsapi.marpyong.work",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    try:
        redis_data = redis_client.get('position').decode('utf-8')
        print(redis_data)
        if redis_data is not None:
            redis_data_dict = json.loads(redis_data)
            position = {
                "lat": redis_data_dict["lat"],
                "lng": redis_data_dict["lng"],
            }
            return position

        return {
            "lat": 35.8,
            "lng": 139.6
        }
    except Exception as err:
        print(traceback.format_exc())
        return {
            "lat": 35.8,
            "lng": 139.6
        }
