---
layout: post
title: "La magia de los namespaces"
excerpt: la concisión de los nombres en un módulo funciona como un indicador de la cohesión de ese módulo.
date: 2020-08-31 11:29:56
tags: [software, programación]
---

Mi primer contacto con la idea de `namespace` fue programando C++ en la Facultad. En ese momento, para mí un namespace era pura sintaxis, algo que usabas para evitar conflictos de nombres entre tu código y el de terceros, apenas otro arma en la interminable batalla contra el compilador.

Un par de años después, cuando estaba aprendiendo Python y leí [el Zen](https://www.python.org/dev/peps/pep-0020/), me encontré con:

> Namespaces are one honking great idea &#x2013; let's do more of those!

Supongo que esto me debe haber confundido un poco. El resto de las reglas del Zen tenían consecuencias prácticas muy evidentes, pero esta hablaba de algo que, a diferencia de lo que pasaba en C++, no formaba parte de la sintaxis lenguaje. En Python me resultaba más natural razonar en términos de funciones y clases, así que me olvidé de los namespaces.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

Fue recién con Clojure que la idea de namespaces se volvió una herramienta de diseño para mis programas. En Clojure hay muchas (tal vez demasiadas) formas de manipular un namespace e importar cosas desde otros módulos: `ns`, `require`, `refer`, `use`, `alias`, `import`&#x2026;

Un [post de Nikita Prokopov](https://tonsky.me/blog/readable-clojure/) me ayudó no solo a ser consistente con mis requires, sino a empezar a prestar atención a cómo estas declaraciones afectan a la legibilidad de mis módulos, algo que tiene utilidad mucho más allá de Clojure. En particular, si uno reemplaza<sup><a id="fnr.1" class="footref" href="#fn.1" role="doc-backlink">1</a></sup>:

```python
from advenjure.game import make_game, run_game
from advenjure.rooms import make_room, add_item
from advenjure.items import make_item

magazine = make_item("sports magazine",
                     "The cover read 'Sports Almanac 1950-2000'")

bedroom = make_room("Bedroom", "A smelling bedroom.")
bedroom.add_item(magazine)

```

Por su alternativa:

```python
import advenjure.game as game
import advenjure.rooms as rooms
import advenjure.items as items

magazine = items.make_item("sports magazine",
                           "The cover read 'Sports Almanac 1950-2000'")

bedroom = rooms.make_room("Bedroom", "A smelling bedroom.")
bedroom.add_item(magazine)
```

El código se vuelve más legible: se hace evidente si un símbolo es local o se lo está trayendo de otro módulo (y cuál es ese módulo). Y, citando a Nikita, grep vuelve a funcionar.

Se puede hacer una objeción al ejemplo anterior, sin embargo: la expresión `rooms.make_room`, más allá de ser un poco larga, parece redundante. Y acá es donde empieza la magia: si aceptamos que siempre vamos a referirnos a símbolos externos calificándolos con su namespace, podemos renombrar `rooms.make_room` a `rooms.make`. Yendo un poco más lejos, probablemente sea evidente por contexto que `rooms.add_item` recibe un item por parámetro, entonces:

```python
magazine = items.make("sports magazine",
                      "The cover read 'Sports Almanac 1950-2000'")

bedroom = rooms.make("Bedroom", "A smelling bedroom.")
bedroom.add(magazine)
```

Lo interesante de trabajar de esta manera es que ciertos [code smells](https://wiki.c2.com/?CodeSmell) empiezan a tener un correlato visual:

-   Si el módulo `game` define funciones `make_room` y `make_item`, resultaría ambiguo renombrar `game.make_game` a `game.make`. Posiblemente esto sea un indicio de que el módulo game no es cohesivo.
-   Si la entidad `game` se manipula con funciones del estilo `game.add_room`, `game.add_item` y `game.add_character`, posiblemente tenga demasiadas responsabilidades y sea útil introducir nuevas entidades.
-   Si mi módulo `room` está plagado de funciones con el prefijo `item.`, posiblemente padezca de [feature envy](https://wiki.c2.com/?FeatureEnvySmell).

En otras palabras: la concisión de los nombres en un módulo funciona como un indicador de la cohesión de ese módulo. Zachary Tellman desarrolla esta idea con mucha claridad en el primer capítulo de [Elements of Clojure](https://elementsofclojure.com/)<sup><a id="fnr.2" class="footref" href="#fn.2" role="doc-backlink">2</a></sup>:

> In theory, a namespace can hold an unlimited number of functions, as long as none of them share the same name. In practice, namespaces should hold functions which share a common purpose, so that **the namespace lends narrowness to the names inside it**. Typically, this means that all the functions should operate on a common datatype, a common data scope, or both.

Claro que, como siempre en el software, hay que saber encontrar el balance:

> A large number of namespaces is taxing for our readers (&#x2026;). As such, we should add new namespaces only when necessary. By questioning the need for new namespaces, we implicitly question the need for new datatypes and data scopes, which will lead to simpler code overall.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

Una de las cosas que me simpatiza de Erlang es que la propia sintaxis fomenta el método descripto arriba: la única manera de llamar una función externa es calificándola con el módulo donde está definida: `rooms:make/2`, `rooms:add/3`, `items:make/2`, etc. Como consecuencia, no hace falta "importar" las funciones que se van a usar en un módulo, sino que se declaran las funciones (y, opcionalmente, los tipos) que se van a *exportar* desde ese módulo:

```erlang
-module(rooms).

-export([make/2, add/3]).

make(Name, Description) ->
  #{name => Name,
    description => Description,
    items => []}.

add(Room, Item, ItemRoomDescription) ->
  NewItems = [{Item, ItemRoomDescription} | maps:get(items, Room)],
  maps:update(items, NewItems, Room).
```

Todas las funciones que no están declaradas en la lista del `export`, son internas del módulo, invisibles desde el exterior. Lo interesante de esta inversión de las declaraciones, más que el "ocultamiento de la información" (sobre el que no soy demasiado religioso), es que favorece la legibilidad: uno abre el archivo del módulo y, si tiene suerte, se encuentra con documentación y definiciones de tipos, pero aunque no tenga suerte puede ver la lista de exports para darse una idea de qué cosas se pueden hacer con ese módulo &mdash;cuál es su interfaz&mdash; y qué debería esperar encontrarse si decide seguir leyendo.

## Footnotes

<sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> Estos ejemplos fueron originalmente concebidos en Clojure, pero me pareció más amigable usar Python para fines ilustrativos.

<sup><a id="fn.2" class="footnum" href="#fnr.2">2</a></sup> En ese primer capítulo (que [se puede leer online](https://leanpub.com/elementsofclojure/read_sample)) se da el mejor tratamiento que conozco a la cuestión de poner nombres en software, y debería ser útil para cualquier programador, independientemente del lenguaje y el paradigma que use.