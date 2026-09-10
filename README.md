# HoraVerde

**No consumas menos electricidad. Consúmela a otra hora.**

Proyecto del hackathon sobre cambio climático. HoraVerde consulta en tiempo real
cuánto CO2 emite la electricidad de la red y te dice a qué hora conviene poner la
lavadora, cargar el coche o lanzar esa tarea pesada del ordenador.

---

## El problema

La electricidad no siempre contamina lo mismo. Cuando hace viento y sol, la red
se llena de renovables. Cuando no, entran a cubrir el hueco las centrales de gas.
La diferencia entre la mejor y la peor hora del día puede ser de varias veces en
gramos de CO2 por kilovatio-hora.

Casi nadie lo sabe, y quien lo sabe no tiene forma de consultarlo. Así que todos
consumimos a la hora que nos viene bien, que a menudo es la peor.

## La solución

Mover el consumo flexible a las horas limpias reduce emisiones **sin reducir el
consumo ni pedir ningún sacrificio**. La ropa se lava igual de limpia a las 3 de
la madrugada. Solo falta saber cuándo.

HoraVerde hace visible ese dato y lo convierte en una recomendación concreta:

1. **Ahora mismo** — cuánto CO2 emite cada kWh en este momento y qué mezcla de
   fuentes lo está generando.
2. **Las próximas 48 horas** — el pronóstico completo, para ver el patrón.
3. **La recomendación** — la mejor franja horaria para consumir, y cuánto CO2
   te ahorras respecto a la peor.

## Cómo funciona

```
API de intensidad de carbono
          |
          v
   Cliente Python  ->  Análisis: mejor y peor franja
          |
          +---> Web Flask (panel + gráfica)
          |
          +---> Bot de Discord (avisos al servidor)
```

## Stack

- **Python** — lógica y análisis
- **Flask + Jinja** — servidor web y plantillas
- **HTML + CSS** — interfaz
- **requests** — consumo de la API
- **discord.py** — bot de avisos
- **Entorno virtual** + **git/GitHub**

## Fuente de datos

[Carbon Intensity API](https://api.carbonintensity.org.uk/) del operador de red
británico. **Abierta, gratuita y sin clave de API.**

Endpoints usados:

| Endpoint | Para qué |
|---|---|
| `/intensity` | Intensidad actual (gCO2/kWh) e índice |
| `/intensity/{from}/fw48h` | Pronóstico de las próximas 48 horas |
| `/generation` | Mezcla de generación: eólica, solar, gas, nuclear... |

*Limitación conocida:* esta API cubre Gran Bretaña. La arquitectura es la misma
para cualquier otro operador que publique estos datos.

## Estado

**En desarrollo** — fase de definición completada.

- [x] Repositorio e idea consolidada
- [ ] Cliente de la API
- [ ] Web Flask con el dato actual
- [ ] Pronóstico y recomendación horaria
- [ ] Bot de Discord
- [ ] Pitch

## Instalación

> Pendiente: se completará cuando exista el código.

```bash
git clone <url-del-repo>
cd hackathon-clima
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Estructura

```
hackathon-clima/
├── README.md                  # Este archivo
├── IDEA.md                    # La idea consolidada y el plan
├── docs/
│   └── lluvia-de-ideas.md     # Fase de generación de ideas
└── .gitignore
```

## Documentación del proceso

- [IDEA.md](IDEA.md) — qué construimos, qué no, y el plan por lecciones
- [docs/lluvia-de-ideas.md](docs/lluvia-de-ideas.md) — las 6 candidatas y por qué
  ganó esta
