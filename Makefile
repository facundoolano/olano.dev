serve:
	jorge serve

build:
	jorge build

push: build
	rsync -vPrz --delete target/ root@olano.dev:/var/www/olano.dev

# builds and uploads the latest version of the resume by first pushing the site
resume: push
	wkhtmltopdf --print-media-type https://olano.dev/resume src/resume.pdf
	make push
