# Análisis y Modelado Visual con Power BI

> Asignatura: Sistemas de Big Data  
> Curso de Especialización en Inteligencia Artificial y Big Data

## 📌 Descripción
Unidad enmarcada en el extremo final de la cadena de datos (Visualización analítica o Business Intelligence). El objetivo es adquirir solvencia con Power BI transformando silos de información y registros crudos estáticos y tabulares en tableros de mando (Dashboards) accionables, medibles e intuitivos que apoyen la toma de decisiones basada en datos empíricos.

## 🎯 Objetivos de Aprendizaje
- Importar y sanear grandes volúmenes de datos usando Power Query.
- Sintetizar información elaborando métricas DAX de alto valor añadido.
- Configurar y componer visualizaciones estructuradas, mapas y gráficos comparativos de alto impacto.

## 🧠 Contenidos
La unidad experimenta con 3 ejes de datos (casos de uso) dispares para interiorizar las diferentes morfologías que adoptan los repositorios en crudo y su impacto visual final:

1. **Evaluadores Clásicos de Supervivencia (`Titanic.pbix`)**: Integración analítica predictiva básica que se fundamenta sobre atributos demográficos extraídos de `titanic.csv` para correlacionar factores como clase, edad, género y tarifas.
2. **Tablero Financiero Deportivo (`EquiposMasValiosos.pbix`)**: Un visor comercial que extrae valor, métricas absolutas y porcentajes de las escuadras futbolísticas top mundiales desde `most_valuable_teams.csv`, evaluando ligas y tamaño de plantillas empíricamente.
3. **Métricas Estudiantiles Propias (`iesabastospowerbi/`)**: Estudio exhaustivo multivariable uniendo las encuestas de satisfacción escolar (archivos `PE02...xlsx`) y los estadísticos de matrículas formales del IES Abastos. Permite identificar debilidades formativas visualmente aislando el ruido.

## 🛠️ Tecnologías y Librerías
| Herramienta | Uso en este tema |
|---|---|
| Microsoft Power BI | Software integral líder en BI para transformar flujos de orígenes heterogéneos en informes visuales nativamente distribuidos |
| Excel y CSV | Soporte inerte de almacenamiento principal |

## 📁 Archivos
| Archivo | Tipo | Descripción |
|---|---|---|
| `EquiposMasValiosos.pbix` | Informe Power BI | Tablero evaluativo ordenando financieramente las entidades de este deporte. |
| `Titanic.pbix` | Informe Power BI | Caso canónico de analítica demográfica de supervivencia modelizada. |
| `iesabastospowerbi/IES_Abastos.pbix` | Informe Power BI | Proyecto integrativo combinando encuestas complejas departamentales. |
| `most_valuable_teams.csv` | Dataset | Registro crudo de 100 ligas/equipos para el ejercicio asociado. |
| `titanic.csv` | Dataset | Tabular estructurado clásico de 891 registros sin sanear originario de Kaggle. |
| `*.xlsx` | Datos | Archivos extraídos ofimáticamente relativos a los diferentes test realizados e ingestados en BI. |
