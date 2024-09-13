EPUB_FILENAME:=book.epub

all: book.epub

target: src/* layouts/*
	jorge build

# TODO exaplain this
USED_IMAGES:=$(shell grep -oRSh 'static_root*[^"[:space:]]*' src/OEBPS/Text | sort | uniq | sed -E 's|static_root}}/||')
src/OEBPS/img/.stamp: src/OEBPS/Text/* config.yml
	rm -rf src/OEBPS/img
	@for file in $(USED_IMAGES); do \
          echo "processing $$file";\
	  mkdir -p $$(dirname src/OEBPS/$$file) ;\
          cp ../src/assets/$$file "src/OEBPS/$$file";\
        done
	touch $@

images: src/OEBPS/img/.stamp


# FIXME apply a similar fix to links

# based on https://github.com/javierarce/epub-boilerplate/blob/master/publish
$(EPUB_FILENAME): images target
	rm -f $@
	cd target && zip -q0X ../$@ mimetype
	cd target && zip -qXr9D ../$@ * -x "*.svn*" -x "*~" -x "*.hg*" -x "*.swp" -x "*.DS_Store"

check:
	epubcheck $(EPUB_FILENAME)

clean:
	rm -rf src/OEBPS/img
	rm -rf
	rm -rf $(EPUB_FILENAME)
