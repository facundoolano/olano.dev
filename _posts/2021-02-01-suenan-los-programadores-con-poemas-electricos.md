---
layout: post
title: "¿Sueñan los programadores con poemas eléctricos?"
subtitle: Programación y escritura
date: 2021-02-01
tags: [programación, software, literatura]
favorite: true
---

Alguna vez me dijeron que era un *inmenso pajero* por proponer que la programación es una rama de la literatura<sup><a id="fnr.1" class="footref" href="#fn.1" role="doc-backlink">1</a></sup>. No voy a negar las fuertes notas ahumadas de la frase, pero sí creo que hay puntos de contacto entre las dos disciplinas y que puede ser útil observarlos.

La programación se realiza mediante la palabra escrita; está más o menos aceptado que el código se dirige tanto a la computadora como a otros humanos, que (con la excepción de Perl) el código se lee muchas más veces de las que se escribe. Partiendo de ahí, hace falta apenas un salto para convenir en que *más que decirle a la computadora lo que tiene que hacer, la tarea del programador es explicarle a otro ser humano lo que quiere que haga la computadora*<sup><a id="fnr.2" class="footref" href="#fn.2" role="doc-backlink">2</a></sup>.

Si aceptamos esto, ya no alcanza con preocuparnos por la "legibilidad" &#x2014;poner buenos nombres a las variables, evitar el código excesivamente denso o anidado&#x2014; sino que tenemos que orientar nuestros esfuerzos a comunicar una idea con la mayor eficacia posible.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

Es un lugar común de los escritores decir que no piensan en sus lectores cuando escriben, que lo hacen para sí mismos, quizás como una manera de demostrar que no hacen concesiones a los intereses del público o del mercado. Pero lo cierto es que todos escribimos para ser leídos, aunque nuestro lector ideal no se corresponda con alguien concreto, aunque todavía no haya nacido; siquiera inconscientemente, la escritura conlleva la construcción de un lector modelo, es decir, un lector imaginario que orienta las elecciones del autor, por ejemplo la del nivel de detalle que debe proveer para que el texto sea interpretado<sup><a id="fnr.3" class="footref" href="#fn.3" role="doc-backlink">3</a></sup>.

Para un programador profesional, el lector modelo debería aproximar no solo a sus actuales colegas sino a su yo futuro, a cualquier futuro responsable del código, incluso a quien tenga que consultarlo ocasionalmente en busca de información. ¿Cómo podríamos ponernos en los zapatos de semejante conjunto de personas abstractas? No creo que haya un método satisfactorio; lo mejor que se me ocurre es imaginarse a uno mismo abordando el código con el contexto y el conocimiento del que disponía uno, dos, cinco años atrás. No importa cuánto lo intentemos, es imposible producir código accesible para todo el mundo; se trata más bien de decidir conscientemente, sin frivolidad, a quién se deja afuera.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

El escritor de ficción tiene la tarea improbable de equilibrar un sistema infinitamente complejo, tomar decisiones sobre cada elemento y sobre el conjunto: el orden en que revela información y despliega la trama, la longitud, la cadencia de las frases, la manera en que intercala pasajes descriptivos y diálogos, hasta las asociaciones que prevé evocar en su lector con la elección de este o aquel adjetivo. De igual manera el programador dispone de toda una paleta de instrumentos que pueden servir o conspirar contra la tarea de expresar las intenciones de su programa: la estructura de directorios y archivos, las interfaces de sus módulos, la longitud de las funciones y el orden en que se las presenta, el uso de comentarios, la decisión de nombrar expresiones y el nombre que se les da, el estilo con el que se manipulan los datos y se controla el flujo del programa, y hasta el lugar donde se colocan los espacios en blanco.

A medida que escribimos el código y sobre todo durante la etapa de corrección (cuando el problema está resuelto en nuestra cabeza, el programa ya funciona y podemos reorganizarlo  en la forma que mejor comunique la solución), deberíamos hacer el intento de mirarlo con los ojos de nuestro lector modelo. ¿Qué va a ver una persona cuando liste el directorio del proyecto o entre a GitHub, cuando lea el README y siga los links que le ofrecemos, cuando abra un archivo y lea su encabezado y las primeras funciones hacia las que tratamos de llamar su atención? ¿Qué tan bien lograremos transmitir nuestra idea a alguien que recorra ese camino?

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

