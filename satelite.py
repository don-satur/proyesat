from funciones_base import crear_objeto_skyfield, obtener_posicion

class satelite:
    def __init__(self, nombre, latitud, longitud, altitud_km):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.altitud_km = altitud_km

    def orbita(self):
        if self.altitud_km < 2000:
            return "LEO"
        elif self.altitud_km < 34000:
            return "MEO"
        elif self.altitud_km < 370000:
            return "GEO"
        else:
            return "HEO"
    
    def esta_en_zona(self, zona):
        lon_min, lat_min, long_max, lat_max = zona

        if (lon_min <= self.longitud <= lon_max) and (lat_min <= self.latitud <= lat_max):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.nombre} | {self.orbita()} | {self.altitud_km} km"

def crear_satelites(registros, momento):
    for reg in registros:
        try:
            obj_skyfield = crear_objeto_skyfield(reg)
            lat, lon, alt, = obtener_posicion(obj_skyfield, momento)

            if alt >= 100.0:
                nombre = reg.get("OBJECT_NAME", "Desconocido")
                satelite = Satelite(nombre, lat, lon, alt)
                lista_satelites.append(satelite
        except (KeyError, ValueError, TypeError):
            continue
    return lista_satelites