Proyecto Satélites

Proyecto desarrollado para la asignatura Programación 1 de la carrera Ingeniería Electrónica de la Universidad Nacional de Río Negro (UNRN).

Descripción

El proyecto consiste en procesar y analizar información de satélites artificiales a partir de un archivo JSON que contiene los datos de 16.822 satélites activos.

Mediante diferentes módulos desarrollados en Python, se realiza la lectura y organización de los datos, la clasificación de los satélites según sus grupos y el análisis de sus características orbitales.

También se utiliza la biblioteca Skyfield para calcular posiciones de satélites y estudiar su comportamiento en distintas zonas geográficas.

Los resultados del análisis se presentan mediante un informe desarrollado en Jupyter Notebook.

Integrantes

Ali Relmuan: [Creacion del .gitignore, cambios de rama de HEAD a MAIN para facilitar la interaccion en el repositorio, correciones en satelite.py,
creacion de analisis.py, creacion del README.md].
[Alan David Orosco]: [Creacion e inicializacion del Repositorio Proyesat, organizacion y administracion de los datos del proyecto (/datos, delegacion de funciones_base.py, 
creacion de catalogo.py, satelites.py, creacion de informe.ipynb].



Estructura del proyecto

satelites/
│
├── datos/
│   └── satelites.json
│
├── catalogo.py
├── satelite.py
├── analisis.py
├── funciones_base.py
├── informe.ipynb
├── README.md
└── .gitignore

Requisitos

Python 3.

Skyfield.

Libreria NumPy y Matplotlib.

JupyterLab.

Ejecución del proyecto

Clonar el repositorio:

git clone URL_DEL_REPOSITORIO

Ingresar a la carpeta del proyecto:

cd satelites

Activar el entorno virtual:

source .venv/bin/activate

Iniciar JupyterLab:

python -m jupyterlab

Abrir el archivo informe.ipynb y ejecutar las celdas del notebook.

