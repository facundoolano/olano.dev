---
layout: post
title: "Blogging con Emacs y org-mode"
date: 2020-09-04
tags: [blog, emacs]
css: "highlight"
---

Si el *Hola Mundo!* de la programación web es armar un blog, el *Hola Mundo!* de los posts es aquel que describe cómo se implementó ese blog. En este caso no hay mucho para decir sobre la implementación —todo el trabajo pesado lo hacen Jekyll y Github Pages—, pero sí tuve que invertir algo de tiempo preparando mi editor para el proceso de escritura y publicación.

Una de las razones por las que armé un nuevo blog es que trabajar con WordPress me daba escalofríos. Quería control de versiones para mis posts, tenerlos en GitHub en algún formato independiente de la plataforma, y, lo más importante, poder escribir en Emacs, el mismo editor que uso cotidianamente para programar. En particular, me interesaba usar [org-mode](https://orgmode.org/) como lenguaje de markup. El objetivo es alcanzar un ciclo virtuoso (?) en el que escribo más seguido, aprendo más sobre org-mode y mejoro mi configuración de Emacs en el camino.


## Setup

Ya decidido a usar Emacs y org-mode, me pareció razonable buscar cómo integrarlos con Jekyll y Github Pages, para ahorrarme el trabajo y el costo de hosting y configuración del blog. Encontré [este post](https://carl.ac/blogging-with-emacs-org-github-pages/), que sigue un razonamiento muy parecido al mío, y lo usé como guía. Adicionalmente, la documentación de org-mode tiene [un tutorial](https://orgmode.org/worg/org-tutorials/org-jekyll.html) dedicado específicamente a este escenario.

Siguiendo el ejemplo de aquel post, hice un fork de [BeautifulJekyll](https://beautifuljekyll.com/), un template pensado para GitHub Pages que resuelve la mayoría de las necesidades básicas de un blog (layout, links, comentarios, analytics, etc.).

Para poder producir posts, necesitaba generar HTML que sea "Jekyll-friendly"<sup><a id="fnr.1" class="footref" href="#fn.1" role="doc-backlink">1</a></sup>. org-mode incluye [funcionalidad de exportación](https://orgmode.org/org.html#Exporting) (convertir documentos org a otros formatos como LaTeX, markdown y html) y [publishing](https://orgmode.org/worg/org-tutorials/org-publish-html-tutorial.html) (exportar jerarquías de documentos relacionados o "proyectos"). Lo único que hace falta en este caso es declarar un proyecto que indique de dónde se leen los archivos .org y en dónde hay que guardar los .html exportados:

```emacs-lisp
(setq org-publish-project-alist
      '(("blog"
         ;; Path to org files.
         :base-directory "~/dev/facundoolano/facundoolano.github.io/org"
         :base-extension "org"

         ;; Path to Jekyll Posts
         :publishing-directory "~/dev/facundoolano/facundoolano.github.io"
         :recursive t
         :publishing-function org-html-publish-to-html
         :headline-levels 4
         :html-extension "html"
         :body-only t)))
```

Si bien teóricamente uno no necesita nada más que pushear cambios al repositorio para publicar en GitHub Pages, resulta más práctico tener Jekyll instalado localmente para previsualizar los posts antes de publicarlos. Instalé todo lo necesario así:

```sh
$ asdf install ruby 2.7.1
$ asdf local ruby 2.7.1
$ gem install bundler jekyll
$ bundle install
```


## Workflow

Para convertir un archivo de markdown, o en mi caso, de org-mode, en un post de Jekyll, hacen falta dos cosas: 1. prefijar el nombre del archivo con un timestamp (e.g. `2020-09-02-blogging-con-emacs-y-org-mode`) y 2. agregarle un encabezado con metadata:

```yaml
---
layout: post
title: "Blogging con Emacs y org-mode"
date: 2020-09-04
tags: [blog, emacs]
---
```

Para automatizar esta tarea frecuente, escribí este comando (partiendo de lo que encontré [acá](https://www.dougwoos.com/2013/12/24/posting-to-jekyll-with-emacs.html)):

```emacs-lisp
(defun org-blog-new-post (title)
  "Create a new org-file for a blog post as expected by Jekyll with TITLE."
  (interactive "MPost title: ")
  (let ((slug (sluggify title))
        (date (current-time)))
    (find-file (concat (projectile-project-root) "org/_posts/"
                       (format-time-string "%Y-%m-%d") "-" slug
                       ".org"))
    (insert "#+BEGIN_EXPORT html\n")
    (insert "---\n")
    (insert "layout: post\n")
    (insert "title: \"") (insert title) (insert "\"\n")
    (insert "date: ") (insert (format-time-string "%Y-%m-%d %H:%M:%S")) (insert "\n")
    (insert "tags: []\n")
    (insert "---\n")
    (insert "#+END_EXPORT\n\n")))
```

También agregué un comando para actualizar la fecha del post en el nombre y el encabezado del archivo (más para practicar emacs-lisp que por necesidad, si vamos a ser honestos):

```emacs-lisp
(defun org-blog-reset-date ()
  "Prompt for a new blog post date and set it in the filename and the Jekyll \
header."
  (interactive)
  (if (not (s-contains? "org/_posts/" (pwd)))
      (error "Not visiting a blog buffer")
    (let* ((date (read-from-minibuffer "Post date: " (format-time-string "%Y-%m-%d")))
           (filename (buffer-name))
           (new-name (concat date (substring filename 10))))
      (rename-file filename new-name t)
      (set-visited-file-name new-name t t)
      (save-excursion
        (goto-char (point-min))
        (re-search-forward "^date: .*$" nil t)
        (replace-match (concat "date: " date))))))
```

Para exportar el html uso `org-publish-current-project` y para ver el post localmente corro `bundle exec jekyll serve`.

-   [Así](https://raw.githubusercontent.com/facundoolano/facundoolano.github.io/master/org/_posts/2020-08-31-la-magia-de-los-namespaces.org) se ve el archivo .org de un post.
-   [Así](https://github.com/facundoolano/facundoolano.github.io/blob/master/_posts/2020-08-31-la-magia-de-los-namespaces.html) queda el HTML exportado.
-   [Esta](https://github.com/facundoolano/emacs.d/blob/master/modules/facundo-blog.el) es la sección relevante de mi configuración de Emacs.

<br>

<section class="footnotes" markdown=1>
## Notas

<sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> Alternativamente podría exportar de org a markdown, formato que Jekyll también soporta, pero es algo que todavía no probé.

</section>