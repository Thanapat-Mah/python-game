import pygame
from controlPanel import ControlPanel
from screen import Screen
from cell import CellPanel

class Game:
	def __init__(self, time_count=0, state='set', period=1):
		self.time_count = time_count
		self.state = state
		self.period = period

	def process_event(self, bt, status):
		if bt == 'playpause':
			self.state = status
		elif bt == 'speed':
			self.time_count = 1
			self.period = status

	def play_next(self):
		return(self.time_count%self.period == 0 and self.state == 'play')

	def update_game(self):		
		self.time_count += 1