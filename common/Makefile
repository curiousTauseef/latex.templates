OUTDIR=out
MODE=nonstopmode
MAIN=main.tex

all:
	latexmk -shell-escape -xelatex -bibtex -pvc -interaction=$(MODE) -outdir=$(OUTDIR) -auxdir=$(OUTDIR) -f $(MAIN)

pdf:
	latexmk -shell-escape -xelatex -bibtex -outdir=$(OUTDIR) -auxdir=$(OUTDIR) -f $(MAIN)
	cp -v $(OUTDIR)/main.pdf jinghao_cv.pdf


clean:
	latexmk -outdir=$(OUTDIR) -C
