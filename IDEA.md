# Lo que voy a hacer

Escribo esto para acordarme y no ponerme a hacer cosas que no tocan.

## La idea

HoraVerde te dice a qué hora conviene gastar luz para contaminar menos. No te
pide gastar menos, solo cambiar la hora.

## Por qué creo que está bien

La luz no contamina siempre igual. Cuando hace viento, la electricidad viene de
los molinos y casi no contamina. Cuando no hace, encienden centrales de gas y
contamina bastante más.

Lo probé antes de empezar: eran 79 gramos de CO2 por kWh y el 57 % venía del
viento. Cuando hay poco viento eso sube un montón.

Lo que más me gusta es que no hay que inventar nada. El dato ya existe y es
gratis. Lo que pasa es que nadie lo ve justo cuando va a poner la lavadora.

## Lo que pensé

Para contaminar menos con la luz hay dos formas.

Una es gastar menos. Pero eso cuesta, la gente no quiere, y además hay cosas que
no puedes dejar de hacer.

La otra es gastar a otra hora. Esa no cuesta nada.

Casi todo el mundo habla de la primera. Yo voy a hacer la segunda. Y hay muchas
cosas que te da igual a qué hora sean: la lavadora, el lavavajillas, la
secadora, cargar el móvil o el portátil, el calentador del agua.

## Qué va a hacer

Cuatro cosas y ya está.

Decir cuánto contamina la luz ahora mismo y de dónde viene.

Una gráfica de 48 horas para ver cómo va cambiando.

Decir la mejor hora y la peor de las próximas 24, y cuánto te ahorras. Esto es
lo más importante de todo. Lo demás es para que se entienda.

Un bot de Discord que conteste lo mismo cuando le preguntas.

## Qué NO va a hacer

Esta lista me importa más que la de arriba. Todo lo que quito aquí es tiempo que
me sobra para hacer bien lo otro.

Nada de usuarios ni contraseñas. Nada de guardar tus datos. Nada de conectarlo a
enchufes inteligentes. Solo un país. Nada de app de móvil. Y el bot solo
contesta cuando le preguntas, no avisa él solo.

Si me sobra tiempo, que lo dudo, lo primero sería que avisara solo.

## Cómo lo reparto

Tengo tres clases.

**La primera: que lleguen los datos.** Montar el entorno virtual y el
`requirements.txt`, y hacer un archivo aparte (`carbon_api.py`) que se encargue
de pedir los datos. Y una web de Flask con una página que enseñe el número. Si
al acabar la clase sale un número de verdad, voy bien.

**La segunda: que sirva para algo.** Traer las 48 horas, hacer la parte que
busca la mejor y la peor hora, y montar la página con la gráfica. Quiero que el
color de la página cambie según lo limpia que esté la luz, porque así se ve
rápido sin leer nada. Al acabar tiene que decirte una hora.

**La tercera: que se pueda enseñar.** El bot de Discord, ordenar el código,
hacer capturas y terminar el README, para que se entienda sin que yo tenga
que explicar nada.

## Cuándo estará bien

Si los datos son de verdad y no números que he puesto yo a mano. Si te dice una
hora en vez de solo contarte cosas. Si junto la web con el bot. Si se puede
enseñar en menos de un minuto. Y si funciona sin tener que poner contraseñas
raras.

## Lo que puede salir mal

Que la página de los datos se caiga justo cuando lo esté enseñando. Voy a
guardarme un ejemplo en un archivo para poder enseñarlo igual.

Que no me dé tiempo del bot. Por eso lo he puesto el último. Si no llego, enseño
solo la web y ya.

Que la gráfica sea muy difícil. Si veo que no me sale, hago una tabla o barras
con CSS y listo.
