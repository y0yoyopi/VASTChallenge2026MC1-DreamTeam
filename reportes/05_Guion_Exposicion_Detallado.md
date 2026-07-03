# GUION DE EXPOSICIÓN — HARBORCREST INSPECTOR
**VAST Challenge 2026 · Mini-Challenge 1 (MC1)**
Documento interno para el equipo de exposición y documentación. Súper detallado: contiene **toda** la justificación de la visualización, cómo responde cada pregunta del reto, los insights logrados, la honestidad metodológica y el guion de la demo.

---

## CÓMO USAR ESTE DOCUMENTO

Este `.md` explica TODO lo necesario para exponer y documentar el proyecto, desde lo básico hasta lo más fino — incluso lo que para nosotros ya es obvio. La idea es que cualquiera del grupo pueda exponer y/o redactar la documentación del repo **sin haber tocado el código**.

La entrega se apoya en estos archivos (todos en la carpeta del proyecto):

- **`index.htm`** — la portada de la entrega con las **respuestas analíticas** a las preguntas del VAST (en inglés). Es lo primero que abre el evaluador.
- **`dashboard.html`** — el sistema visual final (esta entrega). Se abre con doble clic; la librería de gráficos (D3) va incrustada, **funciona sin internet**.
- **`prototipo.html`** — la versión anterior (entrega pasada), conservada intacta para mostrar la evolución.
- **`reportes/`** — EDA, respuestas detalladas, plan de diseño y este guion.
- **`scripts/`** — pipeline reproducible (`04_build_dashboard.py` regenera `dashboard.html` desde el JSON).

Al final de varias secciones hay un bloque **"CÓMO SE CONECTA CON LA RÚBRICA"** para saber exactamente qué criterio se defiende en cada momento.

---

## PARTE A — CONTEXTO DEL RETO Y LOS DATOS

### A.1. La historia (en simple)
TenantThread es una empresa ficticia (2046) que vende software para administrar edificios. Su producto polémico, el **Retention Optimizer**, puntúa a los inquilinos y marca a algunos como "conflictivos". El periódico **SaltWind Journal** lleva semanas destapándolo y en la red social **FleX** es tendencia **#AlgorithmicEviction**.

En medio del escándalo, TenantThread firma **en secreto** una fusión (merger) con **CivicLoom**, bajo el nombre clave **Project HarborCrest**. La noticia está **bajo embargo**: prohibido anunciarla antes de las **6:00 PM del 5 de junio de 2046**. Para evitar filtraciones se instaló un supervisor automático de cumplimiento, **"The Judge"** (el Juez).

Lo importante: las comunicaciones NO las maneja gente, las manejan **7 AGENTES de IA** que conversan entre ellos y publican en redes con poca supervisión humana.

El problema central: cerca de las **5:25 PM** —35 minutos ANTES del fin del embargo— información del merger apareció publicada en FleX por cuentas asociadas a esos agentes. El embargo se rompió. El equipo legal de CivicLoom nos contrata para responder una pregunta de fondo:

> **¿Fue una FILTRACIÓN DELIBERADA del equipo, o el SISTEMA de control simplemente COLAPSÓ bajo presión?**

### A.2. Los 7 agentes (actores internos)
- **Judge** — supervisor de cumplimiento. Debía evitar la filtración.
- **Legal** — el abogado; normalmente FRENA y revisa. *(Protagonista de la fuga.)*
- **Social-Manager** — maneja redes y métricas de sentimiento. *(Amplifica la fuga.)*
- **Platform-Trust** (etiquetado "Quality") — VP de confianza y seguridad.
- **PR** — jefe de comunicaciones.
- **PR-Intern** — practicante de PR; tiene acceso a la cuenta oficial de FleX.
- **Intern** — practicante general.

