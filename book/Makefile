.PHONY: images

all: book.epub

target: src/* layouts/*
	jorge build

images:
	mkdir -p target/OEBPS/Images
	@for file in $(shell grep -oRSh 'assets[^"[:space:]]*' target/OEBPS/Text | sort | uniq); do \
          newname=$$(echo $$file | sed 's/\//_/g');\
          ln -s $$(realpath "../src/$$file") "target/OEBPS/Images/$$newname";\
          find target/OEBPS/Text -type f -exec sed -i '' "s|/$$file|../../Images/$$newname|g" {} +; \
          find target/OEBPS/Text -type f -exec sed -i '' "s|$$file|../../Images/$$newname|g" {} +; \
	done

# based on https://github.com/javierarce/epub-boilerplate/blob/master/publish
book.epub: target images
	rm -f $@
	cd target && zip -q0X ../$@ mimetype
	cd target && zip -qXr9D ../$@ * -x "*.svn*" -x "*~" -x "*.hg*" -x "*.swp" -x "*.DS_Store"
