# 🚀 Proyecto ETL End-to-End

**Airflow + dbt + Spark + Great Expectations**

Pipeline de datos completo que automatiza la ingesta, transformación, validación y exposición de datos, siguiendo buenas prácticas de ingeniería de datos.

---

## 📌 Descripción

Este proyecto implementa un pipeline ETL moderno que:

* Orquesta flujos de datos con Apache Airflow
* Procesa grandes volúmenes con Apache Spark
* Modela datos con dbt (ELT)
* Valida calidad con Great Expectations
* Expone resultados mediante una arquitectura lista para consumo

El objetivo es garantizar **datos confiables, trazables y reproducibles**.

---

## 🧱 Arquitectura

```text
Fuentes de Datos
     ↓
Airflow (Orquestación DAGs)
     ↓
Spark (Procesamiento distribuido)
     ↓
dbt (Transformación ELT)
     ↓
Great Expectations (Calidad de datos)
     ↓
Data Warehouse / Consumo
```

---

## 🛠️ Tecnologías

* Apache Airflow → Orquestación de workflows
* Apache Spark → Procesamiento distribuido
* dbt → Transformación de datos (ELT)
* Great Expectations → Validación de calidad
* PostgreSQL → Base de datos
* Docker & Docker Compose → Contenerización

---

## 📂 Estructura del Proyecto

```text
taller_etl_master/
│
├── dags/                  # DAGs de Airflow
├── dbt/
│   ├── profiles.yml
│   └── proyecto_unl/
│       ├── models/
│       │   ├── staging/
│       │   ├── intermediate/
│       │   └── marts/
│       ├── macros/
│       ├── tests/
│       └── dbt_project.yml
│
├── gx/                    # Great Expectations
├── scripts/               # Scripts auxiliares
├── config/                # Configuraciones
├── docker-compose.yaml
├── Dockerfile
└── requirements.txt
```

---

## ⚙️ Cómo ejecutar el proyecto

### 1️⃣ Clonar repositorio

```bash
git clone https://github.com/TU-USUARIO/taller_etl_master.git
cd taller_etl_master
```

---

### 2️⃣ Levantar entorno con Docker

```bash
docker-compose up -d --build
```

---

### 3️⃣ Acceder a servicios

* Airflow UI: http://localhost:8080
* Usuario: `admin`
* Password: `admin`

---

### 4️⃣ Ejecutar pipeline

Desde Airflow:

1. Activar DAG principal
2. Ejecutar flujo ETL

---

## 🔄 Flujo del Pipeline

1. Ingesta de datos (APIs / archivos)
2. Procesamiento con Spark
3. Transformación con dbt
4. Validación con Great Expectations
5. Carga en base de datos
6. Documentación automática

---

## 📊 Calidad de Datos

Se implementan validaciones como:

* Valores nulos en columnas críticas
* Consistencia de tipos de datos
* Unicidad de claves
* Rangos válidos

---

## 📚 Documentación (dbt)

Generar documentación:

```bash
dbt docs generate
```

Visualizar:

```bash
dbt docs serve
```

---

## 🧪 Pruebas

```bash
dbt test
```

Incluye validaciones de integridad y calidad de datos.

---

## 🚀 Características

* Pipeline modular y escalable
* Separación de responsabilidades
* Validación automática de datos
* Documentación integrada
* Arquitectura lista para producción

---

## 🔮 Mejoras Futuras

* Monitoreo con Prometheus / Grafana
* CI/CD con GitHub Actions
* Despliegue en la nube (AWS / GCP / Azure)
* Alertas automáticas en Airflow

---

## 👨‍💻 Autor

Wilson Iriarte

Carolina Paz

---

## ⭐ Notas

Este proyecto fue desarrollado como práctica de ingeniería de datos, aplicando herramientas modernas del ecosistema ETL.
