import pathlib
from PIL import Image, ImageDraw, ImageFont

class LayoutVisualizer:
	row_start_positions = [(80, 370), (180, 445), (195, 525), (225, 600)]
	row_lengths = [13, 13, 11, 10]
	column_spacing = 80
	row_spacing = 25

	def __init__(self, layout, template_path):
		self.template_path = template_path
		self.expanded = layout.expanded
		self.name = ''.join(self.expanded[26:36:2])

	def visualize(self, path=None):
		template = Image.open(self.template_path)
		draw = ImageDraw.Draw(template)
		font = ImageFont.truetype('arial.ttf', 24)

		for row, length in zip(self.row_start_positions, self.row_lengths):

			for i in range(length):
				lower = self.expanded[i + (length * 0)]
				upper = self.expanded[i + (length * 1)]

				x = row[0] + (i * self.column_spacing)
				y = row[1]

				draw.text((x, y), lower, fill='black', font=font)
				draw.text((x, y - self.row_spacing), upper, fill='black', font=font)

		# template.save(self.name + '.png')
		template.save('delete.png')
