push:
	scp index.html root@olano.dev:/var/www/mystery/index.html

serve:
	bundle exec jekyll serve -l

build:
	bundle exec jekyll build
