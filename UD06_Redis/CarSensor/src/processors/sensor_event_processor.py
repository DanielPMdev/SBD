from config import settings

class SensorEventProcessor:
    def __init__(self):
        pass

    def process(self,event):
        """ TODO: realizar el procesamiento del evento que se recibe por WebSocket """
        """ todas las conexiones a las bases de datos estan accesibles mediante la variable settings """
        print(event)
        #{"vehicle":{"id":"CAR01","brand":"Toyota","model":"Corolla","licensePlate":"ABC-1234","speed":3},"sensor":"sensor1","timestamp":1764786764535}
        
        # Historico Completo de Eventos (MongoDB)
        settings.mongo_dao.inser_one('sensor_events', event)

        # Contador de Vehiculos por Sensor (Redis)
        sensor_id = event['sensor']
        settings.redis_dao.increment(sensor_id)
        
        # Último Sensor de cada Vehiculo (Redis)
        vehicle_id = event['vehicle']['id']
        settings.redis_dao.set(vehicle_id, sensor_id)

        """
        settings.postgres_dao.insert(
            sql='''INSERT INTO last_sensor_per_vehicle(vehicle_id, sensor_id, timestamp)
                   VALUES (%s, %s, to_timestamp(%s / 1000.0))
                   ON CONFLICT (vehicle_id) 
                   DO UPDATE SET sensor_id = EXCLUDED.sensor_id, timestamp = EXCLUDED.timestamp;''',
            # EXCLUDED es un alias especial que se refiere a los valores que se intentarían
            # insertar si no hubiera ocurrido el conflicto.
            values=(vehicle_id, sensor_id, event['timestamp'])
        )
        """
