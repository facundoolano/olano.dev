.PHONY: posts
EPUB_FILENAME:=book.epub
PDF_FILENAME:=book.pdf
BOOK_FILTER_KEY:=vol1

all: clean $(PDF_FILENAME)

target: src/* layouts/*
	jorge build

# copy the posts flagged as belonging to the BOOK_FILTER_KEY over to this project, so they are included in the epub
# patches the org file: links so they work as in-book hyperlinks
# TODO the perl hack may be avoided by making the /index.html change optional in jorge
posts:
	cd ../ && jorge meta 'site.posts | where:"book","$(BOOK_FILTER_KEY)" | map:"src_path"' | jq -r '.[]' | xargs -I {} cp {} book/src/OEBPS/Text
	find src/OEBPS/Text -type f -name "*.org" -exec perl -pi -e 's|\[file:([^/\]]+?)(/)?\]|\[file:\1/index.html\]|g' {} +

images: src/OEBPS/img/.stamp

# lookup all images used in the front matter or the post contents and copy them from the parent project
# so only used images are bundled in the epub.
INLINE_IMAGES:=$(shell grep -oRSh 'static_root*[^"[:space:]]*' src/OEBPS/Text | sort | uniq | sed -E 's|static_root}}/img/||')
COVER_IMAGES:=$(shell jorge meta 'site.posts | map:"cover-img" | compact' | jq -r '.[]')
src/OEBPS/img/.stamp: src/OEBPS/Text/* config.yml
	rm -rf src/OEBPS/img
	@for file in $(INLINE_IMAGES) $(COVER_IMAGES); do \
          echo "copying $$file";\
	  mkdir -p $$(dirname src/OEBPS/img/$$file) ;\
          cp ../src/assets/img/$$file "src/OEBPS/img/$$file";\
        done
	touch $@

# based on https://github.com/javierarce/epub-boilerplate/blob/master/publish
$(EPUB_FILENAME): posts images target
	rm -f $@
	cd target && zip -q0X ../$@ mimetype
	cd target && zip -qXr9D ../$@ * -x "*.svn*" -x "*~" -x "*.hg*" -x "*.swp" -x "*.DS_Store"

$(PDF_FILENAME): $(EPUB_FILENAME)
	ebook-convert $(EPUB_FILENAME) $(PDF_FILENAME) --extra-css "body {line-height: 1.6;}"

check:
	epubcheck $(EPUB_FILENAME)

clean:
	rm -rf src/OEBPS/img
	rm -rf src/OEBPS/Text/*.org
	rm -rf $(EPUB_FILENAME)
	rm -rf $(PDF_FILENAME)
