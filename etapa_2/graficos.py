import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

Path("salidas").mkdir(exist_ok=True)

def graficar_lanzamientos(lanzamientos, guardar=True):
    anios = list(lanzamientos.keys())
    cantidades = list(lanzamientos.values())

    plt.figure(figsize=(10, 8))
    plt.bar(anios, cantidades, color='royalblue', edgecolor='black', linewidth=0.5)
    plt.xlabel("Año de lanzamiento")
    plt.ylabel("Cantidad de satélites")
    plt.title("Lanzamientos de satélites activos por año")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    if guardar:
        plt.savefig("salidas/lanzamientos_por_anio.png", dpi=300)
    plt.show()

def graficar_lanzamientos_apilados(dic_starlink, dic_resto, guardar=True):
    anios_unicos = sorted(list(set(dic_starlink.keys()) | set(dic_resto.keys())))
    
    vals_1 = [dic_starlink.get(anio, 0) for anio in anios_unicos]
    vals_2 = [dic_resto.get(anio, 0) for anio in anios_unicos]
    
    plt.figure(figsize=(12, 6))
    plt.bar(anios_unicos, vals_1, label="Starlink", color='tab:blue')
    plt.bar(anios_unicos, vals_2, bottom=vals_1, label="Resto", color='tab:orange')
    
    plt.xlabel("Año de lanzamiento")
    plt.ylabel("Cantidad de satélites")
    plt.title("Comparación de lanzamientos: Starlink vs. Resto")
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    if guardar:
        plt.savefig("salidas/lanzamientos_apilados.png", dpi=300)
    plt.show()

def graficar_altitud_media(resumen, guardar=True):
    grupos = list(resumen.keys())
    medias = [resumen[g]["media"] for g in grupos]
    
    plt.figure(figsize=(10, 5))
    plt.bar(grupos, medias, color='forestgreen', edgecolor='black', linewidth=0.5)
    plt.xlabel("Grupo")
    plt.ylabel("Altitud media (km)")
    plt.title("Altitud media por grupo de satélites")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    if guardar:
        plt.savefig("salidas/altitud_media_grupos.png", dpi=300)
    plt.show()

def graficar_altitudes_leo(satelites, ancho_bin, guardar=True):
    altitudes = [s.altitud_km for s in satelites if 200 <= s.altitud_km <= 2000]
    bins = np.arange(200, 2000 + ancho_bin, ancho_bin)
    
    plt.figure(figsize=(10, 5))
    plt.hist(altitudes, bins=bins, color='purple', edgecolor='black', linewidth=0.5)
    plt.xlabel("Altitud (km)")
    plt.ylabel("Frecuencia")
    plt.title(f"Histograma de altitudes LEO (ancho de bin: {ancho_bin} km)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    if guardar:
        plt.savefig(f"salidas/histograma_leo_bin{ancho_bin}.png", dpi=300)
    plt.show()

def graficar_altitudes_log(satelites, guardar=True):
    """Histograma de todas las altitudes en escala logarítmica."""
    altitudes = [s.altitud_km for s in satelites if s.altitud_km > 0]
    min_alt = max(min(altitudes), 1)
    max_alt = max(altitudes)
    
    bins = np.logspace(np.log10(min_alt), np.log10(max_alt), 50)
    
    plt.figure(figsize=(10, 5))
    plt.hist(altitudes, bins=bins, color='teal', edgecolor='black', linewidth=0.5)
    plt.xscale("log")
    plt.xlabel("Altitud (km) - Escala Logarítmica")
    plt.ylabel("Frecuencia")
    plt.title("Distribución global de altitudes (Escala Log)")
    plt.grid(True, which="both", linestyle='--', alpha=0.5)
    plt.tight_layout()
    
    if guardar:
        plt.savefig("salidas/histograma_altitudes_log.png", dpi=300)
    plt.show()

def graficar_inclinaciones(registros, guardar=True):
    inclinaciones = []
    for reg in registros:
        inc = reg.get("INCLINATION")
        if inc is not None:
            try:
                inclinaciones.append(float(inc))
            except (ValueError, TypeError):
                continue
                
    bins = np.arange(0, 181, 1)
    
    plt.figure(figsize=(10, 5))
    plt.hist(inclinaciones, bins=bins, color='crimson', edgecolor='black', linewidth=0.2)
    plt.xlabel("Inclinación (grados)")
    plt.ylabel("Frecuencia")
    plt.title("Distribución de inclinaciones orbitales (0° - 180°)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    if guardar:
        plt.savefig("salidas/histograma_inclinaciones.png", dpi=300)
    plt.show()




### Bloque adicional para la presentación
from catalogo import anio_lanzamiento, grupo

def graficar_evolución_constelaciones(registros, grupos_intereses=None, anio_inicio=2015, anio_fin=2026, guardar=True):
    if grupos_intereses is None:
        grupos_intereses = ["Starlink", "OneWeb", "Planet", "Iridium", "GPS"]

    anios = list(range(anio_inicio, anio_fin + 1))
    conteos = {g: {a : 0 for a in anios} for g in grupos instereses}

    for reg in registros:
        g = grupo(reg["OBJECT_NAME"])
        if g in conteos:
            a = anio_lanzamiento(reg)
            if anio_inicio <= a <= anio_fin:
                conteo[g][a] += 1

    plt.figure(figsize=(12,6))
    for g in grupos_interes:
        valores = [conteos[g][a] for a in anios]
        plt.plot(anios, valores, marker="o", linewith=2, label=g)

    plt.title(f"Evolución de lanzamientos por constelación ({anio_inicio}–{anio_fin})")
    plt.xlabel("Año de lanzamiento")
    plt.ylabel("Cantidad de satélites lanzados")
    plt.xticks(anios)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()

    if guardar:
        plt.savefig("salidas/evolucion_constelaciones.png", dpi=300)
    plt.show()