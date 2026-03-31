from pymongo import MongoClient
from bson import ObjectId

# --- Conexión a MongoDB ---
cliente = MongoClient("mongodb://localhost:27017/")
bd = cliente["instituto"]

# --- LIMPIAR DATOS PREVIOS ---
bd.estudiantes.delete_many({})
bd.cursos.delete_many({})
bd.inscripciones.delete_many({})

# =========================
#  INSERCIÓN DE DATOS
# =========================

# ----- Colección estudiantes -----
estudiantes = [
    {
        "nombre": "Daniel Porras Morales",
        "edad": 22,
        "correo": "danielpm.dev@gmail.com",
        "ciudad": "Tresjuncos",
    },
    {
        "nombre": "Diego Martínez Ruiz",
        "edad": 24,
        "correo": "diego.martinez@gmail.com",
        "ciudad": "Valencia",
    },
    {
        "nombre": "Carmen Torres López",
        "edad": 21,
        "correo": "carmen.torres@gmail.com",
        "ciudad": "Bilbao",
    },
]
result_est = bd.estudiantes.insert_many(estudiantes)
print("Estudiantes insertados con IDs:", result_est.inserted_ids)

# ----- Colección cursos -----
cursos = [
    {
        "nombre": "Sistemas de Big Data",
        "codigo": "SBD101",
        "creditos": 6,
        "instructor": "Javier Peña",
    },
    {
        "nombre": "Programacion de Inteligencia Artificial",
        "codigo": "PIA202",
        "creditos": 5,
        "instructor": "Laura Ortega",
    },
    {
        "nombre": "Minería de Datos",
        "codigo": "MD303",
        "creditos": 4,
        "instructor": "Andrés Muñoz",
    },
]
result_cur = bd.cursos.insert_many(cursos)
print("Cursos insertados con IDs:", result_cur.inserted_ids)

# ----- Colección inscripciones -----
inscripciones = [
    {
        "id_estudiante": result_est.inserted_ids[0],
        "id_curso": result_cur.inserted_ids[0],
        "anio": 2025,
        "nota": 8.7,
    },
    {
        "id_estudiante": result_est.inserted_ids[1],
        "id_curso": result_cur.inserted_ids[1],
        "anio": 2025,
        "nota": 7.9,
    },
    {
        "id_estudiante": result_est.inserted_ids[2],
        "id_curso": result_cur.inserted_ids[2],
        "anio": 2025,
        "nota": 9.1,
    },
]
result_ins = bd.inscripciones.insert_many(inscripciones)
print("Inscripciones insertadas con IDs:", result_ins.inserted_ids)

# =========================
#  CONSULTAS
# =========================

# Buscar un curso por ID
id_curso_buscado = result_cur.inserted_ids[1]
curso = bd.cursos.find_one({"_id": id_curso_buscado})
print("\n Curso encontrado por ID:")
print(curso)

# Buscar un alumno por nombre
nombre_buscado = "Daniel Porras Morales"
alumno = list(bd.estudiantes.find({"nombre": nombre_buscado}))
print("\n Alumno encontrado por nombre:")
for a in alumno:
    print(a)

# =========================
#  ACTUALIZACIÓN
# =========================

# Actualizar la ciudad de un estudiante
resultado_update = bd.estudiantes.update_one(
    {"nombre": "Diego Martínez Ruiz"}, {"$set": {"ciudad": "Madrid"}}
)
print(f"\n Estudiantes modificados: {resultado_update.modified_count}")

# =========================
#  ELIMINACIÓN
# =========================

# Eliminar una inscripción
id_estudiante_eliminar = result_est.inserted_ids[1]
resultado_delete = bd.inscripciones.delete_one(
    {"id_estudiante": id_estudiante_eliminar}
)
print(f"\n Inscripciones eliminadas: {resultado_delete.deleted_count}")

# =========================
#  AGREGACIONES
# =========================

# Mostrar inscripciones con nombres de estudiantes y asignaturas
print("\n Inscripciones con nombres de estudiante y curso:")
pipeline1 = [
    {
        "$lookup": {
            "from": "estudiantes",
            "localField": "id_estudiante",
            "foreignField": "_id",
            "as": "estudiante",
        }
    },
    {"$unwind": "$estudiante"},
    {
        "$lookup": {
            "from": "cursos",
            "localField": "id_curso",
            "foreignField": "_id",
            "as": "curso",
        }
    },
    {"$unwind": "$curso"},
    {
        "$project": {
            "_id": 0,
            "anio": 1,
            "nota": 1,
            "estudiante.nombre": 1,
            "curso.nombre": 1,
        }
    },
]
for doc in bd.inscripciones.aggregate(pipeline1):
    print(doc)

# Calcular promedio de notas por estudiante
print("\n Promedio de notas por estudiante:")
pipeline2 = [
    {
        "$lookup": {
            "from": "estudiantes",
            "localField": "id_estudiante",
            "foreignField": "_id",
            "as": "estudiante",
        }
    },
    {"$unwind": "$estudiante"},
    {"$group": {"_id": "$estudiante.nombre", "promedio_notas": {"$avg": "$nota"}}},
    {
        "$project": {
            "_id": 0,
            "estudiante": "$_id",
            "promedio_notas": {"$round": ["$promedio_notas", 2]},
        }
    },
]
for doc in bd.inscripciones.aggregate(pipeline2):
    print(doc)

# Contar cuántos estudiantes hay inscritos por asignatura
print("\n Total de estudiantes por curso:")
pipeline3 = [
    {
        "$lookup": {
            "from": "cursos",
            "localField": "id_curso",
            "foreignField": "_id",
            "as": "curso",
        }
    },
    {"$unwind": "$curso"},
    {"$group": {"_id": "$curso.nombre", "total_estudiantes": {"$sum": 1}}},
    {"$project": {"_id": 0, "curso": "$_id", "total_estudiantes": 1}},
]
for doc in bd.inscripciones.aggregate(pipeline3):
    print(doc)

# =========================
#  FIN DEL PROGRAMA
# =========================
cliente.close()
print("\n Operaciones completadas correctamente.")
