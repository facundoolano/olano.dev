---
layout: post
title: "Inocencia interrumpida"
excerpt: La mentira que nos contamos a nosotros mismos.
date: 2023-10-12
tags: [software]
thumbnail-img: assets/img/pappo.jpg
image: assets/img/pappo.jpg
---

Hace unos días leí este mensaje de Graydon Hoare, el iniciador de Rust<sup><a id="fnr.1" class="footref" href="#fn.1" role="doc-backlink">1</a></sup>:

> I hear this sentiment ("code is meant to be read more than run") a lot among programming communities and I've even repeated it myself but lately I wince seeing/hearing it repeated. I increasingly think it serves to obscure the economic realities of our occupation. Like it's a story we like to tell ourselves to try to elevate us from proletarians to poets or something (&#x2026;) And I think it's actually not very true. Code <span class="underline">can</span> be written for reading, among people interested in that practice, but it's mostly written for running, and even more-mostly written by someone being paid by someone else very interested in minimizing the cost of going from "nothing running" to "great, something is running" (&#x2026;) Virtually none of the people paying for software ever want to <span class="underline">read</span> it.

El texto me provocó una serie de reacciones, que ahora quiero desmenuzar.

En primer lugar me puso en guardia, porque la opinión de que "el código es para las personas antes que para las máquinas" es una que yo sostengo, a veces [exageradamente](../2021-02-01-suenan-los-programadores-con-poemas-electricos). En segundo lugar me hizo cuestionarme si esa opinión efectivamente conlleva cierta arrogancia, cierta pretensión de superioridad, como insinúa Hoare. Tiendo a creer que no: al menos en mi cabeza esa idea siempre coexistió con la de que [somos plomeros digitales](../2023-05-19-los-sinsabores-del-software-imaginario/) más que arquitectos o ingenieros; que nuestro trabajo es menos especial y menos valioso de lo que muchos suponen.

Ocurre que la informática es una disciplina relativamente joven, que en algunos aspectos tiene un grado de desarrollo pre-industrial: los programadores se parecen más a los artesanos de los talleres que a los trabajadores de las fábricas. El desarrollo tecnológico no alcanza ([por ahora](../2023-07-10-la-era-de-la-boludez)) para prescindir del componente intelectual humano; no es una tarea alienante y repetitiva a lo *Tiempos Modernos* sino que requiere intervención activa e incluso creativa del trabajador<sup><a id="fnr.2" class="footref" href="#fn.2" role="doc-backlink">2</a></sup>. Y entiendo que este tipo de involucramiento en la actividad conlleva, al menos en algunas personas, un aprecio por el trabajo, una vocación de *hacerlo bien* separada de su retribución económica<sup><a id="fnr.3" class="footref" href="#fn.3" role="doc-backlink">3</a></sup>. El programador que promueve el código legible (o que escribe tests o hace algún otro esfuerzo de "mantenibilidad") no está maquillando su tarea para que parezca más interesante: está intentando honestamente hacer bien su trabajo.

La cuestión es que la definición de *trabajo bien hecho* la da el propio artesano: es subjetiva y [puede no estar alineada](../2022-11-28-posdata-sobre-la-complejidad-esencial/) con los intereses de quien lo paga. En esto creo que tiene razón Hoare: es fácil para nosotros enamorarnos del oficio, tratar de hacerlo bien según nuestro criterio, ignorando el marco económico en el que existe. Pero me parece que tampoco sirve la actitud opuesta: limitarse a cumplir una tarea sin compromiso, al menor costo posible. Creo que es obligación del desarrollador de software aceptar la tensión de intereses y [buscar un equilibrio razonable](../2023-02-22-worse-is-better-is-worse-is-better/).

De acuerdo con como yo aprendí el oficio &#x2014;según ideas que cristalizaron alrededor del año 2000&#x2014;, ese equilibrio se puede encontrar poniendo en primer plano a los usuarios del software que desarrollamos: teniendo siempre presente que el código no es un fin en sí mismo sino un medio para resolver problemas o proveer servicios. Por eso el movimiento Agile, antes de devenir culto religioso, ponía como máxima prioridad satisfacer al cliente<sup><a id="fnr.4" class="footref" href="#fn.4" role="doc-backlink">4</a></sup>; por eso Extreme Programming proponía sentar al cliente al lado del equipo; por eso *The Pragmatic Programmer* nos pedía que deleitemos a nuestros usuarios en vez de limitarnos a entregar código<sup><a id="fnr.5" class="footref" href="#fn.5" role="doc-backlink">5</a></sup>. El razonamiento era que, poniendo al software en términos de la utilidad que provee a los usuarios, el programador podía reconciliar su definición de *trabajo bien hecho* con la del mercado, disponía de una vara con la que medir costos y beneficios y orientar sus decisiones.

Aunque no me guste el ejemplo particular que usa Hoare, comparto su intención de cuestionar el sentido común del oficio y exponer las dinámicas socioeconómicas a las que responde. Fue la expresión "it's a story we like to tell ourselves" &#x2014;que traduzco: *es una mentira que nos contamos a nosotros mismos*&#x2014; la que me hizo entrar en resonancia. Porque le terminó de dar forma a una idea que venía zumbando en mi cabeza: aquello de que nuestra tarea es resolverle los problemas a los usuarios *también es una mentira que nos decimos a nosotros mismos*, también es una forma de evadirnos de la realidades económicas que determinan nuestro trabajo.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

Basta observar el negocio del software moderno, el sistema de incentivos económicos que lo rige y el lugar en el que pone a los usuarios, para reconocer que aquella idea es hoy una fantasía. Tanto en las plataformas *Big Tech* como en los productos de las startups incipientes, lo que vale no es la experiencia del usuario sino el potencial de crecimiento: se diseñan sistemas sin saber qué servicio concreto proveen; se los prepara para escalar globalmente cuando apenas tienen usuarios; se acumulan usuarios antes de encontrar un modelo de negocio sustentable; se aceptan inversiones exageradas para el potencial de ganancias; [se deteriora la experiencia de usuario](../2023-08-30-miscelanea-sobre-web-y-redes-sociales) para recuperar esas inversiones.

Este *modus operandi* de crecer a toda costa, buscar inversiones y preocuparse al final por generar ganancias &#x2014;sostenido, presumo, por un contexto económico global que no estoy en condiciones de analizar&#x2014; distorsiona las reglas del juego capitalista: ya no importa hacer un producto mejor y más barato que la competencia, importa construir un monopolio lo suficientemente rápido para impedir que la competencia llegue a existir o a tener posibilidades de supervivencia<sup><a id="fnr.6" class="footref" href="#fn.6" role="doc-backlink">6</a></sup>.

Los casos de Google y Facebook son ejemplares. Las dos empresas empezaron ofreciendo productos gratuitos, con un discurso que priorizaba al usuario y rechazaba los ads; las dos, una vez adquirida su posición dominante, se constituyeron en las agencias de publicidad más grandes de la historia<sup><a id="fnr.7" class="footref" href="#fn.7" role="doc-backlink">7</a></sup>.

Google se fundó alrededor de un buscador revolucionario que cambió la web para siempre. Era un producto que, en principio, no generaba ganancias, pero su superioridad tecnológica le valió a la empresa un flujo enorme de inversiones. Ningún otro de los productos de Google estuvo a la altura del buscador, pero eso no fue problema: con la financiación que obtuvo se dedicó a comprar lo que no podía desarrollar en casa: YouTube, Android, DoubleClick, Motorola, Waze, DeepMind<sup><a id="fnr.8" class="footref" href="#fn.8" role="doc-backlink">8</a></sup>. De forma parecida, Zuckerberg, que compitió y se impuso a MySpace en la guerra de las redes sociales, se aseguró de que nadie le pudiera hacer a él lo mismo: aunque Facebook se haya vuelto un basurero, bastó con comprar a la competencia (WhatsApp, Instagram) para retener a los usuarios.

El buscador de Google funciona hoy sensiblemente peor que hace veinte años, y amenaza con empeorar<sup><a id="fnr.9" class="footref" href="#fn.9" role="doc-backlink">9</a></sup>. Facebook se enmierdizó y supongo que Instagram, como diría Borges, *corre el mismo albur*. Ambas empresas constituyen monopolios explotadores de los que no podemos prescindir. En todos los casos el usuario es el producto y se lleva la peor parte.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

El supuesto de que ofrecerle un mejor servicio al usuario es la manera de aumentar el valor del software &#x2014;que era una abstracción conveniente de las *realidades económicas* que motivaban su producción&#x2014; dejó de ser cierto: ya no es una representación satisfactoria de la realidad. Hoy el beneficio económico pasa por otro lado. Pensábamos que el software tiene que deleitar al usuario pero la economía y buena parte de la industria nos exige que sucesivamente lo ignoremos, lo manipulemos y lo maltratemos. La neurosis del programador contemporáneo resulta de que pasó, en menos de una década, de tener una profesión demasiado buena para ser cierta a tener un *bullshit job*<sup><a id="fnr.10" class="footref" href="#fn.10" role="doc-backlink">10</a></sup>: un trabajo que no produce valor tangible, que hace del mundo un lugar peor, que resulta difícil de justificar incluso en los términos tradicionales del capitalismo.

¿Cómo conseguirse un empleo honesto en sistemas, sin tener que cambiar primero *el* sistema? ¿Qué nos queda si sacamos los proyectos de software imaginario, las redes sociales de vigilancia, las agencias publicitarias encubiertas, los productos que le hacen la cama a sus usuarios, las blockchains cuyos promotores oscilan entre el delirio místico y la estafa, la Inteligencia Alucinógena que riega con basura toda la web? ¿Existe todavía algún *kibutz* para deleitar a los usuarios sin corromperlos y sin engañarlos?

Elijo creer que sí. Consumidores de software no faltan. Necesidades tampoco.

<section class="footnotes" markdown=1>
## Notas

<sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> El mensaje original fue borrado, pero se puede leer el texto completo [acá](https://dcreager.net/2023/09/28-graydon-code-should-be-readable/).

<sup><a id="fn.2" class="footnum" href="#fnr.2">2</a></sup> En ese sentido cabe la comparación con otros oficios, sin pretensión de superioridad. La alusión al *poeta* que hace Hoare incurre en la romantización del oficio de escritor: la suposición de que consiste apenas en transcribir lo que dicta la inspiración cuando, en realidad, tiene mucho de pico y pala, prueba y error, sangre, sudor y lágrimas.

<sup><a id="fn.3" class="footnum" href="#fnr.3">3</a></sup> La [sublimación](https://es.wikipedia.org/wiki/Sublimaci%C3%B3n_(psicoan%C3%A1lisis)), que le dicen.

<sup><a id="fn.4" class="footnum" href="#fnr.4">4</a></sup> [Principles behind the Agile Manifesto](https://agilemanifesto.org/principles.html ).

<sup><a id="fn.5" class="footnum" href="#fnr.5">5</a></sup> Por eso los programadores de LucasArts organizaban "orgías de pizza" para que amigos y familiares prueben los juegos en desarrollo; por eso los de Midway ponían versiones preliminares del *NBA Jam* en un arcade del barrio para ver cómo reaccionaban los jugadores.

<sup><a id="fn.6" class="footnum" href="#fnr.6">6</a></sup> [“Metaverse” means “pivot to video”](https://archive.is/Fsd04).

<sup><a id="fn.7" class="footnum" href="#fnr.7">7</a></sup> Es curioso que los ads sean la solución preferida para improvisarle un modelo de negocio a los servicios de software: según el libro *Subprime Attention Crisis*, la industria de los ads se funda en supuestos incomprobables y conforma también una burbuja esperando por estallar.

<sup><a id="fn.8" class="footnum" href="#fnr.8">8</a></sup> [List of mergers and acquisitions by Alphabet](https://en.wikipedia.org/wiki/List_of_mergers_and_acquisitions_by_Alphabet#Key_acquisitions).

<sup><a id="fn.9" class="footnum" href="#fnr.9">9</a></sup> [Google’s AI Hype Circle](https://archive.is/ibHBY).

<sup><a id="fn.10" class="footnum" href="#fnr.10">10</a></sup> [On the Phenomenon of Bullshit Jobs](https://strikemag.org/bullshit-jobs/).

</section>