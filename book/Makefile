all: book.epub

target: src/* layouts/*
	jorge build

# based on https://github.com/javierarce/epub-boilerplate/blob/master/publish
book.epub: target
	rm -f $@
	cd target && zip -q0X ../$@ mimetype
	cd target && zip -qXr9D ../$@ * -x "*.svn*" -x "*~" -x "*.hg*" -x "*.swp" -x "*.DS_Store"
