from visualize import LayoutVisualizer
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import numpy as np
import random
import math

import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

case_map = dict(zip(ascii_lowercase, ascii_uppercase))

class Key:
	def __init__(self, base, shift):
		self.base = base
		self.shift = shift

	def __repr__(self):
		return f'Key({self.base}, {self.shift})'

	def __eq__(self, other):
		return isinstance(other, Key) and self.base == other.base and self.shift == other.shift

	def __hash__(self):
		return hash((self.base, self.shift))

class Layout:
	special_chars = list(digits + punctuation)

	def __init__(self, keys=None):
		if keys is not None:
			if isinstance(keys, str):
				self.keys = []
				i = 0
				while (i < len(keys)):
					if (keys[i] in ascii_lowercase):
						self.keys.append(Key(keys[i], keys[i].upper()))
					else:
						self.keys.append(Key(keys[i], keys[i + 1]))
						i += 1
					i += 1
			else:
				self.keys = keys
		else:
			self.randomize()

		self.set_expanded()
		self.fitness = None

	def __repr__(self):
		return '[' + ' '.join(map(str, self.keys)) + ']'

	def set_expanded(self):
		self.expanded = []
		for key in self.keys:
			self.expanded.extend([key.base, key.shift])

	def validate(self):
		assert len(self.keys) == 47
		assert len(set(self.keys)) == len(self.keys)

	@staticmethod
	def crossover(a, b):
		child_keys = [None] * len(a.keys)
		assigned_letters = set()
		letter_positions = []

		# First pass: Assign letter keys
		for i in range(len(a.keys)):
			a_is_letter = a.keys[i].base in ascii_lowercase
			b_is_letter = b.keys[i].base in ascii_lowercase

			if a_is_letter and b_is_letter:
				# Both are letter keys
				if random.random() < 0.5:
					letter = a.keys[i].base
				else:
					letter = b.keys[i].base
			elif a_is_letter:
				letter = a.keys[i].base
			elif b_is_letter:
				letter = b.keys[i].base
			else:
				continue  # Skip if neither is a letter key

			if letter not in assigned_letters:
				child_keys[i] = Key(base=letter, shift=case_map[letter])
				assigned_letters.add(letter)
				letter_positions.append(i)

		# Collect remaining letters not yet assigned
		remaining_letters = set(ascii_lowercase) - assigned_letters
		remaining_positions = [i for i in range(len(child_keys)) if child_keys[i] is None]
		random.shuffle(remaining_positions)
		for letter, i in zip(remaining_letters, remaining_positions):
			child_keys[i] = Key(base=letter, shift=case_map[letter])
			assigned_letters.add(letter)
			letter_positions.append(i)

		# Second pass: Assign special keys
		special_positions = [i for i in range(len(child_keys)) if child_keys[i] is None]
		special_keys_pool = [k for k in (a.keys + b.keys) if k.base not in ascii_lowercase]
		used_special_keys = set()
		for i in special_positions:
			for k in special_keys_pool:
				if k not in used_special_keys:
					child_keys[i] = k
					used_special_keys.add(k)
					break

		# If any positions are still None, create random special keys
		while None in child_keys:
			i = child_keys.index(None)
			base = random.choice(Layout.special_chars)
			shift = random.choice(Layout.special_chars)
			child_keys[i] = Key(base=base, shift=shift)

		# Create the new child layout
		child = Layout(keys=child_keys)
		child.set_expanded()
		return child

	def mutate(self, mutation_rate=0.1):
		if random.random() < mutation_rate:
			i, j = random.sample(range(len(self.keys)), 2)
			# Swap entire keys to maintain base and shift pairing
			self.keys[i], self.keys[j] = self.keys[j], self.keys[i]
			# Re-pair the special keys after mutation
			self.repair_special_keys()
			# Update the expanded representation
			self.set_expanded()

	def repair_special_keys(self):
		# Collect the indices of special keys
		special_key_indices = [idx for idx, key in enumerate(self.keys) if key.base not in ascii_lowercase]

		# Use the class variable special_chars
		special_chars = self.special_chars.copy()
		random.shuffle(special_chars)

		# Ensure the number of special characters is even
		if len(special_chars) % 2 != 0:
			special_chars.append(' ')  # Add a placeholder if necessary

		# Pair up special characters to create special keys
		special_keys = []
		for i in range(0, len(special_chars), 2):
			base = special_chars[i]
			shift = special_chars[i + 1]
			special_keys.append(Key(base=base, shift=shift))

		# Now assign special_keys to the positions in self.keys
		num_special_keys_needed = len(special_key_indices)
		special_keys = special_keys[:num_special_keys_needed]

		for idx, new_key in zip(special_key_indices, special_keys):
			self.keys[idx] = new_key

	def randomize(self):
		letter_keys = [Key(base, shift) for base, shift in zip(ascii_lowercase, ascii_uppercase)]

		special_chars = self.special_chars.copy()
		random.shuffle(special_chars)

		# Ensure the number of special characters is even
		if len(special_chars) % 2 != 0:
			special_chars.append(' ')  # Add a placeholder if necessary

		# Pair up special characters to create special keys
		special_keys = []
		for i in range(0, len(special_chars), 2):
			base = special_chars[i]
			shift = special_chars[i + 1]
			special_keys.append(Key(base=base, shift=shift))

		# Combine all keys into a single list
		all_keys = letter_keys + special_keys

		# Shuffle all keys to randomize their positions
		random.shuffle(all_keys)

		self.keys = all_keys

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

	def visualize(self):
		visualizer = LayoutVisualizer(self, 'template.png')
		visualizer.visualize()

colemak = Layout("""`~1!2@3#4$5%6^7&8*9(0)-_=+qwfpgjluy;:[{]}\|arstdhneio'"zxcvbkm,<.>/?""")
qwerty = Layout("""`~1!2@3#4$5%6^7&8*9(0)-_=+qwertyuiop[{]}\|asdfghjkl;:'"zxcvbnm,<.>/?""")
