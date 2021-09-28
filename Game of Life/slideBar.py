import pygame

class SlideBar:
	def __init__(self, x, y, name, font, text_color, bar_lenght, bar_color, point_color, min_label='min', max_label='max', value=1, min_value=1, max_value=100):
		self.x = x
		self.y = y
		self.name = name
		self.font = font
		self.text_color = text_color
		self.bar_lenght = bar_lenght
		self.bar_color = bar_color
		self.point_color = point_color
		self.min_label = min_label
		self.max_label = max_label
		self.value = value
		self.min_value = min_value
		self.max_value = max_value

	def draw_bar(self, display):
		# name
		self.show_name = self.font.render(self.name, 1, self.text_color)
		show_name_size = self.show_name.get_size()
		display.blit(self.show_name, (self.x+(self.bar_lenght-show_name_size[0])/2, self.y))
		# bar
		self.surface = pygame.Surface((self.bar_lenght, 6))
		self.surface.fill(self.bar_color)
		self.bar = pygame.Rect(self.x-5, self.y+show_name_size[1]+5, self.bar_lenght+10, 20)
		display.blit(self.surface, (self.x, self.y+show_name_size[1]+12))
		# point
		point_x = self.x+self.bar_lenght*(self.value-self.min_value)/(self.max_value-self.min_value)
		point_y = self.y+show_name_size[1]+15
		pygame.draw.circle(display, self.point_color, (point_x, point_y), 10)
		# min label
		self.show_min_label = self.font.render(self.min_label, 1, self.text_color)
		display.blit(self.show_min_label, (self.x, self.y+show_name_size[1]+30))
		# max label
		self.show_max_label = self.font.render(self.max_label, 1, self.text_color)
		show_max_label_size = self.show_max_label.get_size()
		display.blit(self.show_max_label, (self.x+self.bar_lenght-show_max_label_size[0], self.y+show_name_size[1]+30))

	def update_value(self, event):
		clicked = False
		x, y = pygame.mouse.get_pos()
		
		# update value
		if pygame.mouse.get_pressed()[0]:
			if self.bar.collidepoint(x, y):
				clicked = True
				if x <= self.x:
					self.value = self.min_value
				elif x > self.x+self.bar_lenght:
					self.value = self.max_value
				else:
					self.value = int(self.min_value + (self.max_value-self.min_value)*(x-self.x)/self.bar_lenght)
		return(clicked, self.value)