serve:
	bundle exec jekyll serve -l --drafts --future

build:
	JEKYLL_ENV=production bundle exec jekyll build --incremental

push: build
	rsync -vPrz _site/ root@olano.dev:/var/www/olano.dev

# builds and uploads the latest version of the resume by first pushing the site
resume: push
	wkhtmltopdf https://olano.dev/resume resume.pdf
	make push
