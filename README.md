# qonwaygameoflife
Hackaton Madrid 2019 - Quantum Game of Life

This is three renditions of the quantum game of life - top left is the classical game of life, top right is the semi quantum version
and the bottom is a fully quantum kernel rendition. The fully quantum kernel uses a quantum cloning machine to bring cells to life as an average of the neighbouring cells.

continous boundary conditions!
you can draw live cells!

You can run the file by using 
python life.py seedfile.txt 
or python life.py lower_bound upper_bound 
where lower bound and upper bound are floats between 0 and 1 

Semi quantum simulation is based on https://arxiv.org/pdf/1902.07835.pdf

The quantum kernel is original.

