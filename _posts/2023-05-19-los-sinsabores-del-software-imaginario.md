---
layout: post
title: "Los sinsabores del software imaginario"
date: 2023-05-19
tags: [software]
thumbnail-img: assets/img/imaginary.png
share-img: assets/img/imaginary2.png
image: assets/img/imaginary2.png
---

Los otros días circuló un artículo del equipo de Prime Video<sup><a id="fnr.1" class="footref" href="#fn.1" role="doc-backlink">1</a></sup> en el que cuentan cómo, contrayendo un conjunto de microservicios a una aplicación monolítica, resolvieron un cuello de botella y redujeron los costos de infraestructura en un 90%. La noticia llamó la atención, por un lado porque se supone que todo el chiste de los microservicios era facilitar la escalabilidad de los sistemas y, por otro, porque venía justamente de Amazon que, cabe suponer, es el principal beneficiario del derroche en infraestructura. Los detractores de los microservicios, que estaban agazapados esperando su oportunidad, se apuraron a leer el artículo como una admisión de derrota y prueba de la inviabilidad del modelo<sup><a id="fnr.2" class="footref" href="#fn.2" role="doc-backlink">2</a></sup>, mientras que sus defensores reaccionaron explicando que el problema no es <del>el comunismo</del> la Arquitectura Orientada a Servicios, sino sus implementaciones existentes<sup><a id="fnr.3" class="footref" href="#fn.3" role="doc-backlink">3</a></sup>.

El de los microservicios es un caso más de tecnología que tiene su utilidad en un contexto determinado, que se pone de moda y se empieza a utilizar indiscriminadamente fuera de ese contexto y termina causando mucho más daño del que alivia<sup><a id="fnr.4" class="footref" href="#fn.4" role="doc-backlink">4</a></sup>. Mi percepción es que la moda (el uso indiscriminado, por defecto) ya pasó hace unos años y que, a esta altura, ensañarse contra la tecnología es como pegarle a alguien que está en el suelo. Pero me interesa revisar el trasfondo de aquella moda, caso particular de una tendencia generalizada en la industria: el "preparacionismo" del software imaginario, que justifica la implementación de soluciones complicadas a problemas que no existen<sup><a id="fnr.5" class="footref" href="#fn.5" role="doc-backlink">5</a></sup>.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

El estilo de arquitectura de microservicios no resuelve un problema técnico o de negocio sino uno organizacional. Es una manera, siguiendo las leyes de Conway<sup><a id="fnr.6" class="footref" href="#fn.6" role="doc-backlink">6</a></sup> y Brooks<sup><a id="fnr.7" class="footref" href="#fn.7" role="doc-backlink">7</a></sup>, de desacoplar los componentes de un ecosistema para que cada uno pueda ser desarrollado y operado por equipos independientes, reduciendo la coordinación y la fricción típicos de los sistemas compartidos (y el caos alternativo del equipo único que crece indefinidamente).

Implementar microservicios implica una gran inversión inicial y un esfuerzo constante de mantenimiento: más componentes, más costos de infraestructura, más dificultad en ejecutar los servicios localmente, la necesidad de estandarizar la funcionalidad común (configuración, deployment, logging, monitoreo, seguridad), de implementar mecanismos para encontrar y comunicar los servicios y para garantizar la consistencia de los datos, etc. Quizás el mayor de los problemas, sobre el que no se insiste lo suficiente, es que los sistemas distribuidos son *complicados<sup><a id="fnr.8" class="footref" href="#fn.8" role="doc-backlink">8</a></sup>* y es un error grave hacer de cuenta que da igual llamar una función local que ejecutar un procedimiento remoto<sup><a id="fnr.9" class="footref" href="#fn.9" role="doc-backlink">9</a></sup>.

Toda esa inversión solo tiene sentido en organizaciones grandes, cuando hay oportunidades concretas de asignarle servicios distintos (preferentemente pocos) a cada equipo y obtener el beneficio del desarrollo independiente. Sam Newman, autor del texto canónico sobre microservicios<sup><a id="fnr.10" class="footref" href="#fn.10" role="doc-backlink">10</a></sup>, nos previene desde el principio:

