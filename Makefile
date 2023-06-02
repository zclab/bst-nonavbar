PROJECTPATH   	= ./
SPHINXOPTS    	=
SPHINXBUILD   	= sphinx-build
SPHINXPROJ    	= bulma sphinx theme
SOURCEDIR     	= docs
BUILDDIR      	= docs/_build

all: html

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

html: 
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

pdf:
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

clear:
	@rm -rf "$(BUILDDIR)"

open: $(BUILDDIR)/html/index.html
	@open $<

.PHONY: help html all clear open pdf
