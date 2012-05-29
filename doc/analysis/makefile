all: projet.pdf

projet.pdf : projet.tex besoin.tex recit.tex fonctionnalite.tex versions.tex
	pdflatex projet.tex
	clean

clean:
	rm -f *.aux *.lof *.log  *.lot *.out *.toc
