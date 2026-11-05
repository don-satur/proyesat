import json
from pathlib import Path

GRUPOS = {
    "STARLINK": "Starlink",
    "ONEWEB": "OneWeb",
    "KUIPER": "Kuiper",
    "QIANFAN": "Qianfan",
    "IRIDIUM": "Iridium",
    "GLOBALSTAR": "Globalstar",
    "NAVSTAR": "GPS",
    "BEIDOU": "BeiDou",
}

def leer_satelites(ruta):
    ruta = Path(ruta)
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"aviso: el archivo '{ruta}' no encontrado")
        return []
    except json.JSONDecodeError:
        print(f"aviso: el archivo {ruta}' no tiene formato JSON válido")
        return []

def anio_lanzamiento(registro):
    try:
        obj_id = registro.get("OBJECT_ID", "")
        return int(obj_id[:4])
    except (ValueError, TypeError):
        return None

def grupo(nombre):
    if not isinstance(nombre, str):
        return "Otros"

    nombre_upper = nombre.upper()
    for pref, nombre_grupo in GRUPOS.items():
        if nombre_upper.startswith(pref):
            return nombre_grupo
    return "Otros"

def contar_por_grupo(registros):
    conteo = {}
    for reg in registros:
        nombre = reg.get("OBJECT_NAME", "")
        g = grupo(nombre)
        conteo[g] = conteo.get(g, 0) + 1
    return conteo

def lanzamientos_por_anio(registros):
    conteo = {}
    for reg in registros:
        anio = anio_lanzamiento(reg)
        if anio is not None:
            conteo[anio] = conteo.get(anio, 0) +1
    return dict(sorted(conteo.items()))