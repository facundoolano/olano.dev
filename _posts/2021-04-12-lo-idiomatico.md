---
layout: post
title: "Lo idiomático"
date: 2021-04-12
tags: [programación, software]
css: "highlight"
---

La semana pasada circuló [un repositorio de José Valim](https://github.com/josevalim/nested-data-structure-traversal) que plantea un problema sencillo de programación (recorrer y "anotar" una estructura de datos anidada) e invita a enviar soluciones usando distintos lenguajes. Fue simpático ver cómo crecían las contribuciones con el correr de las horas.

El ejercicio me pareció interesante porque el problema es suficientemente fácil como para entenderlo y encontrarle una solución rápidamente y después divagar a gusto sobre las distintas formas de expresarla. En particular, me entretuve pensando cómo cambiaría mi propia solución según cuál de los lenguajes que frecuento usara en cada caso. Abajo transcribo algunas ideas que surgieron en el proceso.

Para más contexto, sugiero leer la [descripción del problema](https://github.com/josevalim/nested-data-structure-traversal#the-problem). El código del que extraje los ejemplos siguientes se puede encontrar [acá](https://github.com/facundoolano/nested-data-structure-traversal).


## Python

La solución que escribí en Python es casi idéntica al [ejemplo provisto en el repositorio](https://github.com/josevalim/nested-data-structure-traversal/blob/bce81f759dcb4c1efa113e3155520099da7cb300/python/for-in.py#L28-L42), lo que era esperable:

```python
section_position = 1
lesson_position = 1
for section in sections:
    section["position"] = section_position
    section_position += 1

    if section["reset_lesson_position"]:
        lesson_position = 1

    for lesson in section["lessons"]:
        lesson["position"] = lesson_position
        lesson_position += 1

print(sections)
```

Tendría que haber forzado las cosas para llegar a algo diferente.

Encuentro que Python minimiza la distancia entre lo que pienso y lo que termino por escribir. Supongo que se debe en parte a la expresividad del lenguaje pero también a que la forma en que aprendí a razonar cuando estaba empezando a programar se ajusta bastante al estilo imperativo que fomenta Python.

Para ser justo en las comparaciones con los otros lenguajes voy a agregar algunas restricciones: el código no puede estar suelto en el módulo sino que tiene que ser agrupado en funciones; la función que recibe la lista de secciones no puede mutarla sino que tiene que construir una nueva estructura:

```python
def traverse(sections):
    result = []
    section_position = 1
    lesson_position = 1
    for section in sections:
        section = {**section, "position": section_position}
        section_position += 1

        if section["reset_lesson_position"]:
            lesson_position = 1

        lessons = []
        for lesson in section["lessons"]:
            lesson = {**lesson, "position": lesson_position}
            lesson_position += 1
            lessons.append(lesson)

        section[lessons] = lessons
        result.append(section)

    return result
```


## Erlang

La implementación en Erlang, donde los datos son inmutables y no hay sentencias iterativas, me requiere un poco más de esfuerzo mental, aunque con los años me acostumbré a descomponer este tipo de problemas en funciones recursivas. Sé que voy a necesitar una función que procese un elemento de la lista a la vez&#x2026;

```erlang
traverse_sections([Section | Rest], % ...
```

&#x2026;que voy a tener que acumular los resultados en otra lista y llamar a la misma función con el resto de las secciones&#x2026;

```erlang
traverse_sections([Section | Rest], Output % ...
    %% ...
    traverse_sections(Rest, [SectionWithPositions | Output], %...
```

&#x2026;y que al terminar de procesar las secciones voy a tener que invertir la lista con los resultados, para preservar el orden original:

```erlang
traverse_sections([Section | Rest], Output % ...
    %% ...
    traverse_sections(Rest, [SectionWithPositions | Output], %....
traverse_sections([], Output, % ...
    lists:reverse(Output).
```

La primera versión me quedó así:

```erlang
traverse_sections([Section | Rest], Output, SectionPosition, LessonPositon) ->
    {Lessons, ActualLessonPosition} =
        case Section of
            #{lessons := Lessons, reset_lesson_position := true} -> {Lessons, 1};
            #{lessons := Lessons} -> {Lessons, LessonPositon}
        end,

    {LessonsWithPostions, NextLessonPosition} =
        traverse_lessons(Lessons, [], ActualLessonPosition),
    SectionWithPositions = Section#{position => SectionPosition,
                                    lessons => LessonsWithPostions},

    traverse_sections(Rest, [SectionWithPositions | Output], SectionPosition + 1, NextLessonPosition);
traverse_sections([], Output, _, _) ->
    lists:reverse(Output).

traverse_lessons([Lesson | Rest], Output, LessonPosition) ->
    LessonWithPosition = Lesson#{position => LessonPosition},
    traverse_lessons(Rest, [LessonWithPosition | Output], LessonPosition + 1);
traverse_lessons([], Output, LastLessonPosition) ->
    {lists:reverse(Output), LastLessonPosition}.
```

Un poco más engorroso que la versión imperativa, pero nada complicado. Prestando un poco de atención, el `case` en la primera cláusula me huele mal: en primer lugar porque está haciendo dos cosas a la vez (extraer la lista de lecciones y decidir si se debe resetear la posición), en segundo lugar porque no me gusta hacer con un `case` lo que se puede hacer con una función auxiliar con pattern-matching en sus argumentos. El resultado:

```erlang
traverse_sections([Section | Rest], Output, SectionPosition, LessonPosition) ->
    #{lessons := Lessons, reset_lesson_position := ResetPosition} = Section,

    {LessonsWithPostions, NextLessonPosition} =
        traverse_lessons(Lessons, LessonPosition, ResetPosition),
    SectionWithPositions = Section#{position => SectionPosition,
                                    lessons => LessonsWithPostions},

    traverse_sections(Rest, [SectionWithPositions | Output], SectionPosition + 1, NextLessonPosition);
traverse_sections([], Output, _, _) ->
    lists:reverse(Output).

traverse_lessons(Lessons, LessonPosition, _Reset=false) ->
    traverse_lessons(Lessons, [], LessonPosition);
traverse_lessons(Lessons, _LessonPosition, _Reset=true) ->
    traverse_lessons(Lessons, [], 1);

traverse_lessons([Lesson | Rest], Output, LessonPosition) ->
    LessonWithPosition = Lesson#{position => LessonPosition},
    traverse_lessons(Rest, [LessonWithPosition | Output], LessonPosition + 1);
traverse_lessons([], Output, LastLessonPosition) ->
    {lists:reverse(Output), LastLessonPosition}.
```

El código queda menos anidado, lo que considero un indicio de que el cambio es positivo.

La misma solución se podría reescribir usando [funciones de orden superior](https://learnyousomeerlang.com/higher-order-functions), en este caso `lists:foldl/3`, en vez de aplicar recursión "a mano".

```erlang
traverse_sections(Sections) ->
    {Output, _, _} =
        lists:foldl(
          fun (Section, {Output, SectionPosition, LessonPosition}) ->
                  #{lessons := Lessons, reset_lesson_position := ResetPosition} = Section,
                  {LessonsWithPostions, NextLessonPosition} =
                      traverse_lessons(Lessons, LessonPosition, ResetPosition),
                  SectionWithPositions = Section#{position => SectionPosition,
                                                  lessons => LessonsWithPostions},
                  {[SectionWithPositions | Output], SectionPosition + 1, NextLessonPosition}
          end, {[], 1, 1}, Sections),
    lists:reverse(Output).
```

Si bien son menos líneas de código, esta opción no me termina de convencer: el código resulta más anidado, demasiado denso. Si quisiera extraer la función anónima del `foldl` y darle su propio nombre, tampoco sería satisfactorio:

```erlang
traverse_sections(Sections) ->
    {Output, _, _} =
        lists:foldl(fun traverse_section/2, {[], 1, 1}, Sections),
    lists:reverse(Output).

traverse_section(Section, {Output, SectionPosition, LessonPosition}) ->
    #{lessons := Lessons, reset_lesson_position := ResetPosition} = Section,
    {LessonsWithPostions, NextLessonPosition} =
        traverse_lessons(Lessons, LessonPosition, ResetPosition),
    SectionWithPositions = Section#{position => SectionPosition,
                                    lessons => LessonsWithPostions},
    {[SectionWithPositions | Output], SectionPosition + 1, NextLessonPosition}.
```

Encuentro que estas funciones "reductoras" son un poco confusas cuando se las separa del llamado a `foldl`: se oscurece la justificación para empaquetar los argumentos en una tupla (`{Output, SectionPosition, LessonPosition}`) y al llamar al `foldl` me veo obligado a descartar elementos del resultado (`{Output, _, _}`). Desde ya que esto corresponde al gusto personal; ninguna de las opciones anteriores me parece rebuscada, todas podrían calificar de *idiomáticas*.


## Lo (no) idiomático

¿Qué me impide intercambiar los estilos que usé para Python y Erlang? Salvando las especificidades de cada plataforma, uno podría ensayar una versión funcional en Python usando `map`, `reduce` y `lambda`, así como una versión con estado mutable en Erlang, por ejemplo usando [counters](https://erlang.org/doc/man/counters.html)<sup><a id="fnr.1" class="footref" href="#fn.1" role="doc-backlink">1</a></sup>. Esas soluciones serían válidas pero extravagantes, el tipo de código que hace detenerse al lector y preguntar *qué es esto*. ¿Qué me impide hacerlo? La empatía, la vergüenza. El respeto por el prójimo. Los usos y costumbres. La honestidad intelectual. Lo idiomático.

Yo creo que existe el estilo en programación, entendido como las preferencias, la impronta personal del individuo para expresarse a través del código. Existe y es de las cosas que enriquecen al oficio, pero hay que usarlo con moderación. Hablando de proyectos profesionales (es decir, aquellos cuyo objetivo principal es producir software útil y no experimentar o entretenerse), suscribo a la idea de que el estilo apropiado es aquel preexistente en el código sobre el que se trabaja. Pero en ciertos casos no hay código preexistente o lo hay pero no informa el estilo de lo que vamos a escribir; o bien consideramos que el código preexistente es inadecuado y nos disponemos a reemplazarlo. En estos casos hay que apelar a lo idiomático, es decir, usar la herramienta en forma convencional, no exigir un esfuerzo innecesario a quien tenga que leer lo que vamos a escribir. Solo dentro de esos límites me parece aceptable dar lugar al estilo personal.

Es cierto que hablar de lo idiomático es meterse en terreno pantanoso. Salvo en casos puntuales, las convenciones no están escritas; refieren a un sentido común discutible, sujeto a interpretación y a cambios en el tiempo. El peligro es convencerse de que existe una única forma correcta de hacer las cosas y que, casualmente, coincide con *nuestra* forma de hacer las cosas. No queda más que ser autocrítico: ver el código con los ojos del otro, que el código sea visto por otros ojos.


## Posdata: JavaScript

¿Existe lo idiomático en JavaScript, un lenguaje que es tantos lenguajes? No voy a repetir lo que ya puse en [otro post](../2020-09-22-javascript-las-partes-nobles), pero seguramente hay ciertos consensos sobre lo que *no* se debe hacer. Lo que es decir que hay buen margen para el propio estilo o, en todo caso, para un estilo consensuado en equipo o en comunidad.

Si bien podría escribir una solución casi idéntica a la de Python<sup><a id="fnr.2" class="footref" href="#fn.2" role="doc-backlink">2</a></sup>&#x2026;

```javascript
function traverse(sections) {
  let result = [];
  let lessonPosition = 1;

  for (let i = 0; i < sections.length; i++) {
    let section = sections[i];

    if (section.reset_lesson_position) {
      lessonPosition = 1;
    }

    const lessons = [];
    for (let j = 0; j < section.lessons.length; j++) {
      let lesson = section.lessons[j];
      lesson = {...lesson, position: lessonPosition};
      lessons.push(lesson);
      lessonPosition++;
    }

    section = {...section, position: i + 1, lessons};
    result.push(section);
  }

  return result;
}
```

&#x2026;en mi corazón JavaScript siempre va a ser un lenguaje funcional (*the first lambda language to go mainstream*):

```javascript
function traverse(sections) {
  let lessonPosition = 1;
  return sections.map(function (section, i) {

    if (section.reset_lesson_position) {
      lessonPosition = 1;
    }

    const lessons = section.lessons.map(function (lesson) {
      lesson = {...lesson, position: lessonPosition};
      lessonPosition++;
      return lesson;
    });

    return {...section, lessons, position: i + 1};
  }, []);
}
```

Me tomé la licencia de mutar la variable externa `lessonPosition` y así cambiar lo que sería un `reduce` por un `map`, resultando la que probablemente sea la más sencilla de todas las implementaciones que mostré.

Claro que todo se puede llevar demasiado lejos. Durante un tiempo tuve cierta fascinación con la biblioteca [Ramda.js](https://ramdajs.com/) y produje código que puede gustar o no, pero ciertamente no es idiomático. El mejor ejemplo es el [paquete App Store Optimization](https://github.com/facundoolano/aso/blob/master/lib/visibility.js): lo expresé casi completamente en términos de transformaciones de datos con funciones de Ramda y el resultado, para bien o para mal, fue que todo el mundo se abstuvo para siempre de mandar un Pull-Request a ese proyecto.


## Posdata: Ejercicios de estilo

Hay un libro que sigue una premisa parecida al repositorio de José Valim. Se llama [Exercises in programming style](https://www.routledge.com/Exercises-in-Programming-Style/Lopes/p/book/9780367350208), inspirado por el [libro de ejercicios de estilo](https://en.wikipedia.org/wiki/Exercises_in_Style) de Raymond Queneau. Ahí se usa Python no en forma idiomática sino como *lingua franca* para resolver un mismo problema de muchas maneras posibles y en el proceso hacer un repaso de la historia de la programación.

> In the universe of all things a good programmer must know, I see collections of programming styles as being as important as any collection of data structures and algorithms, but with a focus on human effects rather than on computing effects. Programs convey information not just to the computers but, more importantly, to the people who read them. As with any form of expression, the consequences of **what** is being said are shaped and influenced by **how** they are being said. An advanced programmer needs not be able to just write correct programs that perform well; he/she needs to be able to choose appropriate styles for expressing those programs for a variety of purposes.

Los ejercicios se pueden ver [en este repositorio](https://github.com/crista/exercises-in-programming-style).

<section class="footnotes" markdown=1>
## Notas

<sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> En esta línea, por ejemplo, hay soluciones en Elixir [usando tablas ETS](https://github.com/josevalim/nested-data-structure-traversal/blob/bce81f759dcb4c1efa113e3155520099da7cb300/elixir/ets_for.exs) y en Clojure [usando atoms](https://github.com/josevalim/nested-data-structure-traversal/blob/bce81f759dcb4c1efa113e3155520099da7cb300/clojure/atom.clj).

<sup><a id="fn.2" class="footnum" href="#fnr.2">2</a></sup> En el repositorio de Valim hay una [solución imperativa](https://github.com/josevalim/nested-data-structure-traversal/blob/bce81f759dcb4c1efa113e3155520099da7cb300/javascript/for_of.js) bastante más limpia usando `for ... of`.

</section>