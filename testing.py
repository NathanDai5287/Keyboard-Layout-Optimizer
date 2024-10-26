import nltk

# CORPUS = ''.join(nltk.corpus.brown.words())[:1000]
CORPUS = open('corpus/output.txt', 'r', encoding='utf-8').read().replace('’', '')[:100000]

from keyboard import colemak, qwerty, Layout
import pickle

# qwerty.set_fitness(CORPUS)
# print(qwerty.fitness)

colemak.set_fitness(CORPUS)
print(colemak.fitness)

CORPUS = open('corpus/output.txt', 'r', encoding='utf-8').read()[:1000]
colemak.set_fitness(CORPUS)
print(colemak.fitness)

with open('keyboards/keyboard.pkl', 'rb') as f:
	keyboard = pickle.load(f)

print(keyboard.translate('The quick brown fox jumps over the lazy dog.', colemak))
