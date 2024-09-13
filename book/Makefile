all: book.epub images

target: src/* layouts/* images
	jorge build

images:
	mkdir -p target/OEBPS/Images
	@for file in $(shell grep -oRSh 'assets[^"[:space:]]*' src/OEBPS/Text | sort | uniq); do \
          newname=$$(echo $$file | sed 's/\//_/g');\
          ln -s $$(realpath "../src/$$file") "target/OEBPS/Images/$$newname";\
	done

# based on https://github.com/javierarce/epub-boilerplate/blob/master/publish
book.epub: target
	rm -f $@
	cd target && zip -q0X ../$@ mimetype
	cd target && zip -qXr9D ../$@ * -x "*.svn*" -x "*~" -x "*.hg*" -x "*.swp" -x "*.DS_Store"
