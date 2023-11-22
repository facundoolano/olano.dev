---
layout: post
title: "Worse is Better (is Worse (is Better))"
date: 2023-02-22
tags: [software]
thumbnail-img: assets/img/satriales2.png
share-img: assets/img/satriales2.png
image: assets/img/satriales2.png
cover-img: assets/img/satriales1.png
---

En 1989 Richard P. Gabriel publicó *Lisp: Good News, Bad News, How to Win Big*, un ensayo sobre la actualidad y el futuro de Lisp. Casi todo el texto resulta hoy anticuado y de interés solamente histórico pero hay una sección, [*The Rise of the Worse is Better*](https://www.dreamsongs.com/RiseOfWorseIsBetter.html), que se puede leer independientemente y es famosa por ponerle una etiqueta al estilo de desarrollo que predomina desde los '80 &#x2014;y a la cultura que lo rodea.

Gabriel propone dos escuelas alternativas de diseño de software: por un lado el estilo MIT, preferido por la comunidad de Lisp y, por otro, el estilo New Jersey, que se usó para diseñar Unix y C.
Si bien los dos buscan producir buen software en términos de **simplicidad**, **exactitud**, **consistencia** y **funcionalidad**, difieren en la importancia que le otorgan a cada uno de esos atributos y en qué están dispuestos a sacrificar.

Según el estilo MIT, al que Gabriel resume como *The Right Thing*, el diseño tiene que ser ante todo correcto y consistente. Además, tiene que contemplar la mayor cantidad de casos posible: aunque la simplicidad sea deseable &#x2014;sobre todo la simplicidad de la interface de los programas&#x2014; no se permite sacrificar funcionalidad para simplificar el diseño. El estilo New Jersey, al que se puede resumir como *Worse is Better*, valora la simplicidad por sobre todas las cosas, en particular la simplicidad de la implementación. Se puede sacrificar consistencia e incluso exactitud para hacer el software más simple, aunque lo mejor es sencillamente eliminar las partes del diseño que introducen complejidad. Se puede sacrificar funcionalidad en favor de cualquier otro de los atributos.

Gabriel dice que *Worse is Better* suele ser preferible porque produce software con mejores posibilidades de supervivencia. Como prioriza simplicidad de implementación ante todo, requiere menos esfuerzo de diseñar e implementar la funcionalidad esencial de un sistema &#x2014;digamos: el 50% más importante. En el caso de C y Unix, esto no solo significó que el sistema estuviera rápidamente disponible sino que fuera fácil de trasladar a nuevas plataformas, acelerando su propagación, que Gabriel compara con la de un (buen) virus. Una vez que el sistema es aceptado por los usuarios, aparece el incentivo para mejorarlo hasta ser *almost the right thing* y alcanzar el 90% de la funcionalidad ideal. El estilo MIT, en cambio, justamente por apuntar más alto tiende a fallar: el diseño toma demasiado tiempo, nunca se llega a completar la implementación o resulta demasiado compleja de reproducir en nuevos contextos.

En resumen, nos dice Richard Gabriel, lo mejor es no intentar una solución ideal. Nos conviene empezar con una solución *aceptable*, conseguir usuarios y recién entonces dedicarnos a mejorar el diseño hasta alcanzar una solución *suficientemente buena*. A lo largo de los años (y a la luz de la popularidad de su ensayo), Gabriel [revisaría su argumento](https://www.dreamsongs.com/WorseIsBetter.html) y publicaría otros, a favor y en contra de la cultura del *Worse is Better*.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

El argumento a favor del estilo New Jersey nos atrae, en primer lugar porque la historia lo confirma: durante los '90 el virus Unix continuó propagándose, le siguió la revolución de Linux<sup><a id="fnr.1" class="footref" href="#fn.1" role="doc-backlink">1</a></sup>, hoy en día todos los sistemas operativos son de una forma u otra sus herederos. C inició una tradición de lenguajes &#x2014;C++, Java, JavaScript, Go&#x2014; todos ellos dominantes y menos que perfectos. Lisp sigue sobreviviendo con respirador artificial y lenguajes ejemplares como Eiffel, SmallTalk y Haskell resultaron apenas buenos *influencers*<sup><a id="fnr.2" class="footref" href="#fn.2" role="doc-backlink">2</a></sup>. Más allá de tecnologías específicas, encontramos rastros del *Worse is Better* en la cultura, en el sentido común de la industria: las metodologías ágiles, el diseño iterativo, [*perfect is the enemy of good*](https://en.wikipedia.org/wiki/Perfect_is_the_enemy_of_good), [*you ain't gonna need it*](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it), [*do the simplest thing that could possibly work*](http://wiki.c2.com/?DoTheSimplestThingThatCouldPossiblyWork), [*not everything worth doing is worth doing well*](https://en.wikipedia.org/wiki/The_Soul_of_a_New_Machine).

Pero hay otra razón por la que la filosofía *Worse is Better* resuena con nuestra experiencia. Cuando aprendemos a programar es lógico que nuestro objetivo sea hacer las cosas lo mejor posible, sin concesiones. La programación parece una rama de la lógica, una más de las ciencias exactas: tiene que haber una solución precisa para cada problema y es nuestra responsabilidad encontrarla. Más tarde, cuando empezamos a trabajar como desarrolladores, nos encontramos con que es necesario y deseable ser pragmático, que hay que considerar factores que exceden al código, justificar nuestras decisiones según sus costos y beneficios. Que hay muchas dimensiones de *lo correcto,* algunas de ellas subjetivas, algunas más relevantes que otras. Que hay que convencer a los demás, generar consensos, tomar decisiones en equipo.

En la oposición entre MIT y New Jersey hay ecos de Academia contra Industria, de Ciencia contra Ingeniería. La aceptación de que *Peor es Mejor* es parte de nuestro tránsito hacia la profesionalidad.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

Los desarrolladores convivimos con la tensión entre hacer las cosas bien y hacerlas económicamente &#x2014;maximizar calidad o minimizar esfuerzo. John Ousterhout<sup><a id="fnr.3" class="footref" href="#fn.3" role="doc-backlink">3</a></sup> habla de esa tensión cuando describe las [actitudes táctica y estratégica](../2022-04-11-el-dilema-del-ingeniero-de-software) para abordar la programación. La programación táctica consiste en tomar el camino más corto para resolver una tarea. La programación estratégica nos pide aprovechar cada oportunidad para mejorar el diseño del sistema. Según Ousterhout, es una inversión que paga a largo plazo con una reducción en los tiempos de desarrollo.

Aunque es la actitud más razonable, la programación estratégica es también una forma de *the right thing*, no necesariamente adecuada a todas las circunstancias. Claro que Ousterhout no propone adoptar dogmáticamente la mirada de largo plazo sino más bien lo contrario: *no adoptar ciegamente una actitud táctica*. *Worse is Better* se convierte en un problema cuando [se lo adopta como un eslogan](http://pchiusano.github.io/2014-10-13/worseisworse.html): cuando se opta por la solución más fácil sin analizar las alternativas o incluso se desestima ese análisis como una pérdida de tiempo. Si extraemos la conclusión de que *the right thing* es siempre contraproducente y que la enseñanza de Unix es que alcanza con hacer las cosas *más o menos bien*, entonces vamos a producir software consistentemente malo, software con menos posibilidades de supervivencia y en el que no nos satisface trabajar, con el que no estamos comprometidos.

Aunque la *única acción moral sea la* [*minimización de la entropía*](../2022-11-28-posdata-sobre-la-complejidad-esencial), los desarrolladores convivimos con fuerzas que nos exigen trabajar en la dirección opuesta. La utilidad del software se juzga por aspectos observables fuera del código: el valor que le provee a los usuarios, el costo de producirlo. El abuso de *Worse is Better* pasa fácilmente desapercibido; la calidad de un diseño, cuando los cosas funcionan bien, es de interés exclusivo de los programadores. Solo se vuelve una preocupación para el resto de la organización cuando el desarrollo se estanca o cuando aumentan los errores. Es decir, cuando el deterioro es más difícil de revertir. ¿Cómo podemos conciliar la responsabilidad de realizar *the right thing* con los objetivos de negocio, con cumplir expectativas y brindar un servicio?

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

En su ensayo [*Hackers and Painters*](http://www.paulgraham.com/hp.html), Paul Graham propone que los hackers son artesanos, su objetivo crear cosas buenas y bellas, sin concesiones. Una idea romántica que suena parecida a *the right thing*<sup><a id="fnr.4" class="footref" href="#fn.4" role="doc-backlink">4</a></sup>. Los hackers, dice, tienen más para aprender de otras disciplinas creativas &#x2014;arquitectura, [escritura](../2021-02-01-suenan-los-programadores-con-poemas-electricos), especialmente pintura&#x2014; que de la ciencia y la ingeniería.
Profesional o artesano; hacker o ingeniero; pragmático o idealista, ¿son formas opuestas? ¿Tendremos que llevar vidas paralelas, como sugiere Graham, un *day job* de ingenieros para ganar plata y una vocación de hacker a la que dedicarnos por las noches y los fines de semana<sup><a id="fnr.5" class="footref" href="#fn.5" role="doc-backlink">5</a></sup>?

Yo creo que es preferible mantener vivo ese orgullo de artesano. Aunque no sea lo que determine el éxito de nuestro trabajo, negar la belleza es matar un poco la profesión, matar aquello que tal vez nos hizo &#x2014;nos hace&#x2014; elegirla. Hay que encontrar una manera de dosificar esa pulsión por lo bueno y lo bello, cultivarla sin dejar que sea la sola fuerza conductora de nuestras decisiones, camuflarla. Darle una fachada de pragmatismo ingenieril a nuestro núcleo idealista.

Los desarrolladores, ya se sabe, somos equilibristas. La [primera ley de la arquitectura de software](../2020-09-15-tldr-fundamentals-of-software-architecture/) es *everything is a trade-off*; la respuesta a la mayoría de las preguntas: *depende*. Tenemos que adoptar algún criterio para no caer de ninguno de los dos lados del abismo. Hay que ser pragmáticos, sí, hay que aceptar que no siempre podemos optar por *la solución correcta* pero también hay que saber que, aunque *Peor es Mejor*, sigue siendo peor, y está bien que nos resulte incómodo, que nos quite un poco el sueño. Que la [deuda técnica](https://en.wikipedia.org/wiki/Technical_debt) devenga *culpa* técnica.

Entonces solo vamos a permitirnos cortar camino cuando lo justifique un análisis; vamos a simplificar el código aunque ya funcione; vamos a negociar por tiempo para mejorar los sistemas o vamos a pasar las mejoras por contrabando. Sembrar belleza al costado del camino, maximizar el beneficio de la complejidad que eliminemos. Pensar estratégicamente, aunque solo alcancemos a ejecutar una parte de lo que creamos necesario. Hacer lo que se pueda con el tiempo que tengamos.

<section class="footnotes" markdown=1>
## Notas
<!--- 
# Notas al pie de p&aacute;gina

 -->
<sup><a id="fn.1" href="#fnr.1">1</a></sup> Eric S. Raymond, el maestro Zen de Unix, actualiza el argumento de Richard Gabriel con el caso de éxito de Linux en su ensayo [*The Cathedral and the Bazaar*](http://users.ece.utexas.edu/~perry/education/382v-s08/papers/raymond.pdf). El movimiento Open Source del que Raymond fue vocero y que se impuso al Software Libre de Richard Stallman, es otra instancia de *Worse is Better* contra *The Right Thing*.

<sup><a id="fn.2" href="#fnr.2">2</a></sup> Incluso al interior de sus respectivos nichos, las encarnaciones más pragmáticas &#x2014;Clojure, Erlang, Elixir&#x2014; parecen conseguir mejor adopción.

<sup><a id="fn.3" href="#fnr.3">3</a></sup> Los lectores habituales de este blog a esta altura ya sabrán que *A Philosophy of Software Design* es mi *I Ching*.

<sup><a id="fn.4" href="#fnr.4">4</a></sup> Quizás no sea coincidencia que Graham venga del mundo Lisp.

<sup><a id="fn.5" href="#fnr.5">5</a></sup> Teorema: *Work, Hacking, Life. Pick two*.

</section>
