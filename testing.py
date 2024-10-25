import nltk

CORPUS = ''.join(nltk.corpus.brown.words())[:10000]

from keyboard import colemak, qwerty, Layout

qwerty.set_fitness(CORPUS)
print(qwerty.fitness)

colemak.set_fitness(CORPUS)
print(colemak.fitness)

colemak.visualize()
