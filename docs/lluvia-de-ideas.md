# Las ideas que barajé

Antes de decidirme estuve un rato dando vueltas. Lo apunto aquí por si más
adelante tengo que explicar por qué acabé donde acabé.

## Con qué las filtré

Me hice cuatro preguntas con cada una.

¿Reduce emisiones de verdad, o solo lo parece? Quería un vínculo claro, no algo
decorativo que suene bien en una presentación.

¿Puedo conseguir datos reales? Sin datos abiertos me queda una maqueta bonita y
vacía.

¿Cabe en tres lecciones? Es lo que tengo, no hay más.

¿Se puede enseñar funcionando en cinco minutos? Si no se ve, da igual lo bien
pensada que esté.

## Las candidatas

**Reloj de la red eléctrica.** Una web que mira cuánto CO2 emite la electricidad
en este momento y te dice a qué hora conviene consumir. La intensidad de carbono
varía bastante a lo largo del día según cuánto viento y sol haya, así que mover
el mismo consumo a otra hora ya reduce emisiones sin que nadie renuncie a nada.
Lo que falla ahora mismo es que nadie sabe cuándo hacerlo.

**Termómetro de promesas climáticas.** Recoger los compromisos que anuncian
países y empresas y contrastarlos con sus emisiones reales, para sacar un ranking
de quién cumple y quién está haciendo greenwashing. Me gustaba porque la presión
pública es lo que acaba moviendo la política climática, y lo que no se audita no
se cumple.

**Rescate de excedentes alimentarios.** Conectar comercios con producto a punto
de caducar con vecinos y ONGs cercanas. El desperdicio de comida supone entre un
8 y un 10 % de las emisiones globales: comida que se ha producido, transportado y
refrigerado para acabar en un vertedero soltando metano.

**Traductor de huella en compras.** Convertir una cesta de la compra en
emisiones equivalentes y sugerir alternativas. La idea era que el precio no
refleja el coste climático, y que si lo ves justo en el momento de decidir,
decides distinto.

**Detector de deforestación.** Analizar imágenes de satélite para detectar
pérdida de cobertura forestal. La deforestación golpea dos veces: suelta el
carbono que estaba guardado y encima elimina lo que lo absorbía.

**Generador de contenido para campañas.** Una herramienta que produzca material
compartible sobre el problema. Alcance y concienciación. Pero el vínculo con
reducir emisiones de verdad es flojo y no sabría defenderlo si me preguntan.

## Lo que sé hacer

Después de 28 lecciones tengo bots de Discord (clases y métodos, APIs, buscarme
la vida en la documentación, entornos virtuales), la eco-calculadora (HTML, CSS,
Flask, Jinja, rutas, git), el sitio de memes (Flask dinámico, selectores, pasar
datos del frontend al backend, PEP8) y scripts de análisis y de visión por
ordenador.

El curso insiste bastante en que también sé combinarlas. Eso me hizo pensar que
un proyecto que junte dos módulos vale más que uno que se quede en uno solo.

## Cómo quedaron

El rescate de comida se cayó porque necesita una base de datos y eso no lo hemos
dado.

El detector de deforestación se cayó con más pena, porque me parecía la idea más
distinta de todas, pero conseguir imágenes de satélite decentes en el tiempo que
tengo era demasiado riesgo para lo que iba a sacar.

Otras dos se cayeron por un motivo diferente. El traductor de huella es una
eco-calculadora otra vez, y el generador de contenido es el sitio de memes otra
vez. Las dos son ideas razonables, pero son entregas que ya he hecho durante el
curso, y aunque les cambie el tema al clima se nota que no me estoy arriesgando
a nada.

El termómetro de promesas me sigue gustando y creo que daría un buen proyecto,
pero recopilar los datos a mano se me comía las tres lecciones enteras.

Así que me quedo con el reloj de la red. Usa las APIs del módulo de bots, Flask
y Jinja de la eco-calculadora y el paso de datos del sitio de memes, y no repite
ninguna entrega anterior. Encima puedo rematarlo con un bot de Discord y así
junto dos módulos en un mismo proyecto.

Lo que voy a construir exactamente está en [IDEA.md](../IDEA.md).
