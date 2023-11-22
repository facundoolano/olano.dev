---
layout: post
title: "Miscelánea sobre web y redes sociales"
date: 2023-08-30
tags: [software, utopías]
share-img: assets/img/mastodon.jpeg
image: assets/img/mastodon.jpeg
thumbnail-img: assets/img/mastodon.jpeg
excerpt: La proliferación de aplicaciones federadas con ActivityPub, el renovado interés en los lectores RSS y los esfuerzos de la web indie son miniaturas de un proyecto de desmantelar las plataformas monopólicas mediante el uso de tecnología abierta.
---

<p class="verse">
Quien no extraña la vieja web no tiene corazón,<br />
quien la quiere de vuelta no tiene cerebro.<br />
<br />
Vladimir Putin<br />
</p>


## 1: Enmierdización

> Here is how platforms die: first, they are good to their users; then they abuse their users to make things better for their business customers; finally, they abuse those business customers to claw back all the value for themselves. Then, they die.

Alguna vez dije que la solución a la crisis de la balanza de pagos era empezar a exportar memes. (Eso y monetizar a los argentinos notables; digamos: cobrarle retenciones a Messi, derechos formativos a Bergoglio). Porque da gusto ver cómo inventan los argentinos, mártires cínicos,  perfectos violinistas para cualquier Titanic. Cuando Elon Musk compró Twitter, recé para que no lo rompiera antes del Mundial: Qatar puede no haber sido el [fin del fútbol](../2023-02-06-justicia-poetica/), pero sí que fue el *last dance* de Tuiter Argentina.

Cory Doctorow acuñó el termino *enshittification* para designar el ciclo en que las redes sociales pasan de la masividad a una degradación que en algunos casos llega a ser terminal. El artículo, de enero, venía a cuento de algunos cambios en TikTok pero tuvo el timing perfecto para anticiparse al declive de Twitter &#x2014;que había empezado antes pero se acentuó semanas después&#x2014; y al de Reddit que, en medio del [hype por la inteligencia artificial](../2023-07-10-la-era-de-la-boludez), cerró el acceso a las APIs para aplicaciones externas, reservándose el derecho exclusivo de explotar a su comunidad como carne de algoritmo. El término parece haberse puesto de moda para referir al malestar generalizado que produce la web moderna.


### Fuentes

