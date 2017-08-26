import random
from cube import Cube
import copy

class Specimen:
    def __init__(self, sample_cube):
        self.moves = []
        self.fitness = 0

        while len(self.moves) != len(sample_cube.moves):
            new_move = random.randint(-6, 6)
            if new_move != 0:
                self.moves.append(new_move)

    def check_fitness(self, new_cube):
        fitness = 0
        sample_cube = copy.copy(new_cube)

        for m in self.moves:
            sample_cube.turn(m)

        count = 0
        while count != len(sample_cube.cube):
            if sample_cube.cube[count] == count:
                fitness = fitness + 1
            count = count + 1

        self.fitness = fitness

        return fitness

class Population:
    def __init__(self, sample_cube):
        self.population_size = 50
        self.generation = 0

        self.sample = []
        self.parents = []
        #self.best_fitness

        self.sample_cube = sample_cube

        for i in range(self.population_size):
            self.sample.append(Specimen(sample_cube))

    def breed(self, mother, father):
        midpoint = random.randint(0, 25)

        child = Specimen(self.sample_cube)

        count = 0
        while count != len(mother.moves):
            if count < midpoint:
                child.moves[count] = mother.moves[count]
            else:
                child.moves[count] = father.moves[count]

            count = count + 1

        return child

    def find_fitest(self):
        fitnesses = []
        best_species = []

        for s in self.sample:
            s.fitness = s.check_fitness(self.sample_cube)
            fitnesses.append(s.fitness)

        mid = (min(fitnesses) + max(fitnesses)) / 2

        for s in self.sample:
            if s.fitness >= mid:
                best_species.append(s)

        return best_species

    def best_species(self):
        best = self.find_fitest()
        fitnesses = []
        for x in best:
            fitnesses.append(x.fitness)

        return max(fitnesses)

    def new_generation(self):
        parents = self.find_fitest()
        children = []

        for _ in range(self.population_size):
            mother = random.choice(parents)
            father = random.choice(parents)
            child = self.breed(mother, father)
            children.append(child)

        self.sample = children
        self.generation = self.generation + 1
