import pygame
from color import Color
from font import Font
from button import Button
from button import TwoStateButton
from button import CellSizeButton
from button import QuitButton
from slideBar import SlideBar

class ControlPanel:
	def __init__(self, screen, game, background_color=Color.white):
		self.display = screen.display
		self.x = int(screen.width*(1-screen.CPRatio))-1
		self.y = 0
		self.width = int(screen.width*screen.CPRatio)+1
		self.height = screen.height
		self.background_color = background_color
		self.time = 0
		self.playstop_bt = TwoStateButton(x=self.x+280, y=305, text_list=['play', 'stop'], font=Font.comic_small, text_color_list=[Color.white, Color.white], background_color_list=[Color.green, Color.red])
		self.clear_bt = Button(x=self.x+200, y=500, text='clear', font=Font.comic_small, text_color=Color.white, background_color=Color.red)
		self.clear_bt.adjust_middle_panel(screen)
		self.cellsize_bt = CellSizeButton(x=self.x+290, y=195, text=str(game.cell_size), font=Font.comic_small, text_color=Color.white, background_color=Color.black)
		self.speed_bar = SlideBar(x=self.x+50, y=290, name='Time period', font=Font.comic_small, text_color=Color.black, bar_lenght=200,
								bar_color=Color.gray, point_color=Color.dark_gray, min_label='fast', max_label='slow', value=game.period, min_value=1, max_value=100)
		self.init_life_bar = SlideBar(x=self.x+50, y=180, name='Initial life cell', font=Font.comic_small, text_color=Color.black, bar_lenght=200,
								bar_color=Color.gray, point_color=Color.dark_gray, min_label='0%', max_label='100%', value=game.init_life, min_value=0, max_value=100)
		self.fullscreen = screen.fullscreen
		if self.fullscreen:
			self.quit_bt = QuitButton(x=0, y=0, text='X', font=Font.comic_normal, text_color=Color.white, background_color=Color.red)
			self.quit_bt.adjust_position(screen=screen)

	def reset_time(self):
		self.time = 0

	def tick_time(self):
		self.time += 1

	def draw_background(self):
		pygame.draw.rect(self.display, self.background_color, (self.x, self.y, self.width, self.height))

	def draw_time(self):
		time_label = Font.comic_normal.render('Time: ', 1, Color.blue)
		time = Font.comic_normal.render(str(self.time), 1, Color.green)
		self.display.blit(time_label, (self.x+50, 100))
		self.display.blit(time, (self.x+50+time_label.get_width(), 100))

	def draw_panel(self):
		self.draw_background()
		self.draw_time()
		self.playstop_bt.draw_button(self.display)
		self.clear_bt.draw_button(self.display)
		self.cellsize_bt.draw_button(self.display)
		self.speed_bar.draw_bar(display=self.display)
		self.init_life_bar.draw_bar(display=self.display)
		if self.fullscreen:
			self.quit_bt.draw_button(self.display)

	def check_event(self, event, game):
		bt = None
		status = None
		adjust_speed, new_period = self.speed_bar.update_value(event, game.period)
		adjust_init_life, new_init_life = self.init_life_bar.update_value(event, game.init_life)
		if self.fullscreen:
			self.quit_bt.click(event)
		if self.playstop_bt.click(event):
			bt = 'state'
			if self.playstop_bt.text == 'stop':
				status = 'stop'
				self.playstop_bt.switchState()
				self.clear_bt.mark_enable()
				self.cellsize_bt.mark_enable()
			elif self.playstop_bt.text != 'stop':
				status = 'play'
				self.playstop_bt.switchState()
				self.clear_bt.mark_disable()
				self.cellsize_bt.mark_disable()

		elif self.clear_bt.click(event) and self.playstop_bt.text == 'play':
			bt = 'clear'
				
		elif self.cellsize_bt.click(event) and self.playstop_bt.text == 'play':
			bt = 'cellsize'
			if self.cellsize_bt.text == 'S':
				status = 'M'
				self.cellsize_bt.switchState()
			elif self.cellsize_bt.text == 'M':
				status = 'L'
				self.cellsize_bt.switchState()
			elif self.cellsize_bt.text == 'L':
				status = 'S'
				self.cellsize_bt.switchState()

		elif adjust_speed:
			bt = 'period'
			status = new_period

		elif adjust_init_life:
			bt = 'init_life'
			status = new_init_life

		return(bt, status)