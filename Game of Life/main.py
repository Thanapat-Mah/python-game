import pygame
from color import Color
from controlPanel import ControlPanel
from screen import Screen
from cell import CellPanel

def play_game(screen, cellPanel, controlPanel):
	time_count = 0
	state = 'set'
	period = 1
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				
			# check for user trigger event
			bt, status = controlPanel.check_event(event, period)
			if bt == 'playpause':
				state = status
			elif bt == 'cellsize':
				cellPanel = CellPanel(screen=screen, size=status)
				controlPanel.reset_time()
			elif bt == 'speed':
				time_count = 1
				period = status

		# playing next generation over time
		if time_count%period == 0 and state == 'play':
			controlPanel.tick_time()
			cellPanel.update_cell()

		# drawing component	
		screen.update_screen(cellPanel)
		controlPanel.draw_panel()
		pygame.display.update()
		pygame.time.wait(1)
		time_count += 1
	pygame.quit()

if __name__ == '__main__':
	pygame.init()
	
	screen = Screen()	
	cellPanel = CellPanel(screen=screen, size='M')
	controlPanel = ControlPanel(screen=screen, cell_size='M')
	
	play_game(screen, cellPanel, controlPanel)