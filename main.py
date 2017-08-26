import cube
from species import Population

new_cube = cube.Cube()
new_cube.scramble()

new_pop = Population(new_cube)

while new_pop.generation < 5:
    print(new_pop.best_species())
    new_pop.new_generation()
