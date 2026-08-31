# labbook/Makefile
#
# `cd labbook && make` builds main.pdf via latexmk (CLAUDE.md "Session close",
# step 2). The raw command `cd labbook && latexmk -pdf main.tex` must also
# work on its own -- this Makefile is a thin, stricter wrapper around it, not
# a replacement for it.

MAIN          := main
LATEXMK       := latexmk
LATEXMK_FLAGS := -pdf -interaction=nonstopmode -halt-on-error

TEX_SOURCES := $(MAIN).tex $(wildcard sections/*.tex)

.PHONY: all clean distclean

all: $(MAIN).pdf

$(MAIN).pdf: $(TEX_SOURCES)
	$(LATEXMK) $(LATEXMK_FLAGS) $(MAIN).tex

# Remove latexmk's intermediate byproducts (.aux/.log/.fls/.fdb_latexmk/...).
# Leaves main.pdf -- the committed product -- untouched.
clean:
	$(LATEXMK) -c $(MAIN).tex

# Also remove main.pdf itself. Only ever intentional: main.pdf is committed
# (it is the product, CLAUDE.md L9), so this should be followed immediately
# by `make` again, never left mid-way.
distclean:
	$(LATEXMK) -C $(MAIN).tex
