# Análisis del Mercado Laboral de Datos - Perú 2026 📊🇵🇪

## 📝 Descripción
Este proyecto es un análisis integral del mercado laboral tecnológico en Perú, enfocado en roles de **Data Science, Analytics e Ingeniería de Datos**. A través de técnicas de Web Scraping y procesamiento de datos, he consolidado una base de datos real que permite identificar las tecnologías más demandadas, rangos salariales y sectores con mayor crecimiento para el año 2026.

Este repositorio forma parte de mi portafolio profesional para la búsqueda de **prácticas pre-profesionales**, demostrando mi capacidad para manejar el ciclo completo del dato: Extracción, Limpieza, Almacenamiento y Visualización.

---

## 🚀 Características Principales
* **Web Scraping:** Automatización de la extracción de vacantes de portales como LinkedIn e Indeed usando Python.
* **Procesamiento de Datos (ETL):** Limpieza y normalización de más de 100 registros, manejando datos nulos y estandarizando etiquetas de habilidades.
* **Base de Datos:** Implementación de persistencia de datos mediante **SQLite**.
* **Dashboard Interactivo:** Creación de visualizaciones clave para la toma de decisiones basada en datos.

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.x
* **Librerías:** Pandas, NumPy, BeautifulSoup/Selenium.
* **Base de Datos:** SQL (SQLite).
* **Entorno:** Jupyter Notebooks / VS Code.
* **Visualización:** Power BI / Matplotlib.

---

## 📂 Estructura del Repositorio
```bash
├── data/
│   ├── jobs_raw_table.csv       # Datos originales sin procesar
│   └── jobs_cleaned_table.csv   # Dataset final optimizado para análisis
├── notebooks/
│   └── analysis.ipynb           # Análisis Exploratorio de Datos (EDA)
├── scripts/
│   ├── main.py                  # Script principal de ejecución
│   └── config.py                # Configuración de variables y selectores
└── database/
    └── jobs.db                  # Base de datos relacional del proyecto

````
## 📈 Insights del Mercado (Resultados)

A través del análisis realizado, se identificaron los siguientes puntos clave:

- **Herramientas Core:** El 85% de las vacantes de **"Data Analyst"** requieren dominio avanzado de **SQL** y **Excel**.
- **Crecimiento:** Las posiciones de **Data Engineer** han mostrado un incremento del **20%** en sectores de **banca y finanzas**.
- **Modalidad:** El trabajo **Remoto/Híbrido** predomina en el **65%** de las ofertas para perfiles **Junior**.

---

## ⚙️ Configuración e Instalación

### Clonar el repositorio


git clone https://github.com/tu-usuario/data-analysis-peru-2026.git

⚙️ Configuración e Instalación

1. Clonar el repositorio:

git clone [https://github.com/tu-usuario/data-analysis-peru-2026.git](https://github.com/tu-usuario/data-analysis-peru-2026.git)

2.Instalar dependencias:

pip install -r requirements.txt

3.Ejecutar el análisis:

Abre el archivo analysis.ipynb en Jupyter o ejecuta el script principal:
python main.py
