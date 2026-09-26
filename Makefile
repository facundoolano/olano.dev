.PHONY: book

venv=. venv/bin/activate &&

venv:
	python -m venv venv
	$(venv) pip install pyyaml feedparser ipython requests

serve: tags
	jorge serve

build: tags
	jorge build

.PHONY: tags
tags:
	@rm -rf src/blog/tags/*.html
	@for tag in $$(jorge meta 'site.tags|keys|join:" "' | tr -d '"'); do \
		{ echo "---"; \
		  echo "layout: tags"; \
		  echo "tag: $$tag"; \
		  echo "---"; \
		} > "src/blog/tags/$$tag.html"; \
		echo "src/blog/tags/$$tag.html"; \
	done

push: build
	rsync -vPrz --delete target/ root@olano.dev:/var/www/olano.dev

# builds and uploads the latest version of the resume by first pushing the site
resume: push
	wkhtmltopdf --print-media-type --load-error-handling ignore https://olano.dev/resume src/resume.pdf
	make push

book:
	cd book && make && mv book.pdf book.epub ../src/

reads: venv
	$(venv) ./scripts/reads.py