-   [Tiktok's enshittification](https://pluralistic.net/2023/01/21/potemkin-ai/#hey-guys).


## 2: La Fede

Twitter se enmierdizó y fue mi excusa para desmantelar mi cuenta y probar [Mastodon](https://joinmastodon.org/). Anoto algunas cosas que me llamaron la atención después de unas semanas en el *fediverso*.

El ritmo es más lento: la gente se loguea con menos frecuencia, postea esporádicamente, los posts tardan más en propagarse, las reacciones llegan con delay. Se siente un poco como los foros de antes: en vez de recibir un torrente de novedades, voy cada tanto a buscarlas, a ver qué hay de nuevo.

El mayor control sobre el feed cambia profundamente la experiencia de usuario. No sólo porque los posts llegan cronológicamente, sin mediación de "algoritmos" tratando de manipular mi atención o venderme cosas, sino porque Mastodon te da muchas opciones para elegir qué incluir en el timeline: ocultar replies o retweets, desactivar las actualizaciones en vivo, seguir hashtags, silenciar cuentas, crear filtros.

Hay que decir que el Mastodon *realmente existente* es menos descentralizado de lo que permite su tecnología, no resuelve del todo los problemas de las redes masivas. La mayoría de los usuarios se concentra en dos o tres servidores; el proceso de migración es engorroso y los posts son intransferibles; los usuarios, en última instancia, tienen que confiar en algún administrador o asumir el trabajo de convertirse en uno. Y están a merced de perder los datos si la instancia se cae o a quedar aislados si es bloqueada por otras. Pero mientras que las aplicaciones *peer to peer* son un ideal de difícil realización, la federación a través del protocolo ActivityPub es un
[*Worse is Better*](../2023-02-22-worse-is-better-is-worse-is-better) de las redes sociales: la alternativa que estuvo en mejores condiciones de asilar a las sucesivas olas de refugiados de Twitter.

Elegir un server de Mastodon se parece a elegir una distribución de Linux. Y aunque la federación en la práctica tenga sus problemas, hay todo un triunfo en este despliegue global de una red de aplicaciones interoperables. Así como los programas de Linux funcionan sin grandes cambios entre distribuciones e incluso en otras variantes de Unix, así los usuarios del fediverso pueden hablar entre sí sin importar si su cuenta reside en una aplicación de [microblogging](https://micro.blog/), de [fotos](https://pixelfed.org), de [videos](https://joinpeertube.org), de [libros](https://joinbookwyrm.com/), de [links](https://join-lemmy.org/). Eso ya implica un cambio de paradigma, una demostración de alternativas y futuros posibles.


### Fuentes

-   [Can ActivityPub save the internet?](https://www.theverge.com/2023/4/20/23689570/activitypub-protocol-standard-social-network)
-   [Decentralized Social Networks](https://medium.com/decentralized-web/decentralized-social-networks-e5a7a2603f53).
-   [The Federation Fallacy](https://rosenzweig.io/blog/the-federation-fallacy.html).
-   [Mastodon is easy and fun except when it isn’t](https://erinkissane.com/mastodon-is-easy-and-fun-except-when-it-isnt).
-   [Notes from a Mastodon migration](https://erinkissane.com/notes-from-a-mastodon-migration).


## 3: Otras webs

> Do we want the web to be open, accessible, empowering and collaborative? Free, in the spirit of  the open source tools it's built on? Or do we want it to be just another means of endless consumption, where people become eyeballs, targets and profiles? Where companies use your data to control your behaviour and which enables a surveillance society—what do we want?

En Mastodon y en el fediverso sobran programadores frustrados con las redes sociales, con el estado de la web y la industria del software en general. (Me cuento entre ellos). No es una sorpresa considerando: a) el perfil de usuario que opta por un nicho descentralizado, y b) la complejidad técnica de elegir una instancia y encontrar contenido.

Sí llama la atención cómo muchos canalizan esa frustración en una especie de retorno a las fuentes, estudiando los hábitos y tecnologías de la vieja web, los *Bulletin Board Systems*, los feeds RSS. Aunque no estén exentas de cierta nostalgia y romantización del pasado, estas exploraciones intentan encontrar en viejas ideas formas de resistir o superar una crisis que ya es difícil de disimular y que amenaza con profundizarse.

Hay que hacer mucho trabajo para recobrar algo de aquella sensación de exploración y descubrimiento que generaba "navegar" en internet. La web se convirtió hace años en un corralito que se va cerrando alrededor nuestro, un cerco de paywalls y ads y popups de consentimiento, de solicitudes de registro y de suscripciones. La vieja web supo ser una vía de escape del mundo real, un espacio motorizado más por la curiosidad y la creatividad que por el consumo; la web moderna es aquello de lo que necesitamos refugiarnos.

Como en cualquier conjunto de anticapitalistas, pareciera que en el fediverso cada uno se dispone, a su manera, a cambiar el mundo: administrando una instancia de Mastodon o desarrollando una nueva app federada o un protocolo, o simplemente escribiendo un manifiesto para reinventar la web. Los hay revisando el rol que jugaron los blogs en reemplazar a los sitios personales por cronologías de contenidos; los hay buscando en las wikis y las metáforas botánicas una alternativa a los ríos de la información; los hay liderando comunidades devenidas movimientos contraculturales. De todas esas derivas, la que más me interesó fue la de la [*web indie*](https://indieweb.org).

El objetivo de la web indie es devolverle a los usuarios el control de su identidad online, de sus datos y de su experiencia de la web. En un mundo ideal, cada persona tendría un dominio propio, que funcionaría como identificación: en vez de perfiles separados en las corporaciones (`twitter.com/@olano`, `github.com/olano`, `olano@gmail.com`, etc), tendría un perfil unificado en su sitio web (por ejemplo: `olano.com`). Esto no implica eliminar la participación en las redes corporativas sino convertirlas en medios subsidiarios: el contenido se publica primero en el sitio personal y se reproduce (y linkea) en los demás.

Los promotores de la web indie ofrecen tecnologías y protocolos para mantener la funcionalidad de las redes sociales, sin ceder el control de los datos: seguir a otras personas, comentar, compartir e interactuar con su contenido sin necesidad de participar de una misma plataforma. Son herramientas complicadas de ensamblar hasta para un usuario técnico, menos un ejemplo a seguir que una prueba de concepto: una demostración de que las alternativas son posibles. La visión es ponerlas al alcance de cualquier usuario.


### Fuentes

-   [Against an Increasingly User-Hostile web](https://neustadt.fr/essays/against-a-user-hostile-web/).
-   [A Case Against Today's Internet](https://sadgrl.online/cyberspace/modern-web).
-   [The Old web](https://devon.lol/blog/the-old-web/).
-   [How the Blog Broke the web](https://stackingthebricks.com/how-blogs-broke-the-web/).
-   [The Garden and the Stream: A Technopastoral](https://hapgood.us/2015/10/17/the-garden-and-the-stream-a-technopastoral/).
-   [Welcome to the indie web Movement](https://slate.com/technology/2014/04/indiewebcamps-create-tools-for-a-new-internet.html).
-   [The indieweb Movement: Owning Your Data and Being the Change You Want to See in the web](https://www.jvt.me/posts/2019/10/20/indieweb-talk/).


## 4: RSS as in reinassance

> What if you could reply to a blog post in your feed reader, and your reply would show up as a comment on the original post automatically? What if you could click a “heart” in your reader, and the author of the post would see it? What if you had one place to go to follow not just your Twitter friends, but also all of your friends’ blogs, their microblogs, and see the pictures they’re sharing? What if you could have seamless conversations in your reader the way you have seamless conversations on Twitter today?

Aunque Mastodon no sea una corporación chupasangre ni esté gestionado por un supervillano de Silicon Valley, en el fondo sigue siendo un clon de Twitter que trafica en seguidores, likes y notificaciones. Y aunque encontré ahí personas e ideas valiosas y aprendí algunas cosas sobre mis consumos de información, me siguen incomodando el frenesí del microblogging, el drama y el flujo constante de trivialidades que estimula. Prefiero la cadencia más reflexiva de los blogs.

Me di cuenta de que estaba siguiendo a personas solo para enterarme cuándo publicaban en sus sitios y a bots para ahorrame entrar a lobste.rs o hackernews a buscar noticias tecnológicas. Es decir que usaba Mastodon, y antes Twitter, menos como una red social que como un condensador de información. Y la verdad es que ninguno de los dos es la herramienta que mejor se adecúa a esa función. Para eso están los lectores [RSS](https://aboutfeeds.com/).

Los feeds RSS nunca desaparecieron, pese al mito urbano de que el cierre de Google Reader los mató. De hecho llama la atención la cantidad de diarios, revistas y blogs que todavía ofrecen su contenido por ese medio, acaso sin saberlo. Si obviamos el aspecto "social" de los medios digitales, es muy fácil recuperar el control de nuestra vida online usando herramientas como Feedly, Inoreader, FreshRSS o Tiny Tiny RSS. Antes de que Elon se ponga la gorra, esos servicios ofrecían incluso integración con Twitter, para eludir completamente la lógica tóxica del feed "curado" de la red social. (Mastodon no solo tiene una API pública sino que las actualizaciones de cada usuario y cada hashtag están expuestos como un feed RSS).

Terminé de convencerme de que los feeds eran una opción viable para mi cuando leí sobre los *indie web readers*. Los lectores indie son como la evolución de RSS: una mezcla entre Google Reader y feed de Twitter, una red social para armar. Además de unificar el punto de consumo de las distintas fuentes de la web, permiten interactuar con el contenido (darle like, comentar, retweetear) sin salir de la aplicación. Los protocolos de la web indie, además, separan el problema de integrar las fuentes de información del diseño de la aplicación de lectura.

Aunque el concepto es interesante, la implementación de un lector indie es demasiado complicada para el tipo de uso que yo hago de la web. No me molesta abrir un tab en el navegador cuando ocasionalmente quiero dejar un comentario en Mastodon o en lobste.rs. Pero la idea menos ambiciosa de diseñar un lector ergonómico, arbitrariamente configurable, aprovechando la ubicuidad de RSS, me parece un proyecto ideal para reconciliarme con lo bueno y lo bello de la web.


### Fuentes

-   [Who killed Google Reader?](https://www.theverge.com/23778253/google-reader-death-2013-rss-social)
-   [Why I Still Use RSS](https://atthis.link/blog/2021/rss.html).
-   [An IndieWeb reader: My new home on the internet](https://aaronparecki.com/2018/04/20/46/indieweb-reader-my-new-home-on-the-internet).


## 5: Protocolos sí, plataformas no

> Moving us back toward a world where protocols are dominant over platforms could be of tremendous benefit to free speech and innovation online. Such a move has the potential to return us to the early promise of the web: to create a place where like-minded people can connect on various topics around the globe and anyone can discover useful information on a variety of different subjects without it being polluted by abuse and disinformation.

La proliferación de aplicaciones federadas con ActivityPub, el renovado interés en los lectores RSS y los esfuerzos de la web indie son miniaturas de un proyecto de desmantelar las plataformas monopólicas mediante el uso de tecnología abierta, un proyecto que Mike Masnick expresó muy bien en su artículo de 2019.

La vieja web funcionaba alrededor de un conjunto de protocolos abiertos: TCP/IP para la comunicación, HTTP para la web, IMAP, POP3 y SMTP para los mails, IRC y XMPP para el chat.
Esos protocolos funcionaban bien para los usuarios pero no ofrecían muchas oportunidades de explotación económica. La solución de la web 2.0 fue la que Cory Doctorow describe en su ciclo de enmierdización: crear plataformas cerradas alrededor de los protocolos (Facebook, Twitter, Whatsapp), tentar a los usuarios con mejor funcionalidad que las versiones abiertas y, una vez que los tenían "rehenes", aprovechar económicamente el monopolio (usualmente acumulando datos para vender ads).

El texto de Masnick se enfoca en el problema de la libertad de expresión en la web actual. Según el autor, las plataformas crecieron tanto en tamaño e influencia que pasaron a tener ciertas "responsabilidades civiles" que no están en condiciones de cumplir: se espera que prevengan los discursos de odio y la desinformación pero que no caigan en la censura y la vigilancia, todo mientras satisfacen a los accionistas que financiaron aquel crecimiento. El resultado es que el costo de moderación de contenido es cada vez más alto, la vigilancia y la explotación de los usuarios es cada vez más agresiva y nadie está contento. Masnick propone una solución técnica: volver a un mundo protocolos, como el de la vieja web:

> While there would be specific protocols for the various types of platforms we see today, there would then be many competing interface implementations of that protocol. The lowered switching costs of moving from one implementation to another would create less lock-in, and the ability for anyone to create their own interface and get access to all of the content and users on the underlying protocol makes the barriers to entry for competition drastically lower. You don’t need to build an entirely new Facebook if you already have access to everyone making use of the “social network protocol” and just provide a different, or better, interface to it.

En ese mundo, en vez de redes aisladas como Facebook, Reddit y Twitter, existiría un "protocolo de red social" (que me imagino parecido al ActivityPub del fediverso) y muchas implementaciones de interfaces compitiendo entre sí. Podría haber interfaces que garanticen determinadas formas de control de contenido o determinada experiencia de usuario, por ejemplo diseñadas para contenido audiovisual o para lectura de noticias o para chatear. Los usuarios podrían elegir, cambiar y combinar interfaces sin perder a sus contactos y los implementadores de interfaces, que ocuparían el lugar actual de las plataformas, tendrían incentivos para ofrecer un mejor producto:

> End users would still be able to make use of their own data for various social media tools, but rather than having that data locked up in opaque silos with no access, no transparency, and no control, the control would be moved entirely to the end users. The intermediaries are incentivized to be on their best behavior to avoid being cut off.

Esta idea de "invertir el control" y devolverle sus datos a los usuarios tiene mucho en común con los principios del *local-first software*, un proyecto liderado por Martin Kleppmann que propone alcanzar un balance entre la conveniencia de las plataformas en la nube, y la eficiencia y longevidad de los programas tradicionales "offline".

En los últimos 15 años, con el mayor acceso a internet y la proliferación de las computadoras móviles, nos fuimos acostumbrando a que el software pase del escritorio al navegador y del navegador a la app móvil, a que los datos pasen de nuestro disco rígido a la nube, a que el software que antes comprábamos (o no) sea ahora un servicio al que nos tenemos que suscribir. Y lo que pagamos en esa transacción (entregando plata o privacidad) es conveniencia: no tener que bajar o instalar programas, poder usar nuestra cuenta de Google para todo, no preocuparnos por hacer backups o compartir archivos entre personas o sincronizar nuestros varios dispositivos. Pero, quizás sin darnos cuenta, perdimos en esa transición muchas cosas que dábamos por sentadas: ahora cualquier acción tarda más porque tiene que pasar por el servidor, perdemos el acceso al software y los datos cuando no tenemos internet, vivimos expuestos a que el servicio se caiga o que cambien los precios o los términos de uso. O que la empresa se funda porque Amazon copió su servicio, o que la compre Google y decida que al cabo que ni quería mantener ese producto.

La propuesta del local-first es tener lo mejor de los dos mundos: que el usuario sea dueño y tenga acceso para siempre al software y a los datos, y que el servidor ejerza apenas un rol de soporte, de intercambio y sincronización de datos. Aunque el foco esté puesto en la experiencia de usuario y la colaboración en tiempo real, buena parte de la tecnología necesaria para ejecutar el proyecto local-first contribuye al plan de reemplazar las plataformas con protocolos. En ambos casos el control está en los márgenes de la red, en manos de los usuarios, y la nube provee un servicio que no puede trastocarse en monopolio.

<div class="org-center">
<p>
&lowast; &lowast; &lowast;
</p>
</div>

En vista de las continuas burradas de Elon Musk, del creciente desencanto con las plataformas &#x2014;esa enmierdización que ya salpica hasta a los usuarios menos sofisticados&#x2014;, de la viabilidad del fediverso y el supuesto interés de Tumblr y Facebook de integrarse a ActivityPub, es tentador suspender la incredulidad y pensar que ese mundo de protocolos en vez de plataformas está un poco más cerca que algunos años atrás. Que todavía queda espacio para construir una web más humana.


### Fuentes

-   [Protocols, Not Platforms: A Technological Approach to Free Speech](https://knightcolumbia.org/content/protocols-not-platforms-a-technological-approach-to-free-speech).
-   [The endpoint of Web Environment Integrity is a closed Web](https://educatedguesswork.org/posts/wei/).
-   [Local-first software: You own your data, in spite of the cloud](https://www.inkandswitch.com/local-first/).
-   [The Cloud Is a Prison. Can the Local-First Software Movement Set Us Free?](https://www.wired.com/story/the-cloud-is-a-prison-can-the-local-first-software-movement-set-us-free/)
-   [Our Incredible Journey](https://www.gyford.com/phil/writing/2013/02/27/our-incredible-journey/).

