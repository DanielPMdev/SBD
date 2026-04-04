import redis

class RedisDao:
    def __init__(self, hostname, port, database):
        self.__connection = redis.Redis(
            host=hostname,
            port=port,
            db=database,
            decode_responses=True
        )

    def set(self, key, value) -> any:
        return self.__connection.set(key, value)
    
    def increment(self, key):
        return self.__connection.incr(key)
    
    def get(self, key) -> any:
        return self.__connection.get(key)
    
    def mget(self, keys) -> any:
        return self.__connection.mget(keys)
    
    def keys(self, pattern) -> any:
        return self.__connection.keys(pattern)
    
    def geo_search(self, lat, lon):
        return self.__connection.ft('zonesIdx').search(
            query='@shape:[CONTAINS $pt]',
            query_params={'pt': f'POINT({lon} {lat})'}
        )
    
    def close(self):
        self.__connection.close()
