serve:
	bundle exec jekyll serve -l --drafts

build:
	bundle exec jekyll build

push: build
	rsync -vPrz _site/ root@olano.dev:/var/www/olano.dev

# builds and uploads the latest version of the resume by first pushing the site
resume: push
	wkhtmltopdf https://olano.dev/work/ work/resume.pdf
	make push