Los escritores profesionales suelen trabajar con un editor; alguien que puede dar impresiones, intercambiar ideas con el autor, sugerir (o exigir) cambios<sup><a id="fnr.4" class="footref" href="#fn.4" role="doc-backlink">4</a></sup>. Se trata de un lector concreto que complementa al lector modelo de la etapa creativa; creo que este rol se asemeja un poco al del colega que hace un *peer review* cuando el código todavía está en desarrollo<sup><a id="fnr.5" class="footref" href="#fn.5" role="doc-backlink">5</a></sup>.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

Hay autores que recomiendan tomar distancia del texto después de escribir el primer borrador, dejarlo descansar por unas semanas en el cajón<sup><a id="fnr.6" class="footref" href="#fn.6" role="doc-backlink">6</a></sup>. Esto les permite retomarlo con una mirada fresca, como si otra persona lo hubiera escrito, detectar problemas que la extrema familiaridad del trabajo cotidiano les había ocultado.

Los programadores no podemos permitirnos olvidar el código por un tiempo; en la mayoría de los casos queremos usarlo tan rápido como sea posible, incluso antes. Hay mucho potencial de mejora en el pasaje a producción, mucho más de lo que la sola distancia con el código puede ofrecernos. Esto no invalida del todo el método del cajón, sin embargo: para nosotros, pasar el código a producción de alguna manera *es* dejarlo en el cajón.

Si suscribimos a la idea de *Refactoring*, el código nunca está terminado, siempre es posible tomar un programa que funciona y pulirlo, mejorar su estructura. Después del desarrollo inicial de un programa, después de ponerlo en uso y corregirlo, cuando consideramos que la funcionalidad es aceptable, podemos olvidarnos del código por un tiempo; podemos volver a él, meses más tarde, evaluarlo con el beneficio de la distancia, encontrar oportunidades de mejora, refactorizar.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

En el afán de enojar a un grupo mayor de personas, podría cerrar diciendo que algunos criterios comunes de la programación son igualmente aplicables a la escritura en prosa: *divide and conquer*, *keep it simple, stupid*, *don't repeat yourself*. Ciertamente, yo escribo como si estuviera programando; quizás eso explique la tendencia de mis textos a componer secuencias de párrafos levemente acoplados, secuencias que se diluyen hacia al final y terminan abruptamente, como esta.

<section class="footnotes" markdown=1>
## Notas
<!--- 
# Notas al pie de p&aacute;gina

 -->
<sup><a id="fn.1" href="#fnr.1">1</a></sup> [A pythonist finds a new home at Clojure land](https://www.reddit.com/r/programming/comments/65ct5j/a_pythonist_finds_a_new_home_at_clojure_land/dgau7bp/?utm_source=reddit&utm_medium=web2x&context=3).

<sup><a id="fn.2" href="#fnr.2">2</a></sup> [Literate Programming](http://www.literateprogramming.com/knuthweb.pdf), de Donald Knuth.

<sup><a id="fn.3" href="#fnr.3">3</a></sup> [Lector in Codigo](https://alvaro-videla.com/2018/05/lector-in-codigo.html#the-model-reader), de Álvaro Videla.

<sup><a id="fn.4" href="#fnr.4">4</a></sup> [The Art of Editing No. 1](https://www.theparisreview.org/interviews/1760/the-art-of-editing-no-1-robert-gottlieb), entrevista a Robert Gottlieb.

<sup><a id="fn.5" href="#fnr.5">5</a></sup> Me gustaría una herramienta de GitHub que permitiera presentar los cambios de un pull request en un orden arbitrario, intercalando texto descriptivo, una especie de *literate diffing*.

<sup><a id="fn.6" href="#fnr.6">6</a></sup> Por ejemplo: [Chéjov](https://www.pagina12.com.ar/diario/suplementos/libros/subnotas/1823-238-2005-11-13.html) y [Stephen King](https://www.businessinsider.com/stephen-king-on-how-to-write-2014-8#20-when-youre-finished-writing-take-a-long-step-back-220).

---

[English version](../../2021-09-22-do-programmers-dream-of-electronic-poems).

</section>
