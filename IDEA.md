# Lo que voy a construir

Escribo esto para no desviarme. Cada vez que se me ocurra añadir algo, vuelvo
aquí a mirar si cabe.

## La idea

HoraVerde te dice a qué hora conviene consumir electricidad para emitir menos
CO2. Sin pedirte que consumas menos.

## Por qué creo que tiene sentido

La intensidad de carbono de la red —los gramos de CO2 que cuesta producir cada
kilovatio-hora— cambia todo el rato según lo que esté generando en ese momento.
Si sopla viento, baja. Si hay que tirar de gas para cubrir el hueco, sube.

Lo comprobé antes de decidirme: a las 22:30 UTC la red estaba a 79 gCO2/kWh con
un 57 % de eólica. En horas malas esa cifra se multiplica.

Lo que acabó de convencerme es que el problema no es técnico. El dato existe, es
público y es gratis. Simplemente no le llega a la persona que está decidiendo si
pone la lavadora ahora o después de cenar.

## El razonamiento

Para reducir las emisiones de tu consumo eléctrico solo hay dos caminos.

Uno es consumir menos. Cuesta esfuerzo, la gente se resiste y además tiene un
tope: hay cosas que no puedes dejar de hacer.

El otro es consumir en otro momento. Ese no cuesta nada.

Casi todo el discurso climático va por el primer camino. El segundo está
bastante desaprovechado en lo doméstico, y hay más cosas flexibles de las que
parece: lavadora, lavavajillas, secadora, cargar el coche, cargar el portátil,
el calentador de agua, cualquier tarea pesada del ordenador. Ninguna necesita
pasar a una hora concreta.

## Qué va a hacer

Cuatro cosas, y ninguna más.

Enseñar cuánto CO2 emite la red ahora mismo, con el índice cualitativo
(bajo, moderado, alto) y de qué fuentes está saliendo esa electricidad.

Una gráfica de las próximas 48 horas, para que se vea el patrón y no solo el
número suelto.

La recomendación: la mejor franja de las próximas 24 horas, la peor, y cuánto
CO2 te ahorras eligiendo bien. Esto es lo importante del proyecto. Todo lo demás
es contexto para que se entienda.

Y un bot de Discord que conteste lo mismo cuando le preguntas.

## Qué no va a hacer

Esta lista me importa más que la de arriba. Cada cosa que tacho aquí es tiempo
que me queda para terminar lo otro.

Nada de cuentas de usuario ni base de datos. Nada de guardar tu histórico de
consumo. Nada de conectarse a enchufes o electrodomésticos inteligentes. Un solo
país. Nada de app móvil. Y nada de notificaciones automáticas programadas: el
bot contesta cuando le preguntas y ya está.

Si acabo antes de tiempo, cosa que dudo, lo primero que añadiría son las
notificaciones.

## Cómo lo reparto

Tengo tres lecciones.

**La primera, que el dato llegue.** Montar el entorno virtual y el
`requirements.txt`, y escribir un módulo aparte (`carbon_api.py`) que se encargue
de hablar con la API. Encima de eso, una app Flask mínima con una ruta que
enseñe la intensidad actual. Si al acabar la lección la web enseña un número de
verdad venido de la API, voy bien.

**La segunda, que sirva para algo.** Traer el pronóstico de 48 horas, escribir la
lógica que encuentra la mejor y la peor franja, y montar la plantilla Jinja con
la gráfica y la recomendación. Quiero que el color de la página cambie según lo
limpia que esté la red, porque así se entiende de un vistazo sin leer nada. Al
acabar, la web tiene que recomendarte una hora concreta.

**La tercera, que se pueda enseñar.** El bot de Discord, repasar el PEP8, hacer
capturas y rematar el README. Y ensayar el pitch con cronómetro, que si no me
paso seguro.

## El pitch

Cinco minutos, más o menos repartidos así.

Empiezo con el problema, que la electricidad no contamina siempre lo mismo, en
unos tres cuartos de minuto. Luego el razonamiento: mover el consumo no cuesta
nada. La demo en vivo con los datos del momento es la parte larga, unos dos
minutos, y es donde me la juego. Después, deprisa, cómo está construido. Y cierro
con el impacto y qué haría a continuación.

Si voy mal de tiempo recorto la parte técnica. La demo no se toca, que es lo
único que convence de verdad.

## Cuándo diría que ha salido bien

Si enseña datos reales y no números metidos a mano en el código. Si da una
recomendación concreta en lugar de limitarse a informar. Si junta la web con el
bot en vez de quedarse en un solo módulo del curso. Si se puede enseñar
funcionando en menos de un minuto. Y si arranca sin tener que configurar ninguna
clave de API.

## Lo que puede salir mal

Que la API se caiga justo durante el pitch. Voy a guardarme una respuesta de
ejemplo en un JSON para poder servirla si pasa.

Que no me dé tiempo al bot de Discord. Lo he puesto el último precisamente por
eso: si se cae, entrego la web sola y no pasa nada.

Que la gráfica se me complique más de la cuenta. Si veo que se me va de las
manos, la cambio por una tabla o por barras de CSS a pelo.
