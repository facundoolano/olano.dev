.PHONY: book

venv=. venv/bin/activate &&

venv:
	python -m venv venv
	$(venv) pip install pyyaml feedparser ipython requests

serve:
	jorge serve

build: reads
	jorge build

push: build
	rsync -vPrz --delete target/ root@olano.dev:/var/www/olano.dev

# builds and uploads the latest version of the resume by first pushing the site
resume: push
	wkhtmltopdf --print-media-type https://olano.dev/resume src/resume.pdf
	make push

book:
	cd book && make && mv book.pdf book.epub ../src/

reads: venv
	$(venv) ./scripts/reads.py
