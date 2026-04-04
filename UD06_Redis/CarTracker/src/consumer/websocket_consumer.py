import asyncio
import websockets
import json

class WebSocketConsumer:

    def __init__(self, url, processor):
        self.__url=url
        asyncio.run(self.__consume(processor))

    # Function to handle the chat client
    async def __consume(self, processor):
        async with websockets.connect(self.__url) as websocket:
            while True:
                # Receive a message from the server
                event = await websocket.recv()
                print(f"Received: {event}")
                await processor(json.loads(event))