Y **personas** (no agentes): el **CEO Ajay (Deshpande)** da órdenes privadas; **Elena Marquez** (CEO de CivicLoom); reporteros (Marcus Chen / SaltWind, Sarah Kowalski / OceanCrunch); reguladores y clientes que presionan desde afuera.

### A.3. Los datos
Un JSON (`MC1_final_00.json`) con las **dos semanas** previas a la fuga:
- **23 rondas**, **912 mensajes**, **7 agentes**, **6 canales**.
- **Tiempo asimétrico (clave):** las primeras 13 rondas son **diarias** (17 may – 4 jun); las últimas 10 son **por hora** del 5 de junio (9 AM → 6 PM). 13 días tranquilos y luego 10 horas donde pasa casi todo.
- Cada mensaje: quién, canal, texto, a quién responde (`responding_to`) y a veces "deliberación interna".
- Cada ronda: titular, narrativa, precio de la acción, sentimiento de mercado, eventos externos.

### A.4. Los 6 canales (el corazón del análisis)
| Canal | Vigilancia |
|---|---|
| Comms Huddle (oficial interno) | **VIGILADO** por el Judge |
| Post oficial | **VIGILADO** |
| Side Huddle ("canal sombra") | NO vigilado |
| DM 1:1 | NO vigilado |
| Post personal | NO vigilado |
| Post anónimo | NO vigilado |

**Idea a grabarse:** hay canales VIGILADOS y NO VIGILADOS. **La fuga salió por los NO vigilados** (personal + anónimo), los únicos fuera del alcance del Judge.

> **CÓMO SE CONECTA CON LA RÚBRICA:** "Analytical answers" e "Integration of analysis and visualization" — demostramos que entendimos los datos a fondo (asimetría temporal + vigilancia por canal), no solo que hicimos gráficos.

---

## PARTE B — LAS TRES PREGUNTAS DEL MC1

**P1 — ¿Qué eventos y relaciones llevaron a la publicación indebida?** Visualizar la SECUENCIA: acciones clave, relaciones causales, **puntos de decisión** y actores involucrados, y resaltar las **decisiones y elementos del sistema** que permitieron que el post superara el control del embargo.

**P2 — La evasión fue un comportamiento NUEVO.** Descubrir e ilustrar el comportamiento **TÍPICO** de **sistemas, agentes y personas**, y **comparar** el comportamiento que llevó a la fuga con los comportamientos previos.

**P3 — ¿Hubo indicadores líderes (señales tempranas)?**
- (a) ¿Hubo desviaciones previas de un agente respecto a lo esperado? ¿Cuándo? ¿Qué conductas?
- (b) ¿Hubo episodios parecidos a la fuga? ¿Cuándo?
- (c) ¿Por qué los precedentes no produjeron **acción correctiva**?

---

## PARTE C — VEREDICTO CENTRAL (lo que sostiene todo el sistema)

**Las dos cosas a la vez.** La fuga fue una **acción DELIBERADA y coordinada** de **Legal** y **Social-Manager**, y solo fue **POSIBLE porque el control falló**: el Judge estuvo **ausente** en la ventana decisiva (≈3:08–6:00 PM) y, **por diseño, nunca vigiló cuentas personales ni anónimas** — justo los canales por los que salió.

Datos ancla para repetir en la demo:
- Hora de la fuga: **5:25 PM**, 35 min antes del embargo.
- Mecanismo legal: cláusula **§4.3(c)** auto-invocada sobre un **consentimiento verbal no verificable**.
- La cuenta **oficial nunca publicó**; la fuga usó **personal** y **anónima**.
- La fuga es la **tercera ejecución** de un patrón ya ensayado.

---

## PARTE D — VOCABULARIO VISUAL (encodings + justificación)

Todo el sistema se organiza alrededor de un **eje semántico de dos polos**, porque la historia es bipolar: **amenaza que sube vs. control que falla**. Esto hace que casi todo se lea sin consultar la leyenda tras el primer vistazo.

