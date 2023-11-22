---
layout: post
title: "El dilema del ingeniero de software"
date: 2022-04-11
tags: [software]
---

¿Qué tienen en común Los *Venture Capitalists* (VCs) y Andrés Calamaro? Calamaro compone profusamente; siete de cada diez de sus canciones son descartables; graba material para cinco discos y, si no tiene a Joe Blaney  —ese mitológico productor yanqui que solamente es conocido en Argentina— respirándole en la nuca, publica los cinco discos enteros y después, por separado, edita una selección de quince canciones sólidas que incluye algún hit. El VC sigue el mismo *modus operandi* porque, con toda la información y el asesoramiento que el dinero puede comprar, identificar a una startup ganadora es una tarea improbable<sup><a id="fnr.1" class="footref" href="#fn.1" role="doc-backlink">1</a></sup>. Es más realista diversificar: apostar a veinte o cien y, cuando una es un hit, recuperar toda la inversión.

El problema del programador que elige trabajar en una startup es que no tiene la opción de diversificar. El programador de startup se juega su fuerza de trabajo, que es aproximadamente todo su capital, en una sola apuesta. Por más convencido que esté de su elección, por más esfuerzo que ponga de su parte para que el producto sea exitoso, es un objetivo que en mayor medida escapa a su control. El programador de startup compra un boleto de lotería pero sabe que tiene todas las de perder.

Poco me preocupan las consecuencias económicas de esta elección cuando, aún en su casi seguro fracaso, cualquier programador va a gozar de niveles de bienestar insólitamente superiores a los del resto de la sociedad. Lo que me interesa es el lado B de esa elección de carrera, lo que implica para el programador o el ingeniero de software optar entre un proyecto verde y uno maduro para desarrollar su actividad. Ahí está el dilema.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

La historia de la profesión, los libros y las universidades nos enseñaron a programar pensando en el largo plazo, tomando decisiones que favorezcan la sostenibilidad de los sistemas. La tarea del desarrollador no se limita a producir código que funcione sino que debe buscar oportunidades para reducir la complejidad del software o, como me gusta decir a mí, disminuir la entropía del Universo. Así lo explica John Ousterhout<sup><a id="fnr.2" class="footref" href="#fn.2" role="doc-backlink">2</a></sup>:

