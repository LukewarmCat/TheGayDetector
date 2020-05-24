import shutil;
from distutils.util import strtobool

columns, rows = shutil.get_terminal_size();
sideRows = int((rows - 19)/2)

class Zui:
	def line(self):
		print('<' * rows + "\n")

	def input(self, text):
			return input('{:^{rows}}'.format(text, rows=rows).rstrip() + " ");

	def confirmation(self, text):
				x = '{:^{rows}}'.format(f'{text} [y/n]', rows=rows)
				print(x)
				while True:
						try:
							return strtobool(input())
						except ValueError:
							print(x)

	def center(self, info="Empty"):
		print('{:^{rows}}'.format(info, rows=rows).rstrip() + "\n")
