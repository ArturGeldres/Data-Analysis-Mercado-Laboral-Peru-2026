# 📊 Análisis del Mercado Laboral Tech en Perú 2026
## Proyecto de Data Analytics & Engineering para la Toma de Decisiones Estratégicas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQL](https://img.shields.io/badge/SQL-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Data_Analysis](https://img.shields.io/badge/Data_Analysis-EDA-success?style=for-the-badge)

### 🎯 Objetivo del Proyecto
Desarrollar un flujo completo de datos (End-to-End) para identificar las tendencias de contratación en el sector tecnológico peruano. Este proyecto demuestra mis capacidades en **Web Scraping, Limpieza de Datos, Modelado SQL y Análisis Estadístico**, orientados a resolver problemas reales de mercado.

---

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python (Pandas, Numpy).
* **Almacenamiento:** SQLite para la persistencia y estructuración de datos.
* **Entorno:** Jupyter Notebook para la documentación del proceso analítico.
* **Otras herramientas:** Exel (Power Query)

---

## 🚀 Flujo de Trabajo (Pipeline de Datos)

### 1. Extracción (Scraping)
Se diseñó un script robusto para recolectar vacantes de portales líderes (LinkedIn, Indeed), obteniendo datos como: Cargo, Empresa, Ubicación, Modalidad y Descripción.
<img width="1522" height="926" alt="Script de Extracción" src="https://github.com/user-attachments/assets/dd3abc08-eef5-4612-8c78-c3fec4815a0d" />


### 2. Procesamiento y Limpieza (ETL)
Transformación de datos crudos en información accionable:
* Normalización de salarios y ubicaciones.
* Categorización de roles (Data Analyst, Scientist, Engineer, BI).
* Manejo de valores nulos y duplicados para asegurar la integridad del análisis.

### 3. Almacenamiento Estructurado
Los datos procesados se cargan en una base de datos **SQLite**, permitiendo realizar consultas complejas para segmentar el mercado de manera eficiente.

---

## 📈 Insights y Resultados Clave

### A. Demanda por Rol
Análisis de qué posiciones son las más buscadas en el ecosistema actual.
<img width="1258" height="837" alt="Demanda por Rol" src="https://github.com/user-attachments/assets/4f0e1c56-fcf7-41b4-9c87-b79f418aa03e" />


### B. Habilidades Más Solicitadas (Hard Skills)
Identificación de las tecnologías críticas (SQL, Python, Power BI, etc.) mediante minería de texto en las descripciones.
<img width="922" height="721" alt="Habilidades Más Solicitadas" src="https://github.com/user-attachments/assets/b5518081-3a71-491d-8b24-0f32bdc4411f" />


### C. Geografía del Empleo
Mapa de calor de las ciudades con mayor concentración de ofertas en Perú.
<img width="1113" height="845" alt="Geografía del Empleo" src="https://github.com/user-attachments/assets/a446f549-0998-4d67-972a-7d43cf7a6d02" />


---

## 🧠 Aprendizajes y Desafíos
* **Desafío:** Manejo de datos no estructurados en las descripciones de empleo.
* **Solución:** Implementación de funciones de limpieza con expresiones regulares (RegEx) para extraer palabras clave de forma automática.
* **Logro:** Automatización de un reporte que reduce el tiempo de búsqueda de tendencias de semanas a minutos.

---

## 📂 Estructura del Proyecto
```text
├── main.py                # Ejecución del flujo principal
├── config.py              # Parámetros y configuraciones
├── data/
│   ├── jobs_raw.csv       # Datos crudos
│   └── jobs_cleaned.csv   # Datos listos para análisis
├── notebooks/
│   └── analysis.ipynb     # Análisis exploratorio (EDA)
└── database/
    └── jobs.db            # Base de datos SQLite
```
---
👤 Contacto
Arturo Geldres
Estudiante de 8vo Ciclo de Ingeniería de Sistemas e Informática - UTP

LinkedIn: https://www.linkedin.com/in/arturo-geldres/

Portafolio: https://github.com/ArturGeldres

Email: arturo.gelderland@gmail.com