> Despite the drive in some quarters to make microservice architectures the default approach for software, I feel that because of the numerous challenges I’ve outlined, adopting them still requires careful thought. (&#x2026;) For a small team, a microservice architecture can be difficult to justify because there is work required just to handle the deployment and management of the microservices themselves. Some people have described this as the “microservice tax.” When that investment benefits lots of people, it’s easier to justify. But if one person out of your five-person team is spending their time on these issues, that’s a lot of valuable time not being spent building your product.

Una de las razones por las que usar microservices *por default* podría parecer una buena idea, es que
si el software y la organización crecen (y ¿quién no espera que su proyecto sea exitoso?), el trabajo de dividir y repartir el sistema ya estaría hecho. Pero  Newman lo desmiente:

> I do see a temptation for startups to go microservice first, the reasoning being, “If we’re really successful, we’ll need to scale!” The problem is that you don’t necessarily know if anyone is even going to want to use your new product. And even if you do become successful enough to require a highly scalable architecture, the thing you end up delivering to your users might be very different from what you started building in the first place. Uber initially focused on limos, and Flickr spun out of attempts to create a multiplayer online game. The process of finding product market fit means that you might end up with a very different product at the end than the one you thought you’d build when you started. (&#x2026;) It’s much easier to move to microservices later, after you understand where the constraints are in your architecture and what your pain points are—then you can focus your energy on using microservices in the most sensible places.

Este preparacionismo es la naturaleza de lo que en [otro post](../../2022-04-11-el-dilema-del-ingeniero-de-software) llamé *software imaginario*<sup><a id="fnr.11" class="footref" href="#fn.11" role="doc-backlink">11</a></sup>, software que en una etapa temprana, cuando hay menos información disponible &#x2014;pocos usuarios, un modelo de negocio poco claro&#x2014;, se ajusta para un futuro que probablemente no llegue o que si llega lo hará de forma imprevisible. El compromiso con el proyecto se confunde con optimismo y justifica elecciones de tecnología &#x2014;arquitecturas escalables, bases de datos distribuidas, lenguajes rústicos&#x2013; que inducen un costo innecesario en el corto plazo e incluso pueden llegar a ser contraproducentes en el caso de que el software efectivamente necesite escalar. Es preferible optar por la simplicidad: tomar el camino que nos dé más libertad de movimiento en el futuro, y que nos traiga ese futuro lo antes posible.

La propuesta no es novedosa; en lo que hace al diseño de programas, en la industria decantó un sentido común que prefiere [limitarse a lo necesario](../../2023-02-22-worse-is-better-is-worse-is-better) y que incluso asume la misión de [reducir la complejidad](../../2022-11-28-posdata-sobre-la-complejidad-esencial) en el proceso de desarrollo. Pero, por alguna razón, esa austeridad no alcanza a la elección de tecnologías ni al armado de infraestructura. Resabio, tal vez, de la época en que la arquitectura se concebía como la parte del sistema que hay que definir al principio y que no se puede cambiar.

O Acaso el fenómeno se pueda explicar sociológicamente: nos entrenamos como ingenieros y científicos para resolver problemas difíciles; un trabajo ejecutado con sencillez puede parecer poco meritorio o por debajo de nuestras capacidades, la simplicidad se toma por simpleza. A fin de cuentas, la sociedad contemporánea es una inmensa máquina de marketing y las soluciones rebuscadas nos permiten escribir papers y hablar en conferencias, las *buzzwords* le dan brillo a los currículums y hacen subir las acciones de startups con balances negativos. La austeridad es para los pobres.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

La mayor parte de mi carrera la dediqué, a pesar mío, a proyectos de software imaginario: sistemas que nunca llegaban a producción, productos fallidos, modernizaciones que no igualaban al sistema que se proponían reemplazar. Cuando finalmente conseguí un trabajo de software real &#x2014;un proyecto de escala global con casi una década en producción y restricciones muy específicas de performance&#x2014;, me sorprendió descubrir que no aplicaba ninguna de las herramientas y prácticas sofisticadas que había estudiado durante años. Las instancias se levantaban y morían sin coordinación, los datos se mantenían en memoria para evitar la necesidad y la latencia de un acceso a base de datos, la comunicación entre servicios se hacía escribiendo y leyendo archivos en S3, con bash y cron. La arquitectura equivalente que me imaginaba antes de empezar en ese trabajo, usando Kafka o RabbitMQ para mover los datos en tiempo real, no solo requería más código y más dificultad operacional sino que implicaba más gastos de infraestructura y daba menos garantías de disponibilidad.

Los problemas del software real no nos requerían lidiar con algoritmos complejos ni arquitecturas distribuidas sino reducir costos de infraestructura, automatizar tareas frecuentes, mejorar la observabilidad del sistema y estudiar sus modos de fallo para hacerlo más estable. Dedicábamos más tiempo a *operar* el sistema que a escribir código; partir nuestro majestuoso monolito hubiera multiplicado el trabajo sin agregar valor.

Esa experiencia personal parece coincidir con otras más notables, la de Basecamp<sup><a id="fnr.12" class="footref" href="#fn.12" role="doc-backlink">12</a></sup>, Stack Overflow<sup><a id="fnr.13" class="footref" href="#fn.13" role="doc-backlink">13</a></sup><sup>, </sup><sup><a id="fnr.14" class="footref" href="#fn.14" role="doc-backlink">14</a></sup>, Shopify<sup><a id="fnr.15" class="footref" href="#fn.15" role="doc-backlink">15</a></sup>, la  del emprendedor serial Pieter Levels<sup><a id="fnr.16" class="footref" href="#fn.16" role="doc-backlink">16</a></sup>. Incluso en organizaciones grandes, en las que cabe suponer la necesidad de construir soluciones más complejas, la experiencia prescribe simplicidad. Esto concluía en 2007 James Hamilton, sobre los sistemas de escala global en Microsoft<sup><a id="fnr.17" class="footref" href="#fn.17" role="doc-backlink">17</a></sup>:

> 1.  Expect failures. A component may crash or be stopped at any time. Dependent components might fail or be stopped at any time. There will be network failures. Disks will run out of space. Handle all failures gracefully.
> 2.  Keep things simple. Complexity breeds problems. Simple things are easier to get right. Avoid unnecessary dependencies. Installation should be simple. Failures on one server should have no impact on the rest of the data center.
> 3.  Automate everything. People make mistakes. People need sleep. People forget things. Automated processes are testable, fixable, and therefore ultimately much more reliable. Automate wherever possible.

Más específicamente:

> Complicated algorithms and component interactions multiply the difficulty of debugging, deploying, etc. Simple and nearly stupid is almost always better in a high-scale service &#x2014;the number of interacting failure modes is already daunting before complex optimizations are delivered. Our general rule is that optimizations that bring an order of magnitude improvement are worth considering, but percentage or even small factor gains aren’t worth it.

Los desarrolladores de software somos plomeros<sup><a id="fnr.18" class="footref" href="#fn.18" role="doc-backlink">18</a></sup>. Y cuando el software escala no pasamos a ser ingenieros hidráulicos: seguimos siendo plomeros. Con más inodoros, con caños más largos.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

Manifiestos como *Choose Boring Techonology*<sup><a id="fnr.19" class="footref" href="#fn.19" role="doc-backlink">19</a></sup> y *Radical Simplicty<sup><a id="fnr.20" class="footref" href="#fn.20" role="doc-backlink">20</a></sup>* se proponen como antídotos para el preparacionismo y el glamour de la complejidad:

> MySQL is boring. Postgres is boring. PHP is boring. Python is boring. Memcached is boring. Squid is boring. Cron is boring. The nice thing about boringness is that the capabilities of these things are well understood. But more importantly, their failure modes are well understood. (&#x2026;) The “best” tool is the one that occupies the “least worst” position for as many of your problems as possible. It is basically always the case that the long-term costs of keeping a system working reliably vastly exceed any inconveniences you encounter while building it. Mature and productive developers understand this.

> Radical Simplicity means having as few components and moving parts as possible. Reuse technology for different purposes instead of having a new moving part for each purpose. (&#x2026;) A much smaller setup that achieves the same but has much fewer moving parts that need to be maintained, learned and debugged. Many fewer components need to be monitored, added to a logging server and alerts created. Do some companies need that complex setup when they have 50+ developers and millions of users? Yes. Do most of the companies, especially in their first years, need that complex setup? No.

Eligiendo tecnologías y arquitecturas "aburridas", y limitando la cantidad de componentes, se reduce la carga de trabajo operacional y de mantenimiento, recuperando ese tiempo para proveer valor de negocio.

En sus ensayos clásicos<sup><a id="fnr.21" class="footref" href="#fn.21" role="doc-backlink">21</a></sup><sup>, </sup><sup><a id="fnr.22" class="footref" href="#fn.22" role="doc-backlink">22</a></sup>, Paul Graham describía cómo (en una era anterior de internet y del capitalismo) su startup le había sacado ventaja a la competencia ahorrándose la burocracia de las empresas grandes y usando como arma secreta un lenguaje de programación mejor adecuado al problema. Acaso hoy exista una nueva oportunidad &#x2014;mientras la industria se hunde bajo su propio peso y la mayoría infla burbujas con el zumbido que está de moda&#x2014; de construir valor con herramientas aburridas, radicalmente simples.

<section class="footnotes" markdown=1>
## Notas
<!--- 
# Notas al pie de p&aacute;gina

 -->
<sup><a id="fn.1" href="#fnr.1">1</a></sup> [Scaling up the Prime Video audio/video monitoring service and reducing costs by 90%](https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90).

<sup><a id="fn.2" href="#fnr.2">2</a></sup> [How to recover from microservices](https://world.hey.com/dhh/how-to-recover-from-microservices-ce3803cc).

<sup><a id="fn.3" href="#fnr.3">3</a></sup> En realidad dijeron ([acá](https://twitter.com/samnewman/status/1654432661337788416) y [acá](https://adrianco.medium.com/so-many-bad-takes-what-is-there-to-learn-from-the-prime-video-microservices-to-monolith-story-4bd0970423d4)) que el artículo hablaba más de los costos de usar lambdas en vez de servidores, pero preferí quedarme con el chiste comunista.

<sup><a id="fn.4" href="#fnr.4">4</a></sup> Me resulta parecido al de los patrones de diseño clásicos del *Gang of Four*.

<sup><a id="fn.5" href="#fnr.5">5</a></sup> Vale aclarar que los desarrolladores de Prime Video dicen que su arquitectura inicial de lambdas les permitió experimentar rápido con el producto, por lo que no es un ejemplo del preparacionismo que describo en este artículo.

<sup><a id="fn.6" href="#fnr.6">6</a></sup> [Ley de Conway](https://en.wikipedia.org/wiki/Conway%27s_law): "Las organizaciones dedicadas al diseño de sistemas están abocadas a producir diseños que son copias de las estructuras de comunicación de dichas organizaciones".

<sup><a id="fn.7" href="#fnr.7">7</a></sup> [Ley de Brooks](https://en.wikipedia.org/wiki/Brooks%27s_law): "Si crece el número de personas, también crecerá el tiempo invertido en tratar de averiguar lo que hace el resto".

<sup><a id="fn.8" href="#fnr.8">8</a></sup> [Fallacies of distributed computing](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing).

<sup><a id="fn.9" href="#fnr.9">9</a></sup> [A Note on Distributed Computing](https://scholar.harvard.edu/files/waldo/files/waldo-94.pdf).

<sup><a id="fn.10" href="#fnr.10">10</a></sup> [Building Microservices, 2nd Edition](https://www.oreilly.com/library/view/building-microservices-2nd/9781492034018/).

<sup><a id="fn.11" href="#fnr.11">11</a></sup> En contraposición al software *realmente existente*, el que ya está en producción y tiene una cantidad no despreciable de usuarios a los que les provee alguna utilidad.

<sup><a id="fn.12" href="#fnr.12">12</a></sup> [The Majestic Monolith](https://m.signalvnoise.com/the-majestic-monolith/).

<sup><a id="fn.13" href="#fnr.13">13</a></sup> [How will you design the Stack Overflow website?](https://twitter.com/alexxubyte/status/1577684758779203584?lang=es).

<sup><a id="fn.14" href="#fnr.14">14</a></sup> [Stack Exchange performance](https://stackexchange.com/performance).

<sup><a id="fn.15" href="#fnr.15">15</a></sup> [Deconstructing the Monolith: Designing Software that Maximizes Developer Productivity](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity).

<sup><a id="fn.16" href="#fnr.16">16</a></sup> [RemoteOK.io is a single PHP file](https://twitter.com/levelsio/status/1308145873843560449).

<sup><a id="fn.17" href="#fnr.17">17</a></sup> [On Designing and Deploying Internet Scale Services](https://s3.amazonaws.com/systemsandpapers/papers/hamilton.pdf).

<sup><a id="fn.18" href="#fnr.18">18</a></sup> [The Bulk of Software Engineering is Just Plumbing](https://www.karllhughes.com/posts/plumbing).

<sup><a id="fn.19" href="#fnr.19">19</a></sup> [Choose Boring Technology](https://mcfunley.com/choose-boring-technology).

<sup><a id="fn.20" href="#fnr.20">20</a></sup> [Radical Simplicity](https://www.radicalsimpli.city/).

<sup><a id="fn.21" href="#fnr.21">21</a></sup> [Beating the Averages](http://www.paulgraham.com/avg.html).

<sup><a id="fn.22" href="#fnr.22">22</a></sup> [Hackers and Painters](http://www.paulgraham.com/hp.html).

</section>