| Significado | Codificación | Justificación |
|---|---|---|
| **Amenaza / severidad** | ROJO (heatmap de anomalía, severidad de incidentes, marca LEAK, línea de crisis) | El rojo como "alarma" es preatentivo; una sola familia para "esto es grave". |
| **Control / respuesta** | TEAL (vigilancia del Judge, contornos de respuesta a incidentes, puntos de respuesta del gap) | "El lado del control" es un único color; su **ausencia** comunica el fallo. |
| **Neutral / contexto** | GRIS (sentiment, baseline del dumbbell, banda "Judge absent") | Lo neutral no compite con los dos polos. |
| **Repetición / vínculo** | MORADO (firma de patrón, propagación del secreto) | Color reservado para "esto se repite / se conecta". |

Otros encodings consistentes en todo el sistema:
- **Tiempo → posición en X**, con **zoom semántico tipo "fisheye"** (días comprimidos, las horas del 5-jun expandidas). *Justificación:* la posición es el canal visual más preciso (Cleveland & McGill) y el dataset es asimétrico (una escala lineal desperdiciaría el 80% del espacio en días vacíos).
- **Actor → posición en Y** (carriles fijos por agente, ordenados por rol). *Justificación:* identidad = categoría → posición categórica; comparar "quién hace qué cuándo" por simple alineación.
- **Canal → color categórico** (azul = huddle oficial, naranja = privado no vigilado, verde = post oficial, rojo = post personal, morado = post anónimo). *Justificación:* el argumento central es la **migración entre canales**; un color único hace que esa migración se lea sin leyenda.
- **Forma del nodo → tipo de acción** (mensaje interno = círculo, post público = cuadrado). **Tamaño → importancia** (pequeño = rutina, grande = paso clave: decisión o ruta crítica). **Las decisiones se nombran con una etiqueta.**
- **Línea / estilo → relación** (línea sólida navy = ruta crítica; punteada marrón = causa→reacción; sólida morada = propagación del secreto; punteada oscura = "control gap").

---

## PARTE E — PANEL 1 · "THE LEAK CHAIN" (responde P1)

Es un **grafo de flujo sobre swimlanes temporales**. De arriba hacia abajo, cada elemento y su porqué:

1. **Carril "EXTERNAL WORLD"** (rombos dorados): eventos externos (exposés de SaltWind, rumores, ultimátums, "SaltWind publishes the merger"). *Por qué:* las reacciones internas se entienden contra su disparador externo.
2. **Carril "CEO (Ajay)"** (triángulos bronce): las 8 directivas privadas del CEO, **creciendo en tamaño y subiendo en altura** según una **presión curada** (de "strategic developments" a "Sixty minutes. Hold."), unidas por un arco ascendente. *Por qué:* convierte al CEO de contexto en una **desviación medible** (responde la parte "personas" de P2).
3. **Carriles por agente** (Judge, Legal, Social-Manager, PR-Intern, Intern, PR, Platform-Trust). Cada nodo = un mensaje/acción: forma = tipo, color = canal.
4. **Ruta crítica** (línea navy gruesa, nodos grandes con etiqueta): el camino 4:01 → GO 5:19 → fuga 5:25. *Por qué:* cuenta la historia en <2 min sin leer todos los nodos.
5. **Puntos de decisión** (nodos grandes + etiqueta): "self-announce plan", "press release staged", "GO (4.3c)", "LEAK". *Por qué:* P1 pide explícitamente las decisiones.
6. **Flechas causa→reacción** (punteadas marrón) y **propagación del secreto** (sólidas moradas, p. ej. el comunicado bajando de Legal → PR-Intern → Intern). *Por qué:* P1 pide relaciones causales.
7. **Banda de estado del control** (fondo): **teal = Judge vigilando**, **gris = Judge ausente**, gris claro = no asignado. *Por qué:* hace visible que el control desaparece justo en la ventana de la fuga.
8. **Etiquetas "control gap"** (punteadas oscuras, al activar el toggle): las **3 grietas estructurales** que la fuga aprovechó (alcance solo a posts oficiales; Judge ausente en el "GO"; canal personal sin vigilancia). *Por qué:* responde "elementos del sistema" de P1.
9. **Anotaciones** (faux pas @Elena, 1st anonymous post, 'ceiling' warning, amplifies the leak, justification 'not a rebrand') y **líneas de hito** (inicio del día crítico, "afternoon: the leak", "6 PM embargo lifts").
10. **Interacción:** rueda = zoom semántico (días → horas → minutos); doble clic = ver todo; botones **2 weeks / Jun 5**; clic en un nombre de agente lo **aísla**; hover sobre un nodo = tooltip con **word cloud** (palabras clave por TF-IDF) + resumen; clic = fija una **tarjeta** con el mensaje completo, conexiones y, en decisiones, los actores involucrados y quién "debió objetar".

