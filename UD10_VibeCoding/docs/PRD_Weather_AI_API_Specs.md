# Especificaciones del Proyecto: API de Consulta Meteorológica con IA

## 1. Descripción del Proyecto
El objetivo es desarrollar un servicio que integre modelos de Inteligencia Artificial para la creación de una **API REST** funcional que consuma y transforme datos meteorológicos en tiempo real.

---

## 2. Requisitos del Software

### Funcionalidad de la API
* **Endpoint Único:** Se requiere la publicación de al menos un endpoint de consulta.
* **Origen de Datos:** Los datos deben obtenerse de la siguiente URL externa:
    > `https://api.open-meteo.com/v1/forecast?latitude=39.47&longitude=-0.38&current_weather=true`
* **Formato de Respuesta:** La respuesta del servicio debe estar formateada y exponer obligatoriamente:
    * **Temperatura:** En dos unidades distintas (ej. Celsius y Fahrenheit).
    * **Velocidad del viento:** En dos unidades distintas (ej. km/h y m/s).

### Calidad y Pruebas
* **Tests Unitarios:** Es imperativo incluir pruebas unitarias para:
    * Métodos de transformación de unidades.
    * Cualquier lógica de negocio o método auxiliar considerado oportuno.

---

## 3. Entregables Obligatorios

1.  **Código Fuente:** El desarrollo completo del servicio API REST.
2.  **Documentación de Prompts:** Un documento anexo que detalle el **prompt (o conjunto de prompts)** exactos utilizados para la generación del código mediante IA.

---

## 4. Resumen Técnico de Conversión

Para los métodos de transformación se deben usar **exclusivamente** las siguientes fórmulas:

| Magnitud | Unidad A | Unidad B | Fórmula de Conversión |
| :--- | :--- | :--- | :--- |
| **Temperatura** | Celsius (°C) | Fahrenheit (°F) | $F = (C \times \frac{9}{5}) + 32$ |
| **Viento** | km/h | m/s | $V_{m/s} = V_{km/h} \div 3.6$ |

> **Nota importante:** Ambas fórmulas deben implementarse en funciones puras e independientes (separadas de los endpoints y de la lógica de negocio), de modo que puedan ser testeadas de forma aislada.