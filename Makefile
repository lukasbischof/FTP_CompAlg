# Makefile for running the build process
# to generate the PDF.
#
# Author: Lukas Bischof
# Date: 2024-01-21
# =============================================================================
#
# Usage:
#  make  		  - Build the pdf
#  make clean	- Clean the build directory
#
# =============================================================================
#

build/Summary.pdf : Summary.tex
	@mkdir -p build
	tectonic --print --outdir build Summary.tex

.PHONY: clean
clean:
	rm -rf build
