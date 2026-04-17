# Modelos de Lenguaje y RAG

> Asignatura: Sistemas de Big Data  
> Curso de Especialización en Inteligencia Artificial y Big Data

## 📌 Descripción
Este bloque temático se centra en la implementación práctica de un sistema RAG (Retrieval-Augmented Generation) minimalista. A través de un cuaderno de Jupyter, se aborda el proceso completo de generación de embeddings, recuperación de información basada en similitud del coseno y la integración con grandes modelos de lenguaje (LLMs) mediante APIs para generar respuestas fundamentadas en un contexto empírico inyectado.

## 🎯 Objetivos de Aprendizaje
- Comprender la arquitectura de soporte y flujo básico de un sistema RAG.
- Implementar la vectorización de textos estáticos utilizando modelos ligeros basados en Sentence Transformers.
- Calcular y aplicar la métrica matemática de similitud del coseno con NumPy para la recuperación de contexto relevante.
- Orquestar llamadas remotas a LLMs mediante interfaces compatibles con OpenAI y construir prompts contextualizados.

## 🧠 Contenidos
El módulo explora el ciclo completo de la Generación Aumentada por Recuperación en su forma más pura. Comienza cargando un modelo de vectorización ligero localizado (`paraphrase-MiniLM-L3-v2`) para codificar fragmentos de conocimiento en un espacio hiperdimensional. Se detiene especialmente en exponer de forma programática cómo comparar la consulta de entrada vectorial (pregunta de usuario) contra la base de conocimientos empleando funciones directas (similitud de coseno). Seguidamente, extrae aquellos bloques de texto cuya similitud sobrepasa un umbral y los ensambla en un `prompt`. Este prompt compuesto se transfiere a un modelo gigante servido externamente (`gpt-oss-120b:cerebras`) logrando generar respuestas acotadas al material aportado, minimizando alucinaciones.

### Extracción Semántica
Se expone una función central (`get_context`) que itera comparativamente la codificación de la consulta frente a las piezas de datos, filtrando resultados de alta pertinencia asistiéndose de álgebra vectorial. 

### Inferencia y Prompting
Mediante el cliente de OpenAI (reestructurando la base_url hacia Hugging Face), se configura el rol del LLM (Tutor) y se restringen de forma estricta sus predicciones al bloque referenciado. Para preguntas ausentes en el corpus inyectado, se fuerza al modelo a declarar su desconocimiento mediante reglas impuestas.

## 🛠️ Tecnologías y Librerías
| Herramienta | Uso en este tema |
|---|---|
| `openai` | Interfaz cliente utilizada para conectarse al servicio LLM y enviar peticiones de completado de chat (ChatCompletions). |
| `sentence_transformers` | Carga de los modelos Hugging Face para convertir instantáneamente cadenas de texto a vectores flotantes ("embeddings"). |
| `numpy` | Resolución de operaciones vectoriales implementando la fórmula manual de la similitud del coseno. |

## 📁 Archivos
| Archivo | Tipo | Descripción |
|---|---|---|
| `mini-rag-from-scratch.ipynb` | Notebook | Implementación completa interactiva ilustrando la instalación de dependencias, descarga de modelos perimetrales, matriz de contexto, creación del orquestador y consumo de LLM externo. |

## 🔗 Relación con otros temas
Este tema introduce de forma exploratoria conceptos propios de IA generativa aplicada, que luego podrán ensamblarse e integrarse estructuralmente usando frameworks desplegados como los expurgados en la **UD10**.
