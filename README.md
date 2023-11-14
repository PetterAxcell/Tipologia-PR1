# Práctica 1: Web Scrapping

## Descripción
Esta práctica se ha realizado bajo el contexto de la asignatura _Tipología y ciclo de vida de los datos_, perteneciente al _Máster en Ciencia de Datos de la Universitat Oberta de Catalunya_. En ella, se aplican técnicas de web scraping mediante el lenguaje de programación Python para extraer así datos de la web PlaneCrashInfo y generar un dataset.

## Uso
Para ejecutar el programa es necesario instalar las dependencias que se encuentran en el requirements.txt.
Y ejecutar el siguiente código:

    > python3 source/main.py  


## Ficheros

### Carpeta source
- source/main.py: punto de entrada en el programa. Inicio del proceso de scrapping.
- source/settings.py: fichero de creación y configuración del driver.
- navigatation/navigate.py: fichero que almacena toda la lógica de navegación del proyecto.
- commands/command.py: fichero en el que se implementa las interacciones con la página web.
- extract/extract.py: fichero encargado de recopilar la información de los productos.
- save/save.py: fichero que almacena en diferentes formatos la información extraida

### Carpeta data
- data/csv/dataset.csv: se guarda en formato csv los productos obtenidos.
- data/img/*: se guardan las imagenes extraidas de los productos.

## Miembros del equipo

### [👤](https://www.linkedin.com/in/gorka-pineda-burgue%C3%B1o/) Gorka Pineda Burgueño
Ingeniero en informática (mención en tecnologia de la información y comunicación) e ingeniero en sistemas de telecomunicaciones. Cofundador de la consultora tecnológica, NordlyArrow, y actualmente cursando el máster de Data Science.

Trabajo como técnico de investigación en machine learning y blockchain. Además he realizado las prácticas en ITnow, en las que estuve como ingeniero de sistemas y TI, y finalmente los últimos meses hice Data science.

### [👤](https://www.linkedin.com/in/PetterAxcell) Petter Axcell Peñafiel Macías
Ingeniero en informática (mención en tecnologia de la información y comunicación) e ingeniero en sistemas de telecomunicaciones. Cofundador de la consultora tecnológica, NordlyArrow, y actualmente cursando el máster de Data Science, con aspiración de continuar mis estudios en el máster en Inteligencia Artificial.

He trabajado como programador junior desarrollando soluciones web y web scraping, durante mi último año estube como técnico de investigación en compresión de datos basado en machine learning. Además mi anterior trabajo fue gestionando clústeres (HPC) aplicando técnicas de orquestación mediante SLURM en CentOs/Rocky. Actualmente me encuentro como técnico de investigación en el hospital clínico.

## DOI de Zenodo
[10.5281/zenodo.10125871](https://doi.org/10.5281/zenodo.10125871)

## Consideraciones
Si se desea alamcenar los datos en formato json, hay que crear primero la carpeta "data/json"

## Recursos
1. Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
2. Mitchel, R. (2015). Web Scraping with Python: Collecting Data from the Modern Web. O'Reilly Media, Inc. Chapter 1. Your First Web Scraper.

