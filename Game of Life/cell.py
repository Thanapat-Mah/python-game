import pygame
import random
from color import Color

class Cell:
	def __init__(self, init_life_percent):
		if random.randint(0, 100) <= init_life_percent:
			self.life = True
		else:
			self.life = False
		self.next_life = False

class CellPanel:
	def __init__(self, screen, init_life_percent=30, size='M'):
		self.display = screen.display
		if size == 'S':
			self.size = 10
		elif size == 'M':
			self.size = 20
		elif size == 'L':
			self.size = 40
		self.col = int(screen.width*(1-screen.CPRatio)//self.size + 1)
		self.row = screen.height//self.size + 1
		self.cells = [[Cell(init_life_percent=init_life_percent) for r in range(self.row)] for c in range(self.col)]

	def count_around_life(self, col, row):
		check = [-1, 0, 1]
		count = 0
		for c in check:
			for r in check:
				if c!=0 or r !=0:
					if ((col+c>=0) and (col+c<self.col)) and ((row+r>=0) and (row+r<self.row)):
						if self.cells[col+c][row+r].life:
							count += 1
		return(count)

	def update_cell(self):
		for c in range(self.col):
			for r in range(self.row):
				count = self.count_around_life(c, r)
				if self.cells[c][r].life:
					if count==2 or count==3:
						self.cells[c][r].next_life = True
					else:
						self.cells[c][r].next_life = False
				else:
					if count==3:
						self.cells[c][r].next_life = True
		for c in range(self.col):
			for r in range(self.row):
				self.cells[c][r].life = self.cells[c][r].next_life

	def set_cell(self, event):
		x, y = pygame.mouse.get_pos()
		target_col = x//self.size
		target_row = y//self.size
		if target_col > self.col or target_row > self.row:
			return(False)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0]:	# left click = set life
				self.cells[target_col][target_row].life = True
			elif pygame.mouse.get_pressed()[2]:		# right click = set dead
				self.cells[target_col][target_row].life = False
		
	def clear(self):
		for c in range(self.col):
			for r in range(self.row):
				self.cells[c][r].life = False
				self.cells[c][r].next_life = False

	def draw_panel(self):
		for c in range(self.col):
			for r in range(self.row):
				if self.cells[c][r].life:
					cell_color = Color.white
				else:
					cell_color = Color.black
				pygame.draw.rect(self.display, cell_color, (c*self.size, r*self.size, self.size, self.size))
				pygame.draw.rect(self.display, Color.dark_gray, (c*self.size, r*self.size, self.size, self.size), 1)
