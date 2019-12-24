all	:
	pandoc -t beamer main.md --listings -H configuration/code_block.tex \
	 -o output.pdf

slides	:
	pandoc -t beamer main.md --listings -H configuration/code_block.tex \
-o slides.pdf

tex	:
	pandoc -t beamer main.md --listings -H configuration/code_block.tex \
-o source_code.tex

ppt	:
	pandoc -t main.md -o slides.pptx

report	:
	pandoc main.md -o report.pdf
