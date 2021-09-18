import pygame

class Button:
	def __init__(self, x, y, text, font, text_color, background_color, padding=10):
		self.x = x
		self.y = y
		self.text = text
		self.font = font
		self.text_color = text_color
		self.background_color = background_color
		self.padding = padding

	def draw_button(self, display):
		self.show_text = self.font.render(self.text, 1, self.text_color)
		self.size = (self.show_text.get_size()[0]+self.padding*2, self.show_text.get_size()[1]+self.padding*2)
		self.surface = pygame.Surface(self.size)
		self.surface.fill(self.background_color)
		self.surface.blit(self.show_text, (self.padding, self.padding))
		self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
		display.blit(self.surface, (self.x, self.y))

	def adjust_middle_panel(self, screen):
		self.draw_button(screen.display)
		self.x = int(screen.width*(1-screen.CPRatio) + (screen.width*screen.CPRatio - self.size[0])/2)

	def click(self, event):
		x, y = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0]:		# left mouse clicked
				if self.rect.collidepoint(x, y):
					return(True)
		return(False)

class QuitButton(Button):
	def adjust_position(self, screen):
		super().draw_button(screen.display)
		self.y = 0
		self.x = screen.width - self.size[0]

	def click(self, event):
		x, y = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0]:
				if self.rect.collidepoint(x, y):
					pygame.quit()
					quit()