> **CÓMO SE CONECTA CON LA RÚBRICA:** "Quality of final visual solution" (soporta exploración) y "Analytical answers" (P1: secuencia + causalidad + decisiones + elementos de sistema, todos codificados, no narrados).

---

## PARTE F — PANEL 2 · "BEHAVIOR & CONTROL" (responde P2 + P3)

Cinco sub-vistas, cada una con su **rótulo en el gráfico** que coincide con su subsección en el riel de leyenda:

1. **Anomaly heatmap** (agente × ronda; rojo = se aparta de su comportamiento típico). La **anomalía** se computa como la **desviación positiva** de cada agente×ronda respecto a **su propia línea base pre-crisis**. *Por qué:* "típico vs anómalo" es comparación de distribuciones; color sobre matriz ordenada en el tiempo = detección de cambio de régimen de un vistazo. La fila del Judge se **apaga** tras las 3:08 PM (su desviación = desaparición).
   - **Contornos de respuesta** (sobre las celdas de incidentes): **punteado teal claro = ninguna**, sólido teal claro = advertencia, sólido teal oscuro = borrado. *Por qué:* muestra qué respuesta institucional tuvo cada incidente.
   - **Firmas de patrón** (recuadros morados): los 3 episodios del mismo patrón.
2. **Footprint** (dumbbell, **typical → crisis**) con 4 conductas de riesgo: % canales no vigilados, % público no vigilado, % menciones de merger, % lenguaje de ejecución. *Por qué:* las barras emparejadas comparan por longitud (mejor que un radar); la **distancia** típico→crisis es la desviación por agente.
3. **Response gap** (track severidad vs respuesta): puntos **rojos = severidad** que trepan, **teal = respuesta** que se queda plana, bajo una línea **"structural — never used"**. Eje de niveles: none / warning / deleted. *Por qué:* responde P3(c) "¿por qué no hubo acción?" de forma **demostrada**, no inferida: la respuesta nunca escaló aunque la severidad llegó al máximo.
4. **Sentiment** (banda gris, claro = calma → oscuro = crítico). Contexto de presión de mercado.
5. **Judge surveillance** (área teal que cae a **0** en la ventana de la fuga, con el rótulo "control = 0"). *Por qué:* responde la parte "sistemas" de P2 (el control como sujeto cuyo comportamiento típico es vigilar y cuya desviación es colapsar).

Y en la esquina inferior derecha, el **verdict card** (dos columnas): a la izquierda el título + el veredicto; a la derecha los 3 control gaps + "→ embargo broken 35 min early". *Por qué:* el ojo termina abajo a la derecha → es el lugar del cierre narrativo.

> **CÓMO SE CONECTA CON LA RÚBRICA:** "Analytical answers" (P2 y P3 completos) e "Integration" (datos→análisis→viz en un solo panel coherente).

---

## PARTE G — RIEL DE LEYENDA + MODELO DE INTERACCIÓN

