from pymongo import MongoClient

# --- Configuración de conexión ---
uri = "mongodb://localhost:27017/" 
cliente = MongoClient(uri)

# --- Conectarse a la base de datos ---
bd = cliente["universidad"] 

# --- Elegir una colección ---
coleccion = bd["estudiantes"]

# --- Ejecutar una consulta ---
print("Documentos encontrados:")
for doc in coleccion.find():
    print(doc)

# --- Cerrar conexión ---
cliente.close()
