OUTDIR=out
MODE=nonstopmode
MAIN=main.tex

all:
	latexmk -shell-escape -xelatex -bibtex -pvc -interaction=$(MODE) -outdir=$(OUTDIR) -auxdir=$(OUTDIR) -f $(MAIN)

clean:
	latexmk -outdir=$(OUTDIR) -C