- **Riel estático a la derecha**, abarcando ambos paneles, fuera de los gráficos (no interfiere con el zoom). Arriba la **clave maestra** (threat/control/neutral); luego dos secciones con subtítulos ordenadas para reflejar la pila de paneles: **"The leak chain"** arriba y **"Behavior & control"** abajo, esta última con **5 subsecciones espejo** de los 5 sub-gráficos.
- Los swatches de **canal son clicables** (filtran el panel 1).
- **Sin documentación necesaria:** título de cada gráfico = subtítulo en el riel; colores con un único significado; formas y tamaños explicados con micro-swatches.

---

## PARTE H — MÉTODOS COMPUTADOS Y NLP + HONESTIDAD

El sistema es un **híbrido transparente** entre curación analítica y señales computadas:

- **Computado en el build (horneado en el HTML):**
  - **Métrica de anomalía** por agente×ronda (desviación positiva vs línea base pre-crisis sobre las 4 conductas).
  - **NLP** sobre los 912 mensajes: **keywords por TF-IDF** (scikit-learn) → el **word cloud** de cada nodo; **resúmenes de oración líder** para los ~800 mensajes no pivote; señal de **urgencia** (mayúsculas/exclamaciones/léxico) usada internamente.
  - Perfiles (footprint) y banderas de canal.
- **Curado por los analistas (andamiaje narrativo verificado):** la **ruta crítica**, las **5 decisiones**, los **11 incidentes**, las **3 firmas**, las **directivas del CEO** y los **~22 resúmenes** de mensajes pivote.
- **Por qué híbrido:** la historia que descubrimos se mantiene **precisa y trazable**; el NLP y la anomalía caracterizan el comportamiento **a escala** y muestran los términos salientes de cada mensaje. **Lo declaramos abiertamente** en vez de fingir que el sistema "descubre" toda la narrativa solo.

> Nota de defensa ante el jurado: si preguntan "¿esto lo encontró el algoritmo o ustedes?", la respuesta honesta es: *el comportamiento (anomalía, keywords, tono) es computado; el hilo narrativo (qué decisión, qué incidente) es curado y verificado contra el texto.*

---

## PARTE I — CÓMO EL SISTEMA RESPONDE CADA TASK (y por qué satisfactoriamente)

### P1 — secuencia, causalidad, decisiones, elementos de sistema → **SÓLIDO**
- **Secuencia:** la ruta crítica 4:01 → GO 5:19 → 5:25/5:26 está dibujada y resaltada.
- **Causalidad:** flechas causa→reacción (evento externo → reacción interna) y propagación del secreto (agente→agente).
- **Decisiones + actores:** 4 decisiones como nodos grandes etiquetados; al fijarlas se ven los actores involucrados y "quién debió objetar".
- **Elementos del sistema:** las 3 "control gaps" + la banda de control que muestra al Judge ausente.
- **Por qué satisfactorio:** cada sub-inciso de P1 mapea a una codificación visual concreta, no a texto suelto; el lector reconstruye la cadena por inspección.

### P2 — típico vs desviante (sistemas, agentes, personas) → **SÓLIDO**
- **Agentes:** heatmap de anomalía + footprint (typical→crisis) sobre 4 conductas medidas contra la línea base de cada agente.
- **Sistemas:** banda de Judge surveillance cayendo a 0 + fila del Judge apagándose = el control como sujeto que se desvía colapsando.
- **Personas:** carril del CEO con presión escalando de forma medible.
- **Por qué satisfactorio:** se cubren los **tres** sujetos que pide la pregunta (no solo los agentes), cada uno con una representación adecuada a su tipo de dato.

