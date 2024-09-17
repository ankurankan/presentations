all: figures.pdf main.pdf

clean :
	rm -f main.aux main.bbl main.blg main.fls main.fdb_latexmk main.pdf main.log main.out main.nav main.toc main.snm

main.pdf : main.tex
	latexmk -shell-escape -pdf -use-make main.tex

figures.pdf : figures.tex
	latexmk -pdf -use-make figures.tex
