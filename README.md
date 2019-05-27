# Qiskit Camp - Hackaton Madrid 2019 - Quantum Game of Life

This repo contains our project: slides & code, for the [Qiskit Hackathon Madrid 2019](https://madrid.qiskit.camp/).

## What did we do?

To apply quantum computing to [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life):
* First to try to speed up the generation of new cells
* And then we updated the rules to incorporate quantum physics 

For more details, please have a look to [our presentation](https://raw.githubusercontent.com/qonwaygameoflife/qonwaygameoflife/master/presentation/n_dimensional_quantum_game_of_life.pdf).

## Show me the code

### Environment

In order to run this code, you have to clone this repo & prepare a python virtual environment:

```
> git clone https://github.com/qonwaygameoflife/qonwaygameoflife.git
> cd qonwaygameoflife/
> python3 -m virtualenv QiskitEnv
> source QiskitEnv/bin/activate
(QiskitEnv) > pip install -r requirements.txt
```

### Qonway's Game of Life

![Qonway's Game of Life](https://raw.githubusercontent.com/qonwaygameoflife/qonwaygameoflife/master/images/life.jpeg)

These are three renditions of the quantum game of life - top left is the classical game of life, top right is the semi quantum version
and the bottom is a fully quantum kernel rendition. The fully quantum kernel uses a quantum cloning machine to bring cells to life as an average of the neighbouring cells.

Continous boundary conditions! And you can draw live cells! (draw on the top left classical game and the new cells will be replicated to the other 2).

#### Usage

```
(QiskitEnv) > python gol_2d/life.py -h
pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
usage: life.py [-h] [--sp_up SP_UP] [--sp_down SP_DOWN] [--json JSON]

Quantum Game of Life

optional arguments:
  -h, --help         show this help message and exit
  --sp_up SP_UP      Superposition UP limit (default: 0.51)
  --sp_down SP_DOWN  Superposition DOWN limit (default: 0.48)
  --json JSON        Path to JSON file with pre-configured seed
```

All parameters are optional, if none is informed the entire board is randomly initialized.

Notice that `--sp_up` and `--sp_down` are float values between 0 and 1. Also, they are ignored if `--json` is informed.

We also provide a few JSON seeds you can try in [gol_2d/seeds](https://github.com/qonwaygameoflife/qonwaygameoflife/tree/master/gol_2d/seeds):

```
(QiskitEnv) > python gol_2d/life.py --json gol_2d/seeds/waitforit.json
```

#### Attribution

* Instead of implementing the game from scratch, we re-purposed the code in: https://github.com/adrianchifor/conway-game-of-life.
* Semi quantum simulation is based on: https://arxiv.org/pdf/1902.07835.pdf. The quantum kernel is original.

### 1D Quantum Game of Life

![1D Quantum Game of Life](https://raw.githubusercontent.com/qonwaygameoflife/qonwaygameoflife/master/images/onedgameoflife.jpeg)

In this case, instead of a 2D board to code the Game of Life, we use a 1D quantum register. By putting the qubits in different states as if they were cells: alive (|1>), dead (|0>) or neither alive nor dead (superposition), the idea was to produce all possible results by sequentially applying the same Truth Table Oracle which coded the dead/alive rules. However:
* The resulting circuit was (as you can see above) huge
* The output of an oracle was inputted in the next one but, it is likely, that by doing so we were also propagating an unintended phase change that eventually **corrupted** the results. With 4 or more input qubits, the outputs of the second oracle were no longer valid. 

#### Usage

```
(QiskitEnv) > python gol_1d/onedgameoflife.py 
Input:
☒ ☒ ☒
Output:
□ □ □  <1.7677669529663689>
■ ■ ■  <1.0606601717798212>
Output:
□ □ □  <1.0>
```
