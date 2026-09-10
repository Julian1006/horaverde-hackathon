"""Pide los datos de la red electrica a la API de Carbon Intensity.

Todo lo que tiene que ver con internet esta metido aqui, asi el resto del
proyecto solo tiene que llamar a estas funciones y no se entera de nada.
"""

import requests

URL_BASE = "https://api.carbonintensity.org.uk"

# Si la pagina tarda mas de 10 segundos, mejor rendirse que quedarse colgado.
ESPERA_MAXIMA = 10

# La API contesta en ingles y yo quiero enseñarlo en español.
NOMBRES = {
    "wind": "viento",
    "solar": "sol",
    "nuclear": "nuclear",
    "gas": "gas",
    "coal": "carbon",
    "biomass": "biomasa",
    "hydro": "agua",
    "imports": "importada",
    "other": "otras",
}

# La API dice "low", "moderate" o "high". Lo paso a español.
NIVELES = {
    "very low": "muy limpia",
    "low": "limpia",
    "moderate": "normal",
    "high": "sucia",
    "very high": "muy sucia",
}


def _pedir(camino):
    """Le pide algo a la API y devuelve la respuesta convertida a diccionario.

    El guion bajo del principio quiere decir "esto es de uso interno",
    o sea que solo lo usan las otras funciones de este archivo.
    """
    respuesta = requests.get(
        URL_BASE + camino,
        headers={"Accept": "application/json"},
        timeout=ESPERA_MAXIMA,
    )
    respuesta.raise_for_status()
    return respuesta.json()


def intensidad_actual():
    """Cuanto CO2 cuesta la luz ahora mismo.

    Devuelve un diccionario con los gramos por kWh y si eso es mucho o poco.
    """
    datos = _pedir("/intensity")
    ahora = datos["data"][0]

    # A veces el dato medido todavia no esta y viene vacio.
    # En ese caso uso el que habian pronosticado.
    medido = ahora["intensity"]["actual"]
    pronosticado = ahora["intensity"]["forecast"]

    return {
        "gramos": medido if medido is not None else pronosticado,
        "indice": ahora["intensity"]["index"],
        "nivel": NIVELES.get(ahora["intensity"]["index"], "no se sabe"),
        "desde": ahora["from"],
        "hasta": ahora["to"],
    }


def mezcla_actual():
    """De donde viene la luz ahora mismo.

    Devuelve una lista de parejas (fuente, porcentaje), ordenada de la que
    mas manda a la que menos.
    """
    datos = _pedir("/generation")
    mezcla = datos["data"]["generationmix"]

    fuentes = []
    for fuente in mezcla:
        nombre = NOMBRES.get(fuente["fuel"], fuente["fuel"])
        fuentes.append((nombre, fuente["perc"]))

    fuentes.sort(key=lambda pareja: pareja[1], reverse=True)
    return fuentes


# Esto solo se ejecuta si lanzo este archivo directamente.
# Si lo importa otro archivo, no pasa nada. Sirve para probar.
if __name__ == "__main__":
    ahora = intensidad_actual()
    print("La luz esta a", ahora["gramos"], "gramos de CO2 por kWh")
    print("O sea que la luz esta", ahora["nivel"])
    print()
    print("Ahora mismo viene de:")
    for nombre, porcentaje in mezcla_actual():
        if porcentaje > 0:
            print("  ", nombre, "->", porcentaje, "%")
