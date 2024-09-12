all: book.epub

target: src/* layouts/*
	jorge build

# based on https://github.com/javierarce/epub-boilerplate/blob/master/publish
book.epub: target
	rm -f $@
	zip -q0X $@ target/mimetype
	zip -qXr9D $@ target/* -x "*.svn*" -x "*~" -x "*.hg*" -x "*.swp" -x "*.DS_Store"
