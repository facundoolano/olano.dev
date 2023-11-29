serve:
	bundle exec jekyll serve -l --drafts

build:
	bundle exec jekyll build

push: build
	rsync -vPrz _site/ root@olano.dev:/var/www/olano.dev
