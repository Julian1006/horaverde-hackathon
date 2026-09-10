# HoraVerde

La luz no contamina siempre lo mismo. Depende de si hace viento o no.

Si hace viento, la electricidad viene de los molinos y casi no contamina. Si no
hace viento, tienen que encender centrales de gas y entonces contamina mucho
más.

HoraVerde mira eso y te dice a qué hora es mejor poner la lavadora.

Lo estoy haciendo para el hackathon del curso. El tema es el cambio climático.

## Cómo se me ocurrió

Al principio pensé otras ideas, pero casi todas eran para decirle a la gente que
gaste menos luz. Eso ya lo dice todo el mundo y nadie hace mucho caso.

Luego vi que hay páginas que dicen cuántos gramos de CO2 cuesta la luz, y que va
cambiando cada media hora. Me pareció raro que nadie lo mire.

Entonces pensé: si la lavadora la puedes poner a cualquier hora, ponla cuando la
luz esté limpia. No tienes que gastar menos, solo cambiar la hora. Y a nadie le
molesta que la lavadora acabe de noche.

## Qué va a hacer

- Decirte cuánto contamina la luz ahora mismo
- Decirte de dónde viene (viento, sol, gas, nuclear...)
- Enseñar una gráfica de las próximas 48 horas
- Decirte la mejor hora y la peor para gastar luz

Cuando escribí esto estaba a 79 gCO2 por kWh y el 57 % venía del viento. Dentro
de un rato será otro número distinto.

## De dónde saco los datos

De esta página: https://api.carbonintensity.org.uk

Es gratis y no hay que registrarse ni pedir ninguna contraseña, así que puedo
usarla directamente. Eso está muy bien porque no pierdo tiempo esperando.

Lo malo es que solo sirve para Reino Unido. Para España habría que buscar otra
página, pero el código serviría casi igual.

Uso tres cosas de esa página:

- `/intensity` para lo de ahora mismo
- `/intensity/{fecha}/fw48h` para las próximas 48 horas
- `/generation` para saber de dónde viene la luz

## Con qué lo hago

Python y Flask, que es lo que hemos dado en el curso. Las páginas con HTML, CSS
y plantillas Jinja. Para pedir los datos uso requests. Y el bot de Discord con
discord.py.

Quiero juntar la parte de la web con la del bot, porque así uso dos cosas del
curso en vez de una sola.

## Por dónde voy

Ya funciona la primera parte: pido los datos y salen en una página web.

- [x] La idea
- [x] Pedir los datos
- [x] La web enseñando el dato de ahora mismo
- [ ] La gráfica y la recomendación
- [ ] El bot de Discord

## Para abrirlo

Cuando haya algo que abrir, será así:

```bash
git clone https://github.com/Julian1006/horaverde-hackathon.git
cd horaverde-hackathon
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Más cosas

En [IDEA.md](IDEA.md) he apuntado el plan y también las cosas que **no** voy a
hacer, para no liarme y no llegar tarde.
