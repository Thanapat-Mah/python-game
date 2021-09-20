import pygame
from color import Color

class Button:
	def __init__(self, x, y, text, font, text_color, background_color, padding=10):
		self.x = x
		self.y = y
		self.text = text
		self.font = font
		self.text_color = text_color
		self.background_color = background_color
		self.padding = padding
		self.enable = True

	def mark_enable(self):
		self.enable = True

	def mark_disable(self):
		self.enable = False

	def draw_button(self, display):
		if self.enable:
			txt_color = self.text_color
			bg_color = self.background_color
		else:
			txt_color = Color.white
			bg_color = Color.gray
		self.show_text = self.font.render(self.text, 1, txt_color)
		self.size = (self.show_text.get_size()[0]+self.padding*2, self.show_text.get_size()[1]+self.padding*2)
		self.surface = pygame.Surface(self.size)
		self.surface.fill(bg_color)
		self.surface.blit(self.show_text, (self.padding, self.padding))
		self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
		display.blit(self.surface, (self.x, self.y))

	def adjust_middle_panel(self, screen):
		self.draw_button(screen.display)
		self.x = int(screen.width*(1-screen.CPRatio) + (screen.width*screen.CPRatio - self.size[0])/2)

	def click(self, event):
		if not self.enable:
			return(False)
		x, y = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0]:		# left mouse clicked
				if self.rect.collidepoint(x, y):
					return(True)
		return(False)

class TwoStateButton(Button):
	def __init__(self, x, y, text_list, font, text_color_list, background_color_list, padding=10):
		super().__init__(x=x, y=y, text=text_list[0], font=font, text_color=text_color_list[0], background_color=background_color_list[0], padding=10)
		self.state = 0
		self.text_list = text_list
		self.text_color_list = text_color_list
		self.background_color_list = background_color_list

	def switchState(self):
		if self.state == 0:
			self.state = 1
		else:
			self.state = 0
		self.text = self.text_list[self.state]
		self.text_color = self.text_color_list[self.state]
		self.background_color = self.background_color_list[self.state]

class CellSizeButton(Button):
	def __init__(self, x, y, text, font, text_color, background_color, padding=10):
		super().__init__(x, y, text, font, text_color, background_color, padding=10)
		self.state = 1
		self.text_list = ['S', 'M', 'L']
		self.padding_list = [5, 10, 15]
		self.position_list = [10, -5, -5]

	def switchState(self):
		if self.state == len(self.text_list)-1:
			self.state = 0
		else:
			self.state += 1
		self.text = self.text_list[self.state]
		self.padding = self.padding_list[self.state]
		self.x += self.position_list[self.state]
		self.y += self.position_list[self.state]

class QuitButton(Button):
	def adjust_position(self, screen):
		super().draw_button(screen.display)
		self.y = 0
		self.x = screen.width - self.size[0]

	def click(self, event):
		if not self.enable:
			return(False)
		x, y = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0]:
				if self.rect.collidepoint(x, y):
					pygame.quit()
					quit()