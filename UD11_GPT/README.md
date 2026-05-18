# Modelos de Lenguaje y RAG

> Asignatura: Sistemas de Big Data  
> Curso de Especialización en Inteligencia Artificial y Big Data

## 📌 Descripción
Este bloque temático se centra en la implementación práctica de un sistema RAG (Retrieval-Augmented Generation) minimalista. A través de un cuaderno de Jupyter, se aborda el proceso completo de generación de embeddings, recuperación de información basada en similitud del coseno local, y la integración de MongoDB Atlas como base de datos vectorial en la nube (Vector Store) mediante búsquedas vectoriales avanzadas. Finalmente, se conecta con grandes modelos de lenguaje (LLMs) mediante APIs para generar respuestas precisas fundamentadas en el contexto recuperado.

## 🎯 Objetivos de Aprendizaje
- Comprender la arquitectura de soporte y flujo básico de un sistema RAG.
- Implementar la vectorización de textos estáticos utilizando modelos ligeros basados en Sentence Transformers.
- Calcular y aplicar la métrica matemática de similitud del coseno con NumPy para la recuperación de contexto relevante de forma local.
- Integrar bases de datos NoSQL como almacén vectorial, implementando MongoDB Atlas Vector Search para indexar y buscar información semántica en la nube.
- Orquestar llamadas remotas a LLMs mediante interfaces compatibles con OpenAI y construir prompts contextualizados con el contexto recuperado.

## 🧠 Contenidos
El módulo explora el ciclo completo de la Generación Aumentada por Recuperación en su forma más pura y evoluciona hacia una solución en la nube persistente. Comienza cargando un modelo de vectorización ligero localizado (`paraphrase-MiniLM-L3-v2`) para codificar fragmentos de conocimiento en un espacio hiperdimensional. Se detiene especialmente en exponer de forma programática cómo comparar la consulta de entrada vectorial (pregunta de usuario) contra la base de conocimientos empleando funciones directas (similitud de coseno). 

Además, se avanza integrando **MongoDB Atlas** como base de datos NoSQL y vectorial. Se explica cómo almacenar los documentos junto con sus respectivos embeddings en colecciones de MongoDB y cómo realizar búsquedas semánticas remotas mediante la etapa de agregación `$vectorSearch` utilizando un índice vectorial (`chatbot_index`). Seguidamente, se extrae el contexto relevante (tanto local como remoto a través de `get_context_mongo`) y se ensambla en un `prompt`. Este prompt compuesto se transfiere a un modelo gigante servido externamente (`gpt-oss-120b:cerebras`) logrando generar respuestas acotadas al material aportado, minimizando alucinaciones.

### Extracción Semántica
Se expone una función central (`get_context`) que itera comparativamente la codificación de la consulta de forma local frente a las piezas de datos asistiéndose de álgebra vectorial, y su evolución (`get_context_mongo`) para realizar consultas vectoriales de manera distribuida y escalable en MongoDB Atlas.

### Inferencia y Prompting
Mediante el cliente de OpenAI (reestructurando la base_url hacia Hugging Face), se configura el rol del LLM (Tutor) y se restringen de forma estricta sus predicciones al bloque referenciado de contexto. Para preguntas ausentes en el corpus inyectado, se fuerza al modelo a declarar su desconocimiento mediante reglas impuestas.

## 🛠️ Tecnologías y Librerías
| Herramienta | Uso en este tema |
|---|---|
| `openai` | Interfaz cliente utilizada para conectarse al servicio LLM y enviar peticiones de completado de chat (ChatCompletions). |
| `sentence_transformers` | Carga de los modelos Hugging Face para convertir instantáneamente cadenas de texto a vectores flotantes ("embeddings"). |
| `numpy` | Resolución de operaciones vectoriales implementando la fórmula manual de la similitud del coseno. |
| `pymongo` | Driver de Python utilizado para conectarse a MongoDB Atlas, almacenar colecciones de documentos con sus embeddings y ejecutar búsquedas vectoriales mediante pipelines de agregación (`$vectorSearch`). |

## 📁 Archivos
| Archivo | Tipo | Descripción |
|---|---|---|
| `mini_rag_from_scratch.ipynb` | Notebook | Implementación completa interactiva ilustrando la instalación de dependencias, generación de embeddings de textos, cálculo manual de similitud, persistencia de vectores en MongoDB Atlas, ejecución de búsquedas vectoriales remotas con `$vectorSearch` y orquestación con LLM externo. |

## 🔗 Relación con otros temas
Este tema introduce de forma exploratoria conceptos propios de IA generativa aplicada, que luego podrán ensamblarse e integrarse estructuralmente usando frameworks desplegados como los expurgados en la **UD10**.