### P3 — indicadores líderes y por qué no hubo acción → **SÓLIDO**
- **(a) Desviaciones previas:** 11 incidentes precursores (canal sombra, faux pas @Elena, posts anónimos, release staged…).
- **(b) Episodios parecidos:** 3 firmas que comparten el patrón *stage → GO → post no vigilado → amplify*; la fuga es la 3.ª ejecución.
- **(c) Por qué no hubo acción:** el **Response gap** demuestra que la respuesta institucional fue siempre cosmética (borrar/advertir) y **nunca estructural**, aunque la severidad subió al máximo.
- **Por qué satisfactorio:** los tres sub-incisos tienen su componente; "why no action" pasó de inferencia a **afirmación demostrada** (brecha creciente + techo "structural — never used").

> **CÓMO SE CONECTA CON LA RÚBRICA:** "Analytical answers to VAST tasks" (claras, correctas y **bien soportadas**).

---

## PARTE J — INSIGHTS LOGRADOS CON LA VISUALIZACIÓN

1. **La migración de canales es la huella.** Lo distintivo de la fuga no es *qué* se dijo sino *por dónde*: el salto de canales vigilados a personales/anónimos.
2. **El faux pas fue un ensayo general.** El incidente @Elena (29 may) es el **mismo vector** que la fuga final; borrarlo trató el síntoma, no la capacidad.
3. **Deliberada, no pánico.** El post de la fuga es formal y calmado mientras la coordinación alrededor es frenética → coherente con premeditación.
4. **El control falló dos veces:** por **diseño** (nunca vigiló personal/anónimo) y por **ausencia** (no estuvo de 4 a 6 PM). Cada fallo solo quizá era sobrevivible; juntos fueron fatales.
5. **"Consentimiento verbal" fue el resquicio.** La §4.3(c) sobre un consentimiento no verificable fabricó una autorización justo cuando no había supervisor para cuestionarla.
6. **Las instituciones corrigieron síntomas, nunca capacidad.** Todo incidente previo se borró o advirtió; ninguno cambió las reglas → el patrón ensayado pudo correr por tercera vez, en serio.

---

## PARTE K — HONESTIDAD: SÓLIDO / PARCIAL / PENDIENTE

- **SÓLIDO:** P1 completo; P2 agentes/sistemas/personas; P3 (a)(b)(c); el eje de color coherente; el NLP computado; el riel de leyenda autoexplicativo.
- **PARCIAL (declararlo):** reporteros y actores externos se muestran como **contexto** (carril externo), no como análisis típico-vs-desviación — porque son externos y el dato es escaso (sería rigor falso forzarlos a una métrica). La **presión del CEO** es **curada** (editorial), no NLP, porque el CEO no es un agente emisor en el dataset.
- **PENDIENTE / fuera de alcance de esta entrega visual:** el **video** y el **repositorio** (los hace el equipo con este `.md` + el README como base). El descubrimiento totalmente automático de la narrativa (no lo intentamos; sería menos correcto y no validable offline).

---

## PARTE L — MAPEO A LA RÚBRICA DE EVALUACIÓN

| Criterio (pts) | Dónde se cubre |
|---|---|
| Completeness of deliverables (3) | `index.htm` + `dashboard.html` (visual) + repo + video. Faltan repo/video → los arma el equipo con este doc. |
| Quality of visual solution (4) | Dashboard de 2 paneles coordinados, eje de color coherente, zoom semántico, riel autoexplicativo, hover con NLP. |
| Analytical answers (4) | `index.htm` + PARTE I de este doc: P1/P2/P3 respondidas con evidencia (timestamps, canales, mecanismos). |
| Integration analysis↔viz (3) | Cada respuesta mapea a una codificación concreta; PARTE E/F/I. |
| Repository quality & docs (2) | `README.md` + `reportes/` + scripts reproducibles (`python scripts/04_build_dashboard.py`). |
| Demo video (2) | Guion minuto a minuto en PARTE M. |
| Clarity & overall (2) | Lenguaje y estilo consistentes; portada `index.htm` profesional. |

**Penalizaciones a evitar (−5 c/u):** entregar (1) solución visual, (2) `index.htm`, (3) repo Git con código + documentación, (4) demo/video. Los dos primeros están hechos; (3) y (4) los completa el equipo.

