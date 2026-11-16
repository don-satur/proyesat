# Proyecto Satélites

# Descripción del proyecto:

El proyecto consiste en procesar y analizar información de satélites artificiales a partir de un archivo JSON que contiene los datos de 16.822 satélites activos.

Mediante diferentes módulos desarrollados en Python, se realiza la lectura y organización de los datos, la clasificación de los satélites según sus grupos y el análisis de sus características orbitales.

También se utiliza la biblioteca Skyfield para calcular posiciones de satélites y estudiar su comportamiento en distintas zonas geográficas.

Los resultados del análisis se presentan mediante un informe desarrollado en Jupyter Notebook.


# Integrantes:

- Alan David Orosco: Creacion e inicializacion del Repositorio Proyesat, organizacion y administracion de los datos del proyecto (`/datos`, delegacion de `funciones_base.py`, creacion de `catalogo.py`, `satelites.py`, creacion del `informe.ipynb`.

- Ali Relmuan: Creacion del `.gitignore`, cambios de rama de HEAD a MAIN para facilitar la interaccion en el repositorio, correciones en `satelite.py`, creacion de `analisis.py`, creacion del `README.md`.


# Estructura del proyecto:

- `catalogo.py`: módulo encargado de la lectura del archivo JSON (`utf-8`), manejo de excepciones y clasificación de los satélites por grupos principales.

- `satelite.py`: módulo que define la clase `Satelite`, modelando su posición, cálculo de tipos de órbita (LEO, MEO, GEO, HEO) y validación de presencia en zonas geográficas.

- `analisis.py`: módulo que contiene funciones para cálculos estadísticos avanzados, extremos orbitales (más altos y más bajos) y filtrados geoespaciales.

- `funciones_base.py`: módulo que provee la integración con la biblioteca Skyfield para la creación de objetos y el cálculo de posiciones y trayectorias.

- `informe.ipynb`: notebook de Jupyter que integra el flujo completo del análisis del catálogo y muestra los resultados detallados.

- `datos/`: carpeta contenedora del archivo con las mediciones y registros de los satélites (`satelites.json`).

- `.gitignore`: archivo de exclusión para control de versiones con Git.

```text
satelites/
├── datos/
│   └── satelites.json
├── catalogo.py
├── satelite.py
├── analisis.py
├── funciones_base.py
├── informe.ipynb
├── README.md
└── .gitignore
```

# Cómo ejecutar el programa:

El proyecto se ejecuta mediante la activación de un entorno virtual y el uso de JupyterLab para correr el código del informe analítico.

- Clonar el repositorio:
```bash
git clone https://github.com/don-satur/proyesat.git
```
- Ingresar a la carpeta del proyecto:
```bash
cd satelites
```
- Activar el entorno virtual:
```bash
source .venv/bin/activate
```
- Ejecucuón desde la terminal:
```bash
python3 -c "import catalogo; print(len(catalogo.leer_satelites('datos/satelites.json')))"
```
Salida esperada:
```text
16822
```
- Ejemplo de dato faltante:

```bash
python3 -c "import catalogo; catalogo.leer_satelites('datos/no_existe.json')"
```
Salida esperada:
```text
aviso: el archivo 'datos/no_existe.json' no encontrado
```
- Iniciar JupyterLab:
```bashh
python -m jupyterlab
```

- Abrir el archivo `informe.ipynb` y ejecutar secuencialmente las celdas del notebook para procesar el catálogo y visualizar los resúmenes estadísticos, órbitas extremas y filtrados por zona.

# Requisitos

- Python 3
- Skyfield
- Libreria NumPy y Matplotlib
- JupyterLab