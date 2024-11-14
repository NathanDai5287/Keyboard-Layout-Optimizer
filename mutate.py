import random
from keyboard import Layout
import nltk
from concurrent.futures import ThreadPoolExecutor
import cProfile
import pstats

POPULATION_SIZE = 20
GENERATIONS = 2000
MUTATION_RATE = 0.2
# CORPUS = ''.join(nltk.corpus.brown.words())[:1000]
CORPUS = open('corpus/output.txt', 'r', encoding='utf-8').read().replace('’', '\'')[:10000]
KEEP_RATE = 0.5

population = [Layout() for _ in range(POPULATION_SIZE)]

# for generation in range(GENERATIONS):
static = 0
previous_fitness = float('-inf')
generation = 0
while (static < 100):
	# [layout.set_fitness(CORPUS) for layout in population]
	with ThreadPoolExecutor(max_workers=POPULATION_SIZE) as executor:
		executor.map(lambda layout: layout.set_fitness(CORPUS), population)

	population.sort(key=lambda layout: layout.fitness, reverse=True)
	best = population[0].fitness

	if (best == previous_fitness):
		static += 1
	else:
		static = 0
	previous_fitness = best

	print(f'Generation {generation}: {population[0].fitness}')

	keep = int(POPULATION_SIZE * KEEP_RATE)
	new_population = population[:keep]

	for _ in range(POPULATION_SIZE - keep):
		parent1, parent2 = random.sample(population, 2)
		child = Layout.crossover(parent1, parent2)
		child.mutate(MUTATION_RATE)
		new_population.append(child)

	population = new_population

	generation += 1

population[0].visualize()
population[0].dump('keyboards/keyboard.pkl')