> If we want to make it easier to write software, so that we can build more powerful systems more cheaply, we must find ways to make software simpler. Complexity will still increase over time, in spite of our best efforts, but simpler designs allow us to build larger and more powerful systems before complexity becomes overwhelming. (&#x2026;) The first step towards becoming a good software designer is to realize that working code isn’t enough. It’s not acceptable to introduce unnecessary complexities in order to finish your current task faster. The most important thing is the long-term structure of the system. Most of the code in any system is written by extending the existing code base, so your most important job as a developer is to facilitate those future extensions. Thus, you should not think of “working code” as your primary goal, though of course your code must work. Your primary goal must be to produce a great design, which also happens to work. This is strategic programming. Strategic programming requires an investment mindset. Rather than taking the fastest path to finish your current project, you must invest time to improve the design of the system. These investments will slow you down a bit in the short term, but they will speed you up in the long term.

Las startups son por definición pura táctica y poca o ninguna estrategia. Todo conspira en contra del pensamiento de largo plazo: lo que importa es llegar a la próxima entrega, la próxima demo, la próxima ronda de inversión. ¿Cómo puede importar la deuda técnica acumulada si tal vez no haya producto ni empresa en seis meses?

> If you are in a company leaning in this direction, you should realize that once a code base turns to spaghetti, it is nearly impossible to fix. You will probably pay high development costs for the life of the product. Furthermore, the payoff for good (or bad) design comes pretty quickly, so there’s a good chance that the tactical approach won’t even speed up your first product release.

Creo que en esto Ousterhout exagera o peca de ingenuo. Hace falta una cantidad considerable de tiempo para recuperar la inversión, para que la calidad del código en un proyecto joven llegue a tener un impacto tangible para alguien que no sea programador. Sería imprudente abogar intransigentemente por el mejor diseño posible en contextos donde la supervivencia de la organización pasa más por el marketing y las finanzas que por la calidad futura del producto. Como dijo Gandalf, el ingeniero tiene que hacer lo mejor que pueda con el tiempo que le dan. Por oficio o por ética profesional, va a tratar de hacer las cosas bien, como le enseñaron: va a pensar estratégicamente, aunque solo pueda ejecutar una pequeña parte de lo que crea necesario. El verdadero problema es que, aunque obre de buena fe, el único tipo de decisiones que puede tomar son decisiones prematuras<sup><a id="fnr.3" class="footref" href="#fn.3" role="doc-backlink">3</a></sup>:

> Your early decisions make the biggest impact on the eventual shape of your system. The earliest decisions you make can be the hardest ones to reverse later. These early decisions about the system boundary and decomposition into subsystems get crystallized into the team structure, funding allocation, program management structure, and even time-sheet codes. Team assignments are the first draft of the architecture. It's a terrible irony that these very early decisions are also the least informed. The beginning is when your team is most ignorant of the eventual structure of the software, yet that's when some of the most irrevocable decisions must be made.

Volvamos al hecho de que la mayoría de las startups fracasan. De la misma forma que hace una apuesta arriesgada económicamente, el programador que elige una startup se está resignando a trabajar en software que posiblemente nunca llegue a producción o que termine teniendo un nivel de uso muy por debajo de los planes. La ironía es que las suposiciones con las que justifica la sostenibilidad de su diseño y la escalabilidad de su arquitectura nunca van a llegar a ser puestas a prueba; está trabajando en proyectos de laboratorio, castillos en el aire, *software imaginario*.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

En el extremo opuesto a la startup tenemos a la empresa rentable, con un modelo de negocio definido, con usuarios, con software que ya está en producción, a veces hace tanto tiempo que lo llamamos *legacy*. Este es el *software realmente existente* y, si bien el programador que se ocupa de él decididamente no construye castillos en el aire, ¿está construyendo algo? Más bien parece dedicado a aterrizar castillos concebidos por otros, hace mucho tiempo, unos que probablemente ya se fueron a otra empresa.

Así como al código se lo lee más frecuentemente de lo que se lo escribe, los sistemas son  operados y mantenidos más de lo que se los diseña. En el software realmente existente los cambios de diseño son lentos, progresivos, a largo plazo, muchas veces difíciles de justificar económicamente. Empezar de cero suele ser temerario o inviable.

Esta realidad parece incompatible con la formación del ingeniero de software, preparado para diseñar sistemas, concebir arquitecturas estratégicamente y administrar su evolución. Ni coincide con las inclinaciones de la mayoría de los que elegimos esta profesión, con nuestro interés por aplicar tecnologías modernas y construir herramientas sofisticadas. En el software realmente existente un monolito tiene más esperanza de vida que un conjunto de microservicios; es más rentable guardar archivos en S3 que operar una base de datos distribuida; una single-page application de React tiene menos chances de ganar el mercado que un [single-file PHP website](https://twitter.com/levelsio/status/1308145873843560449). Marianne Belloti da en la tecla en la introducción de su libro *Kill It with Fire*<sup><a id="fnr.4" class="footref" href="#fn.4" role="doc-backlink">4</a></sup>:

> We are past the point wherre all technical conversations and knowledge sharing can be about building new things. We have too many old things. People from my father's generation wrote a lot of programs, and every year they are shocked by how much of their work survives, still running in a production system somewhere. My generation has programmed exponentially more, infecting every aspect of life with a computer chip and some runtime instructions. We will be similarly shocked when those systems are still in place 30, 40, or 50 years from now.
> 
> Because we don't talk about modernizing old tech, organizations fall into the same traps over and over again. Failure is predictable beacuse so many software engineers think the conversations about modernizing legacy techonology are not relevant to their careers. Some of them are honestly surprised to find out that COBOL still runs much of the financial sector, that the majority of the web is still written in PHP, or that people are still looking to hire software engineers with ActionScript, Flash, and Visual Basic skills.

Entonces, este es el dilema del ingeniero de software: nos preparamos por años para diseñar sistemas estables que sobrevivan a largo plazo, pero tenemos que elegir entre el software imaginario, en el que la calidad de nuestro trabajo es indefinida y en última instancia indiferente, y el software realmente existente, que ya fue diseñado, cuyo mantenimiento es prácticamente una disciplina en sí misma, mucho menos glamorosa que la que nos dictan los libros, las universidades y las conferencias.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

No voy a negar los méritos de quienes saben identificar a un unicornio, ni mucho menos de los que ayudaron a concebir uno. Para ellos, mis felicitaciones. El problema es que su éxito no es reproducible: son ejemplos de emprendedorismo, pero no pueden ser modelos para la profesión, de la misma manera que los ganadores de la lotería no pueden ser modelos de movilidad social. Tiene que haber un camino de carrera realista para la ingeniería de software, uno que todavía sirva cuando los capitalistas se acuerden de generar ganancias y las startups tengan que rendir cuentas de lo que hacen.

El software realmente existente es, en definitiva, el único software del futuro. Suponiendo que todavía quede una civilización, ya acomodados en nuestro rol histórico de plomeros digitales, vamos a dedicarnos a eso: a convivir con las decisiones de nuestros predecesores, administrar la complejidad del software, disminuir la entropía del Universo.

<section class="footnotes" markdown=1>
## Notas
<!--- 
# Notas al pie de p&aacute;gina

 -->
<sup><a id="fn.1" href="#fnr.1">1</a></sup> *[How Many Startups Fail and Why?](https://www.investopedia.com/articles/personal-finance/040915/how-many-startups-fail-and-why.asp)*

<sup><a id="fn.2" href="#fnr.2">2</a></sup> John Ousterhout, *A Philosophy of Software Design*.

<sup><a id="fn.3" href="#fnr.3">3</a></sup> Michael T. Nygard, *Release It!*

<sup><a id="fn.4" href="#fnr.4">4</a></sup> Marianne Bellotti, *Kill It with Fire*.

</section>
