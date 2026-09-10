# HoraVerde

La electricidad no contamina siempre lo mismo. Depende de si en ese momento
está soplando el viento o si han tenido que encender las centrales de gas para
cubrir el hueco.

HoraVerde mira ese dato en tiempo real y te dice a qué hora te conviene poner
la lavadora.

Es mi proyecto para el hackathon de cambio climático del bootcamp.

## De dónde sale la idea

Estuve dando vueltas a unas cuantas ideas y casi todas acababan en lo
mismo: pedirle a la gente que consuma menos. Eso ya está muy visto, y además
cansa a todo el mundo.

Buscando datos me encontré con que los operadores de red publican cuántos gramos
de CO2 cuesta producir cada kWh, actualizado cada media hora. Y resulta que
varía bastante a lo largo del día.

Ahí estaba el proyecto. No hace falta consumir menos: con consumir a otra hora
ya ganas algo. Y a nadie le importa que la lavadora termine a las tres de la
mañana.

## Qué enseña

- Cuánto CO2 emite la red ahora mismo y de dónde sale esa electricidad
  (eólica, gas, nuclear, solar...)
- El pronóstico de las próximas 48 horas
- La mejor y la peor franja para consumir, y cuánto te ahorras eligiendo bien

Mientras escribía esto la red estaba a 79 gCO2/kWh con un 57 % de eólica.
Dentro de unas horas será una cifra completamente distinta, y esa es justo la
gracia del asunto.

## Los datos

Tiro de la [Carbon Intensity API](https://api.carbonintensity.org.uk/) del
operador de red británico. Es gratis y no pide clave, que para un hackathon es
exactamente lo que necesitas: cero tiempo perdido esperando credenciales.

Lo malo es que solo cubre Gran Bretaña. Si algún día quisiera cubrir España
habría que cambiar la fuente de datos, pero el resto del código valdría igual.

Los tres endpoints que uso:

- `/intensity` — lo que está pasando ahora mismo
- `/intensity/{desde}/fw48h` — el pronóstico
- `/generation` — de qué fuentes viene la electricidad en este momento

## Con qué está hecho

Python y Flask, con plantillas Jinja y CSS escrito a mano. Para hablar con la
API, requests. El bot de Discord, con discord.py.

Todo son cosas del curso. La gracia estaba en juntar el módulo de web con el de
bots en un mismo proyecto en vez de quedarme en uno solo.

## Por dónde voy

En definición. Tengo la idea cerrada y la API ya probada, pero el código
todavía no está.

- [x] Idea consolidada y repo montado
- [ ] Cliente de la API
- [ ] La web enseñando el dato de ahora mismo
- [ ] El pronóstico y la recomendación de hora
- [ ] Bot de Discord

## Para arrancarlo

Cuando haya algo que arrancar, será esto:

```bash
git clone https://github.com/Julian1006/horaverde-hackathon.git
cd horaverde-hackathon
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Lo demás

En [IDEA.md](IDEA.md) está el plan repartido por lecciones y, sobre todo, la
lista de cosas que he decidido **no** hacer. Sospecho que esa lista es la que va
a decidir si llego a tiempo o no.
