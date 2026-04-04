from config import settings
import json

class EventProcessor:
    def __init__(self):
        pass
    
    async def process(self,event):
        # Cambiar el event que es un diccionarioo para que lo carge con el JSON
        lat = event["lat"]
        lon = event["lon"]
        result = settings.redis_dao.geo_search(lat, lon)
        # Result Ejemplo: Result{1 total, docs: [Document {'id': 'geo:1', 'payload': None, 'json': '{"zoneId":"1","zoneName":"alboraia","shape":"POLYGON ((-0.35144678987961697 39.483824127585876, -0.34689466693092186 39.48227176313591, -0.33111903487034056 39.48811326427534, -0.3230720881161915 39.49979746182589, -0.3266722650166969 39.50143130249205, -0.35144678987961697 39.483824127585876))"}'}]}
        #print(f'ID de la Zona Encontrada: {json.loads(result.docs[0].json)["zoneId"]}' ) if result.total > 0 else print('Fuera de zona')
        zona_name = json.loads(result.docs[0].json)["zoneName"] if result.total > 0 else None
        event["zone"] = zona_name
        print(f'\n Nombre de la Zona Encontrada: {zona_name.title()}\n' ) if zona_name else print('\n Fuera de zona \n')

        await settings.websocket_producer.produce(event)