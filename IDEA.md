# La idea

> Documento de la fase 3: consolidar la idea. Sirve para mantener la
> concentración y no desviarse durante la implementación.

## En una frase

**HoraVerde te dice a qué hora conviene consumir electricidad para emitir menos
CO2, sin pedirte que consumas menos.**

## El problema concreto

La intensidad de carbono de la red eléctrica —los gramos de CO2 que cuesta
producir cada kilovatio-hora— **varía continuamente a lo largo del día** según la
mezcla de fuentes que esté generando en ese momento.

Un dato real medido durante la definición de este proyecto: a las 22:30 UTC la
red estaba a 79 gCO2/kWh con un 57,4 % de eólica, un índice "bajo". En horas de
poco viento esa cifra sube varias veces.

El problema no es técnico, es de **información**. El dato existe y es público,
pero no llega a quien toma la decisión de encender la lavadora.

## El insight

Hay dos formas de reducir las emisiones del consumo eléctrico:

1. **Consumir menos** — exige sacrificio, la gente se resiste, tiene un tope.
2. **Consumir en otro momento** — no exige ningún sacrificio.

Casi todo el discurso climático se centra en la primera. HoraVerde ataca la
segunda, que está prácticamente sin explotar a nivel doméstico.

**Consumos flexibles:** lavadora, lavavajillas, secadora, carga del coche
eléctrico, carga de portátiles y baterías, tareas pesadas de ordenador,
calentadores de agua. Nada de esto necesita ocurrir a una hora concreta.

## Qué hace (alcance del MVP)

1. **Panel "ahora mismo"** — intensidad actual en gCO2/kWh, el índice
   cualitativo (bajo/moderado/alto) y la mezcla de generación del momento.
2. **Gráfica de 48 horas** — el pronóstico, para que se vea el patrón.
3. **La recomendación** — la mejor franja de las próximas 24 h, la peor, y el
   ahorro en CO2 de elegir bien. Este es el corazón del proyecto.
4. **Bot de Discord** — comando que devuelve el estado actual y la recomendación.

## Qué NO hace (fuera de alcance)

Delimitar esto es lo que permite terminar a tiempo.

- ❌ Cuentas de usuario, login, base de datos
- ❌ Histórico de consumo personal
- ❌ Integración con electrodomésticos o enchufes inteligentes
- ❌ Cobertura de múltiples países
- ❌ App móvil
- ❌ Notificaciones automáticas programadas (solo respuesta a comando)

Si sobra tiempo, lo primero que se añade son las notificaciones automáticas.

## Plan por lecciones

### Lección 1 — Que funcione el dato
- Entorno virtual y `requirements.txt`
- Cliente de la API en un módulo aparte (`carbon_api.py`)
- App Flask mínima con una ruta que muestre la intensidad actual
- **Al final de la lección:** la web enseña un número real de la API

### Lección 2 — Que sirva para algo
- Consumir el pronóstico de 48 h
- Lógica que calcula la mejor y la peor franja y el ahorro
- Plantilla Jinja con la gráfica y la recomendación
- CSS: que el color de la página cambie según lo limpia que esté la red
- **Al final de la lección:** la web recomienda una hora concreta

### Lección 3 — Que se pueda enseñar
- Bot de Discord con comando de consulta
- Repaso PEP8, README final, capturas
- Ensayar el pitch cronometrado
- **Al final de la lección:** proyecto presentable

## Guion del pitch (5 minutos)

| Tiempo | Contenido |
|---|---|
| 0:00–0:45 | El problema: la electricidad no siempre contamina lo mismo |
| 0:45–1:30 | El insight: mover el consumo no cuesta nada |
| 1:30–3:30 | **Demo en vivo** con datos reales del momento |
| 3:30–4:15 | Cómo está construido: API + Flask + bot |
| 4:15–5:00 | Impacto y siguiente paso |

**Regla:** la demo es lo que convence. Si hay que recortar, se recorta de la
parte técnica, nunca de la demo.

## Criterios de éxito

- [ ] Muestra datos reales, no inventados ni fijos en el código
- [ ] Da una recomendación concreta, no solo información
- [ ] Combina dos módulos del curso (web + bot)
- [ ] Se demuestra en vivo en menos de un minuto
- [ ] Funciona sin configurar claves de API

## Riesgos y planes B

| Riesgo | Plan B |
|---|---|
| La API se cae durante el pitch | Guardar una respuesta de ejemplo en JSON y poder servirla |
| No da tiempo al bot de Discord | Es lo último del plan por eso: se entrega solo la web |
| La gráfica se complica | Sustituir por una tabla o barras de CSS puro |
