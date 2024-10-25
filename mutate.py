import random
from keyboard import Layout
import nltk
from concurrent.futures import ThreadPoolExecutor

POPULATION_SIZE = 500
GENERATIONS = 100
MUTATION_RATE = 0.2
CORPUS = ''.join(nltk.corpus.brown.words())[:10000]
KEEP_RATE = 0.5

population = [Layout() for _ in range(POPULATION_SIZE)]

for generation in range(GENERATIONS):
	# [layout.set_fitness(CORPUS) for layout in population]
	with ThreadPoolExecutor(max_workers=POPULATION_SIZE) as executor:
		executor.map(lambda layout: layout.set_fitness(CORPUS), population)

	population.sort(key=lambda layout: layout.fitness, reverse=True)

	print(f'Generation {generation}: {population[0].fitness}')

	keep = int(POPULATION_SIZE * KEEP_RATE)
	new_population = population[:keep]

	for _ in range(POPULATION_SIZE - keep):
		parent1, parent2 = random.sample(population, 2)
		child = Layout.crossover(parent1, parent2)
		child.mutate(MUTATION_RATE)
		new_population.append(child)

	population = new_population

print(population[0])
