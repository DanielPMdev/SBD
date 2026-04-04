
import os
import sys
import json
from dotenv import load_dotenv

from config import settings

from consumer.websocket_consumer import WebSocketConsumer

from processors.sensor_event_processor import SensorEventProcessor


def test():
    """ prueba de las conexiones disponibles """

    settings.redis_dao.set('name','mario')
    print(settings.redis_dao.get('name'))
   
    record = {'name':'mario'}
    settings.mongo_dao.inser_one('users',record)
    print(settings.mongo_dao.find_one('users'))

    settings.postgres_dao.insert(sql='insert into users_example(name) values (%s)',values=("mario",))
    print(settings.postgres_dao.find_all(table='users_example'))

def process():
    """ activa el consumidor de mensajes de WebSocket """
    processor = SensorEventProcessor()

    WebSocketConsumer(
        url=os.getenv('WEBSOCKET_URL'),
        processor=processor.process
    )

def summary():
    data = {}
    """ TODO: preparar las queries necesarias para rellenar el diccionario data con la información """
    
    # Historico Completo de Eventos (MongoDB)
    data['sensor_events'] = []
    data['sensor_events'] = list(settings.mongo_dao.find_all('sensor_events'))

    # Contador de Vehiculos por Sensor (Redis)
    data['vehicle_count_per_sensor'] = {}
    sensor_keys = settings.redis_dao.keys('sensor*')
    for key in sensor_keys:
        count = settings.redis_dao.get(key)
        data['vehicle_count_per_sensor'][key] = int(count)
    

    # Último Sensor de cada Vehiculo (Redis)
    data['last_sensor_per_vehicle'] = {}
    vehicle_keys = settings.redis_dao.keys('CAR*')
    for key in vehicle_keys:
        sensor_id = settings.redis_dao.get(key)
        data['last_sensor_per_vehicle'][key] = sensor_id

    print(data)
        
    try:
        with open("data.json", 'w', encoding='utf-8') as archivo_json:
            json.dump(data, archivo_json, indent=4, ensure_ascii=False)

        print(f"Archivo creado exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al escribir el archivo: {e}")


if __name__ == "__main__":
    load_dotenv()
    settings.init()
    match sys.argv[1]:
        case "test":
            test()
        case "process":
            process()
        case 'summary':
            summary()
        