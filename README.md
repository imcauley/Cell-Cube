# Cell Cube
## A genetic algorithm for solving a Rubik's Cube

### Modeling the cube
The actual cube is just modeled as an array. Calling the turn function simply reorders the array. This was done for simplicities sake, as to not require a library for a more complex three dimensional array with transpose functions. To solve the cube requires a [maximum move set of 26 quarter turns.](http://cube20.org/qtm/) So each cube object has a move set of size 26 exactly.

### Creating the genetic algorithm
The algorithm works by first creating a cube and randomly scrambling it, then a population of an arbitrary size is created and set to run for a number of generation. Each member of the generation is tested on how well it solves the cube. Then the algorithm will pick the top half and randomly breed to create the next generation. This is done until a number of set generations has been hit.

### TO DO:
* Add visuals
* Improve the breeding function
* Improve the fitness function
* Add a null move to complete in sub 20 steps
* Run until cube is complete
