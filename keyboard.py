from visualize import LayoutVisualizer
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import numpy as np
import random
import math

case_map = dict(zip(ascii_lowercase, ascii_uppercase))

# TODO: map each position to either left hand or right hand

class Key:
	def __init__(self, base, shift):
		self.base = base
		self.shift = shift

	def __repr__(self):
		return f'({self.base}, {self.shift})'

	def __eq__(self, other):
		return self.base == other.base and self.shift == other.shift

	def __hash__(self):
		return hash((self.base, self.shift))

class Layout:
	def __init__(self, keys=None):
		if (keys is not None):
			self.keys = keys
		else:
			self.randomize()

		self._Layout__set_expanded()
		self.fitness = None

	def __repr__(self):
		return ''.join(map(str, self.keys))

	def __set_expanded(self):
		print('Setting expanded')
		keys = ''.join(self.keys)
		for char in ascii_lowercase:
			keys = keys.replace(char, char + case_map[char])

		self.expanded = list(keys)


	@staticmethod
	def crossover(a, b):
		length = len(a.keys)

		start, end = sorted(random.sample(range(length), 2))

		child = [None] * length
		child[start:end + 1] = a.keys[start:end + 1]

		i = (end + 1) % length
		for key in b.keys:
			if (key not in child):
				while (child[i] is not None):
					i = (i + 1) % length
				child[i] = key

		return Layout(child)

	def randomize(self):
		self.keys = list(ascii_lowercase + digits + punctuation)
		random.shuffle(self.keys)
		self.keys = ''.join(self.keys)

	def set_fitness(self, corpus):
		self.fitness = 0
		for char in corpus:
			position = self.expanded.index(char)

			# reaching for the +2 row is really bad
			if (position <= 25):
				self.fitness -= 2

			# reaching for the +-1 row is bad
			elif (26 <= position <= 51):
				self.fitness -= 1

			elif (74 <= position):
				self.fitness -= 1

			# pinky stretching is bad
			if (position in {0, 1, 2, 3, 22, 23, 24, 25, 48, 40, 50, 51}):
				self.fitness -= 1

			# using the same finger twice is bad
			# alternating hands is good

		self.fitness /= len(corpus) / 100

	def mutate(self, mutation_rate=0.1):
		if (random.random() < mutation_rate):
			i, j = random.sample(range(len(self.keys)), 2)
			self.keys[i], self.keys[j] = self.keys[j], self.keys[i]

	def visualize(self):
		visualizer = LayoutVisualizer(self, 'template.png')
		visualizer.visualize()

colemak = Layout("""`~1!2@3#4$5%6^7&8*9(0)-_=+qwfpgjluy;:[{]}\|arstdhneio'"zxcvbkm,<.>/?""")
qwerty = Layout("""`~1!2@3#4$5%6^7&8*9(0)-_=+qwertyuiop[{]}\|asdfghjkl;:'"zxcvbnm,<.>/?""")