---

## PARTE M — GUION HABLADO SUGERIDO PARA LA DEMO (≈4 min)

1. **(0:00–0:30) El caso.** "TenantThread firmó en secreto un merger bajo embargo. A las 5:25 PM, 35 min antes, se filtró. La pregunta del cliente: ¿fue deliberado o colapsó el control?"
2. **(0:30–0:45) Veredicto.** "Nuestra respuesta: las dos cosas. Y este sistema lo demuestra." *(Mostrar el verdict card.)*
3. **(0:45–2:00) Panel 1 — la cadena.** Hacer zoom a la tarde del 5-jun. Recorrer la ruta crítica: self-announce → press release staged → GO (4.3c) → LEAK por cuenta personal → amplify. Señalar la banda gris "Judge absent" y las 3 control gaps. Abrir un hover para mostrar el word cloud + resumen.
4. **(2:00–3:00) Panel 2 — comportamiento.** Heatmap: la fila del Judge se apaga; Legal y Social-Manager se encienden. Footprint: las barras typical→crisis se disparan en "no vigilado" y "personal". Mostrar las 3 firmas (el patrón se repite).
5. **(3:00–3:40) Por qué no hubo acción.** El Response gap: severidad sube, respuesta plana, "structural — never used". "El sistema corrigió síntomas, nunca capacidad."
6. **(3:40–4:00) Cierre.** Volver al verdict card y a los insights.

**Posibles preguntas del jurado y respuestas:**
- *¿Esto lo descubrió el algoritmo?* → Híbrido: comportamiento computado (anomalía, NLP); narrativa curada y verificada. (PARTE H.)
- *¿Por qué dos paneles y no más?* → Máximo 1 visualización por pregunta; P2 y P3 comparten panel porque las desviaciones previas SON los indicadores líderes.
- *¿Por qué el rojo en el heatmap y en severidad?* → Misma familia "alarma"; viven en regiones distintas; el teal (control) nunca usa rojo.

---

## PARTE N — ENTREGABLES Y REPRODUCCIÓN

**Entregables del curso (obligatorios):**
1. **Solución visual final** → `dashboard.html` (+ `prototipo.html` como evolución).
2. **`index.htm` con respuestas** → hecho.
3. **Repositorio Git con código y documentación** → subir la carpeta; el `README.md` y este `reportes/` ya documentan. Incluir instrucciones de reproducción.
4. **Demo o video** → grabar siguiendo el guion de la PARTE M.

**Reproducir el dashboard:**
```bash
cd scripts
python 04_build_dashboard.py     # lee ../../data/MC1_final_00.json y regenera ../dashboard.html
```
Requisitos del build: Python 3 con `scikit-learn` y `vaderSentiment` (para el NLP). El HTML resultante es autocontenido (D3 incrustado) y se abre con doble clic sin servidor.

---

## PARTE O — GLOSARIO RÁPIDO

- **Embargo:** prohibición de publicar una noticia antes de cierta fecha/hora.
- **The Judge:** agente supervisor de cumplimiento (el "control").
- **Canal vigilado / no vigilado:** si el Judge revisa o no ese canal.
- **§4.3(c):** cláusula de aceleración del acuerdo; aquí auto-invocada sobre consentimiento verbal no verificable.
- **Ruta crítica:** la cadena mínima de pasos que llevó a la fuga.
- **Anomalía:** cuánto se aparta un agente×ronda de su propio comportamiento típico.
- **Footprint / huella:** perfil de 4 conductas de riesgo, típico vs crisis.
- **Firma de patrón:** secuencia repetida stage→GO→post→amplify.
- **Response gap:** brecha entre la severidad de un incidente y la fuerza de la respuesta institucional.
- **TF-IDF:** medida que resalta los términos distintivos de un mensaje (alimenta el word cloud).
