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

	def visualize(self):
		template = Image.open(self.template_path)
		draw = ImageDraw.Draw(template)
		font = ImageFont.truetype('arial.ttf', 24)

		i = 0
		for row, length in zip(self.row_start_positions, self.row_lengths):
			for col in range(length):
				x = row[0] + (col * self.column_spacing)
				y = row[1]

				lower = self.expanded[i]
				upper = self.expanded[i + 1]

				draw.text((x, y), lower, fill='black', font=font)
				draw.text((x, y - self.row_spacing), upper, fill='black', font=font)

				i += 2

		template.save('images/delete.png')
