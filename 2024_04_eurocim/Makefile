all : conclusion_plot main.pdf

clean :
	rm -f main.aux main.bbl main.blg main.fls main.fdb_latexmk main.pdf main.log main.out main.nav main.toc main.snm

main.pdf : main.tex
	latexmk -pdf -use-make main.tex

conclusion_plot:
	Rscript make_plot.R && latexmk -pdf -use-make figures.tex
