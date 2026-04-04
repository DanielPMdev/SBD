import os
from dotenv import load_dotenv
from config import settings
from consumer.websocket_consumer import WebSocketConsumer


from processors.event_processor import EventProcessor

def process():
    processor = EventProcessor()

    WebSocketConsumer(
        url=os.getenv('WEBSOCKET_INPUT_URL'),
        processor=processor.process
    )

if __name__ == "__main__":
    load_dotenv()
    settings.init()
    
    process()
        