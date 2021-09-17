import pygame
from color import Color
from font import Font
from button import Button
from slideBar import SlideBar

class ControlPanel:
	def __init__(self, screen, cell_size, background_color=Color.white):
		self.display = screen.display
		self.x = int(screen.width*(1-screen.CPRatio))-1
		self.y = 0
		self.width = int(screen.width*screen.CPRatio)+1
		self.height = screen.height
		self.background_color = background_color
		self.time = 0
		self.playstop_bt = Button(x=self.x+100, y=100, text='play', font=Font.comic_small, text_color=Color.white, background_color=Color.green)
		self.cellsize_bt = Button(x=self.x+100, y=150, text=str(cell_size), font=Font.comic_small, text_color=Color.white, background_color=Color.black)
		self.speed_bar = SlideBar(x=self.x+100, y=250, name='Time period', font=Font.comic_small, text_color=Color.black, bar_lenght=200,
								bar_color=Color.gray, point_color=Color.dark_gray, min_label='fast', max_label='slow', value=1, min_value=1, max_value=50)
		self.clear_bt = Button(x=self.x+100, y=200, text='clear', font=Font.comic_small, text_color=Color.white, background_color=Color.red)

	def reset_time(self):
		self.time = 0

	def tick_time(self):
		self.time += 1

	def draw_background(self):
		pygame.draw.rect(self.display, self.background_color, (self.x, self.y, self.width, self.height))

	def draw_time(self):
		time_label = Font.comic_normal.render('Time: ', 1, Color.blue)
		time = Font.comic_normal.render(str(self.time), 1, Color.green)
		self.display.blit(time_label, (self.x, 0))
		self.display.blit(time, (self.x+time_label.get_width(), 0))

	def draw_panel(self):
		self.draw_background()
		self.draw_time()
		self.playstop_bt.draw_button(self.display)
		self.cellsize_bt.draw_button(self.display)
		self.clear_bt.draw_button(self.display)
		self.speed_bar.draw_bar(display=self.display)

	def check_event(self, event, period):
		bt = None
		status = None
		adjust_speed, new_period = self.speed_bar.update_value(event, period)
		if self.playstop_bt.click(event):
			bt = 'state'
			if self.playstop_bt.text == 'stop':
				status = 'stop'
				self.playstop_bt.text = 'play'
				self.playstop_bt.background_color = Color.green	
			elif self.playstop_bt.text != 'stop':
				status = 'play'
				self.playstop_bt.text = 'stop'
				self.playstop_bt.background_color = Color.red

		elif self.cellsize_bt.click(event) and self.playstop_bt.text == 'play':
			bt = 'cellsize'
			if self.cellsize_bt.text == 'S':
				status = 'M'
				self.cellsize_bt.text = 'M'
				self.cellsize_bt.padding = 10				
			elif self.cellsize_bt.text == 'M':
				status = 'L'
				self.cellsize_bt.text = 'L'
				self.cellsize_bt.padding = 15				
			elif self.cellsize_bt.text == 'L':
				status = 'S'
				self.cellsize_bt.text = 'S'
				self.cellsize_bt.padding = 5

		elif self.clear_bt.click(event) and self.playstop_bt.text == 'play':
			bt = 'clear'
				
		elif adjust_speed:
			bt = 'period'
			status = new_period

		return(bt, status)