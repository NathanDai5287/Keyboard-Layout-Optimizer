from visualize import LayoutVisualizer
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random

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
	# Class variable to store the special characters
	special_chars = list(digits + punctuation)

	def __init__(self, keys=None):
		if keys is not None:
			if isinstance(keys, str):
				self.keys = [Key(base, shift) for base, shift in zip(keys[::2], keys[1::2])]
			else:
				self.keys = keys
		else:
			self.randomize()

		self.__set_expanded()
		self.fitness = None

	def __repr__(self):
		return '[' + ' '.join(map(str, self.keys)) + ']'

	def __set_expanded(self):
		self.expanded = []
		for key in self.keys:
			self.expanded.extend([key.base, key.shift])

	def validate(self):
		assert len(self.keys) == 47  # Adjust this number based on your total keys
		assert len(set(self.keys)) == len(self.keys)

	@staticmethod
	def crossover(a, b):
		length = len(a.keys)
		start, end = sorted(random.sample(range(length), 2))
		child_keys = [None] * length

		# Copy a segment from parent 'a'
		child_keys[start:end+1] = a.keys[start:end+1]

		# Fill the rest from parent 'b' without duplicates
		used_bases = set(key.base for key in child_keys if key is not None)
		b_index = 0
		for i in range(length):
			if child_keys[i] is None:
				while b_index < length and b.keys[b_index].base in used_bases:
					b_index += 1
				if b_index < length:
					child_keys[i] = b.keys[b_index]
					used_bases.add(child_keys[i].base)
					b_index += 1
				else:
					# Should not happen now
					raise ValueError("Ran out of keys to fill child layout")

		# After creating child_keys, re-pair the special keys
		child_layout = Layout(child_keys)
		child_layout.repair_special_keys()

		return child_layout

	def mutate(self, mutation_rate=0.1):
		if random.random() < mutation_rate:
			i, j = random.sample(range(len(self.keys)), 2)
			# Swap entire keys to maintain base and shift pairing
			self.keys[i], self.keys[j] = self.keys[j], self.keys[i]
			# Re-pair the special keys after mutation
			self.repair_special_keys()
			# Update the expanded representation
			self.__set_expanded()

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
		# Implement your fitness calculation here
		pass

	def visualize(self):
		visualizer = LayoutVisualizer(self, 'template.png')
		visualizer.visualize()

# Example usage
if __name__ == "__main__":
	# Generate two parent layouts
	layout1 = Layout()
	layout2 = Layout()

	# Display parent layouts
	print("Layout A:")
	print(layout1)
	print("\nLayout B:")
	print(layout2)

	# Perform crossover to create a child layout
	child_layout = Layout.crossover(layout1, layout2)

	# Display child layout
	print("\nChild Layout:")
	print(child_layout)
