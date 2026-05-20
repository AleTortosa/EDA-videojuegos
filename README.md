## EDA videojuegos

### 1) Objetivo
- Analizar y visualizar el dataset de ventas de videojuegos para entender patrones de distribución, géneros predominantes, plataformas principales y evolución temporal de ventas.
- Aplicar proceso completo de limpieza de datos, construcción de características y generación de visualizaciones reproducibles.
- Mantener estructura modular con código reutilizable en `src/` y notebook ejecutable en `notebooks/eda.ipynb`.

### 2) Dataset
- Fuente: Archivo CSV `data/raw/vgsales.csv`
- Nº filas/columnas: 16.598 filas × 11 columnas (antes de limpieza); 11.493 × 11 (después)
- Variables clave:
  - Numéricas: `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`, `Global_Sales`, `Year`, `Rank`
  - Categóricas: `Name`, `Platform`, `Genre`, `Publisher`
- Rango temporal: 1980 a 2020
- Datos faltantes: `Year` (271 nulos), `Publisher` (58 nulos)

### 3) Preguntas
- Q1: ¿Cómo se distribuyen las ventas globales?
- Q2: ¿Qué géneros y plataformas son más comunes?
- Q3: ¿Existe correlación entre ventas de diferentes regiones (NA, EU, JP)?
- Q4: ¿Cuáles fueron los años con mayor indice de lanzamientos de videojuegos?

### 4) Data issues & fixes
- Valores faltantes en `Year` → Eliminación de filas con Year nulo en `src/cleaning.py`
- Valores faltantes en `Publisher` → Imputación con valor 'Unknown' en `src/cleaning.py`
- Formato incorrecto de `Year` (float) → Conversión a entero después de limpiar nulos
- `Name` duplicados por `Platform` → Combinación de filas para mismo juego

### 5) Pipeline
- raw → clean → features → viz → export a `data/processed/clean_dataset.csv`
- Pasos detallados:
  1. `load_csv()` en `src/io.py` carga el CSV
  2. `clean()` en `src/cleaning.py` maneja nulos y convierte tipos
  3. `build_features()` en `src/features.py` agrega por nombre y calcula ratios
  4. `plot_graph()` en `src/viz.py` genera visualizaciones
  5. Exporta DataFrame limpio a `data/processed/`

### 6) Hallazgos
- Insight 1: Distribución altamente sesgada de ventas globales — más del 50% de juegos vende < 0.17M, solo algunos títulos alcanzan ventas masivas (ver histograma con rango < 1M)
- Insight 2: Géneros predominantes son `Action` (3.316 juegos), `Sports` (2.346) y `Misc` (1.739)
- Insight 3: Plataformas líderes son `DS` (2.163), `PS2` (2.161) y `PS3` (1.329) — predominan consolas de Nintendo y Sony
- Insight 4: Correlación fuerte entre `NA_Sales` y `EU_Sales` (r≈0.77) — mercados de Norteamérica y Europa se mueven juntos
- Insight 5: Años 2008-2010 concentran mayores ventas globales (678.9M, 667.3M, 611.1M) — pico de mercado a fines de 2000s

### 7) Estructura del proyecto
- `src/` contiene funciones reutilizables:
  - `io.py` — carga de CSV
  - `cleaning.py` — limpieza y transformación de datos
  - `config.py` — rutas centralizadas (RAW_PATH, OUT_PATH)
  - `features.py` — construcción de características (agregación, ratios)
  - `viz.py` — generación de gráficas (histogramas, scatter, heatmap)
  - `utils.py` — utilidades generales (validaciones)
- `main.py` ejecuta el pipeline end-to-end
- `notebooks/eda.ipynb` análisis interactivo

### 8) Cómo ejecutar
- `pip install -r requirements.txt`
- Ejecutar pipeline: `python main.py`
- (Opcional) Abrir y ejecutar: `jupyter notebook notebooks/eda.ipynb`

## Estructura

```
project/
├── main.py
├── data/
│   ├── raw/
│   │   └── vgsales.csv 
│   └── processed/
├── notebooks/
│   └── eda.ipynb
├── src/
│   ├── __init__.py
│   ├── io.py
│   ├── cleaning.py
│   ├── config.py
│   ├── features.py
│   ├── viz.py
│   └── utils.py
├── README.md
├── .gitignore
└── requirements.txt

```
