EPUB_FILENAME:=book.epub
PDF_FILENAME:=book.pdf

all: clean $(PDF_FILENAME)

target: src/* layouts/*
	jorge build

posts: posts.in
	cat posts.in | xargs -I {} cp {} src/OEBPS/Text
	find src/OEBPS/Text -type f -name "*.org" -exec perl -pi -e 's|\[file:([^/\]]+?)(/)?\]|\[file:\1/index.html\]|g' {} +

images: src/OEBPS/img/.stamp

# TODO exaplain this
INLINE_IMAGES:=$(shell grep -oRSh 'static_root*[^"[:space:]]*' src/OEBPS/Text | sort | uniq | sed -E 's|static_root}}/||')
COVER_IMAGES:=$(shell grep -oRSh 'cover-img:.*$$' src/OEBPS/Text | sort | uniq | sed -E 's|cover-img: |img/|')
src/OEBPS/img/.stamp: src/OEBPS/Text/* config.yml
	rm -rf src/OEBPS/img
	@for file in $(INLINE_IMAGES) $(COVER_IMAGES); do \
          echo "copying $$file";\
	  mkdir -p $$(dirname src/OEBPS/$$file) ;\
          cp ../src/assets/$$file "src/OEBPS/$$file";\
        done
	touch $@

# based on https://github.com/javierarce/epub-boilerplate/blob/master/publish
$(EPUB_FILENAME): posts images target
	rm -f $@
	cd target && zip -q0X ../$@ mimetype
	cd target && zip -qXr9D ../$@ * -x "*.svn*" -x "*~" -x "*.hg*" -x "*.swp" -x "*.DS_Store"

$(PDF_FILENAME): $(EPUB_FILENAME)
	ebook-convert $(EPUB_FILENAME) $(PDF_FILENAME)

check:
	epubcheck $(EPUB_FILENAME)

clean:
	rm -rf src/OEBPS/img
	rm -rf src/OEBPS/Text/*.org
	rm -rf
	rm -rf $(EPUB_FILENAME)
	rm -rf $(PDF_FILENAME)
