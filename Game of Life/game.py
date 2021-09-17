import pygame
from controlPanel import ControlPanel
from screen import Screen
from cell import CellPanel

class Game:
	def __init__(self, time_count=0, state='set', period=10, init_life=30, cell_size='M'):
		self.time_count = time_count
		self.state = state		# set, play, stop
		self.period = period
		self.init_life = init_life
		self.cell_size = cell_size

	def process_event(self, bt, status):
		if bt == 'state':
			self.state = status
		elif bt == 'period':
			self.time_count = 1
			self.period = status
		elif bt == 'init_life':
			self.init_life = status

	def is_play(self):
		return(self.time_count%self.period == 0 and self.state == 'play')

	def update_game(self):		
		self.time_count += 1