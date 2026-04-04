import websockets
import json

class WebSocketProducer:

    def __init__(self, url):
        self.__url=url
        self.__connection=None

    async def __connectar(self):
        if not self.__connection:
            self.__connection = await websockets.connect(self.__url)

    # Function to handle the chat client
    async def produce(self, event):
        await self.__connectar()
        await self.__connection.send(json.dumps(event))