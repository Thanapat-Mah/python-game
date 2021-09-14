from color import Color
import pygame
from controlPanel import ControlPanel

class Screen:
	def __init__(self, width=1500, height=750, fullscreen=False, CPRatio=0.3, background_color=Color.black):
		if fullscreen:
			infoObject = pygame.display.Info()
			self.width = infoObject.current_w
			self.height = infoObject.current_h
		else:
			self.width = width
			self.height = height
		self.CPRatio = CPRatio
		self.background_color = background_color
		self.display = pygame.display.set_mode((self.width, self.height))

	def refresh_background(self):
		self.display.fill(self.background_color)

	def update_screen(self, cellPanel):
		self.refresh_background()
		cellPanel.draw_panel()
		# controlPanel = ControlPanel(screen=self)
		# controlPanel.draw_panel()


		# pygame.display.update()