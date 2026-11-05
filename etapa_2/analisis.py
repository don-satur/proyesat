from catalogo import grupo


def mas_bajo(satelites):
    return min(satelites, key=lambda satelite: satelite.altitud_km)


def mas_alto(satelites):
    return max(satelites, key=lambda satelite: satelite.altitud_km)


def en_zona(satelites, zona):
    resultado = []

    for satelite in satelites:
        if satelite.esta_en_zona(zona):
            resultado.append(satelite)

    return resultado


def ordenar_por(satelites, atributo, descendente=False):
    return sorted(
        satelites,
        key=lambda satelite: getattr(satelite, atributo),
        reverse=descendente
    )


def top_n(satelites, n, mas_altos=True):
    ordenados = ordenar_por(satelites, "altitud_km", descendente=mas_altos)

    return ordenados[:n]


def resumen_por_grupo(satelites):
    grupos = {}

    for satelite in satelites:
        nombre_grupo = grupo(satelite.nombre)

        if nombre_grupo not in grupos:
            grupos[nombre_grupo] = []

        grupos[nombre_grupo].append(satelite.altitud_km)

    resumen = {}

    for nombre_grupo, altitudes in grupos.items():
        resumen[nombre_grupo] = {
            "cantidad": len(altitudes),
            "minima": min(altitudes),
            "media": sum(altitudes) / len(altitudes),
            "maxima": max(altitudes)
        }

    return resumen

def contar_por_tipo(satelites):
    cantidades = {
        "LEO": 0,
        "MEO": 0,
        "GEO": 0,
        "HEO": 0
    }

    for satelite in satelites:
        tipo = satelite.orbita()
        cantidades[tipo] += 1

    return cantidades    