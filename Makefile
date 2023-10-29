serve:
	bundle exec jekyll serve -l

build:
	bundle exec jekyll build

push: build
	rsync -vPrz _site/ root@olano.dev:/var/www/olano.dev
