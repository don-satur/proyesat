import json
from pathlib import Path

grupos = {
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
