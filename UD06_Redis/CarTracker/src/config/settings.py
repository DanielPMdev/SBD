import os

from dao.redis_dao import RedisDao

from producer.websocket_producer import WebSocketProducer

def init():
    global redis_dao
    redis_dao = RedisDao(
        hostname=os.getenv('REDIS_HOSTNAME'),
        port=os.getenv('REDIS_PORT'),
        database=os.getenv('REDIS_DATABASE')
    )

    global websocket_producer
    websocket_producer = WebSocketProducer(
        url=os.getenv('WEBSOCKET_OUTPUT_URL'),
    )