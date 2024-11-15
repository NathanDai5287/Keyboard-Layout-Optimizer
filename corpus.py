# TODO: remove api keys and long sections of text in quotes

import random
import os

path = r'C:\Users\natha\Programming'

files = []
for root, _, filenames in os.walk(path):
	for filename in filenames:
		if not (filename.endswith('.py') or filename.endswith('.js')):
			continue

		if ('node_modules' in root):
			continue

		if ('.next' in root):
			continue

		if ('CS61A' in root):
			continue

		if ('Tutorials' in root):
			continue

		if (filename[0] == '.'):
			continue

		if (filename[0] == '_'):
			continue

		if (filename.count('.') >= 2):
			continue

		files.append(os.path.join(root, filename))

random.shuffle(files)

output = ''
for file in files:
	with open(file, 'r', encoding='utf-8') as f:
		output += f.read()

# remove all whitespace
import re
output = re.sub(r'\s+', '', output)

with open('corpus/output.txt', 'w', encoding='utf-8') as f:
	f.write(output)
