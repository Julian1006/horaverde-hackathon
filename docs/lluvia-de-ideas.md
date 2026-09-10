# Lluvia de ideas — Hackathon Cambio Climático

> Fase 2 del flujo de trabajo. En esta fase **no** pensamos en lo técnico:
> solo en cómo cada idea resuelve el problema.

## Criterios de selección

1. **¿Reduce emisiones o las hace visibles?** Vínculo causal claro, no decorativo.
2. **¿Hay datos reales disponibles?** Sin datos abiertos, el proyecto queda en maqueta.
3. **¿Se puede acotar a 3 lecciones?** Alcance terminable, no un producto entero.
4. **¿Se demuestra en 5 minutos?** Tiene que verse funcionando en el pitch.

## Candidatas

### A. Reloj de la red eléctrica
Panel que muestra cuánto CO2 emite la electricidad del país **ahora mismo** y
recomienda a qué horas conviene consumir (lavadora, coche eléctrico, servidores).

- *Cómo resuelve el problema:* la intensidad de carbono de la red varía muchísimo
  a lo largo del día segun cuánto viento y sol haya. Mover el mismo consumo a otra
  hora reduce emisiones **sin reducir el consumo**. Nadie cambia de hábitos si no
  sabe cuándo hacerlo.
- *Datos:* APIs públicas de intensidad de carbono / operadores de red.

### B. Termómetro de promesas climáticas
Recopila compromisos de países y empresas y los contrasta con sus emisiones reales.
Ranking de quién cumple y quién hace greenwashing.

- *Cómo resuelve el problema:* la presión pública es la palanca que mueve la
  política climática. Lo que no se audita, no se cumple.
- *Datos:* inventarios nacionales de emisiones, informes de sostenibilidad.

### C. Rescate de excedentes alimentarios
Conecta comercios con producto a punto de caducar con vecinos y ONGs cercanas.

- *Cómo resuelve el problema:* el desperdicio alimentario supone en torno al
  8-10% de las emisiones globales. Comida producida, transportada y refrigerada
  que acaba en un vertedero emitiendo metano.
- *Datos:* geolocalizacion, catálogos de comercios.

### D. Traductor de huella en compras
Convierte una cesta de la compra en emisiones equivalentes y sugiere alternativas.

- *Cómo resuelve el problema:* el precio no refleja el coste climático. Hacer
  visible ese coste en el momento de decidir cambia la decisión.
- *Datos:* bases de datos de huella de carbono por producto/categoría.

### E. Detector de deforestación
Analiza imágenes satelitales para detectar pérdida de cobertura forestal y alertar.

- *Cómo resuelve el problema:* la deforestación golpea doble (libera carbono
  almacenado y elimina el sumidero). Detectarla pronto permite intervenir.
- *Datos:* imágenes satelitales abiertas.

### F. Campaña viral / generador de contenido
Herramienta que produce contenido compartible sobre el problema climático.

- *Cómo resuelve el problema:* alcance y concienciación.
- *Riesgo:* vínculo causal débil con la reducción de emisiones. Difícil de
  defender ante el jurado.

## Decisión

Ver [IDEA.md](../IDEA.md).

---

## Filtro de viabilidad segun lo aprendido en el curso

Caja de herramientas disponible tras 28 lecciones:

- **Bots de Discord** — clases y métodos, APIs, documentación, archivos y
  carpetas, entornos virtuales.
- **Eco-calculadora** — HTML + CSS, plantillas Flask, variables Jinja,
  enrutamiento web, GitHub + IDE.
- **Sitio de memes** — Flask dinámico, selectores, paso de datos del frontend al
  backend, PEP8.
- **Scripts analizadores** y **visión por ordenador**.

El curso subraya que también sabemos **combinar** estas tecnologías. Un proyecto
que une dos módulos destaca sobre uno que solo repite uno.

| Idea | Encaje técnico | Veredicto |
|---|---|---|
| A. Reloj de la red eléctrica | API + Flask/Jinja + formulario + análisis | Usa todo y no repite nada |
| B. Termómetro de promesas | Script analizador + Flask | Viable, pero recopilar datos consume el tiempo |
| C. Rescate alimentario | Flask + base de datos | Descartada: no se han dado bases de datos |
| D. Traductor de huella | Flask + cálculo | Descartada: es otra eco-calculadora |
| E. Detector de deforestación | Visión por ordenador | Diferenciadora, pero riesgo alto con las imágenes |
| F. Generador de memes | Flask dinámico | Descartada: es otra vez el sitio de memes |

**Criterio decisivo:** D y F reproducen entregas ya realizadas en el curso. Aunque
se cambie el tema al clima, el jurado percibe que no hubo riesgo ni aprendizaje
nuevo. Se descartan por eso, no por calidad de la idea.

**Recomendación:** idea A, combinando web Flask + bot de Discord.
