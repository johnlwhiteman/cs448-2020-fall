.PHONY: clean

CSS = syllabus.css
TITLE = Syllabus

DFLAGS        = \
  --self-contained \
  --standalone \
  --css ${CSS} \
  --metadata title='${TITLE}' \
  --from=markdown \
  --to=docx

EFLAGS        = \
  --self-contained \
  --standalone \
  --css ${CSS} \
  --metadata title='${TITLE}' \
  --from=markdown \
  --to=epub3

PFLAGS        = \
  --from=epub \
  --to=pdf

docx:
	pandoc ${DFLAGS} -i syllabus.md -o syllabus.docx

epub:
	pandoc ${EFLAGS} -i syllabus.md -o syllabus.epub

pdf: epub
	pandoc ${PFLAGS} -i syllabus.epub -o syllabus.pdf

clean:
	-rm -fr *.docx *.epub *.html *.pdf