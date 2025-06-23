from fastapi import FastAPI
from fastapi import WebSocket, WebSocketDisconnect
import redis
import json

app = FastAPI()
redis_client = redis.Redis(host = 'redis1', port = 6379)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept() # Websocketを開通
    try:
        while True:
            # ここに接続中に行いたい処理を記述する
            data = await websocket.receive_text()
            print(f"Received message: {data}")

            upload_data = json.loads(data)
            if 'lat' in upload_data:
                pass
            ## Simple
            redis_client.set('position', data)
    except WebSocketDisconnect:
        websocket.close()
