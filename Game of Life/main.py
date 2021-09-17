import pygame
from controlPanel import ControlPanel
from screen import Screen
from cell import CellPanel
from game import Game

def play_game(screen, cellPanel, controlPanel, game):
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			# check for user trigger event
			bt, status = controlPanel.check_event(event, game.period)
			if bt == 'cellsize':
				cellPanel = CellPanel(screen=screen, size=status)
				controlPanel.reset_time()
			else:
				game.process_event(bt, status)

		# playing next generation over time
		if game.play_next():
			controlPanel.tick_time()
			cellPanel.update_cell()

		# drawing component	
		screen.update_screen(cellPanel)
		controlPanel.draw_panel()
		game.update_game()
		pygame.display.update()
		pygame.time.wait(1)		
	pygame.quit()

if __name__ == '__main__':
	pygame.init()
	
	screen = Screen()
	cellPanel = CellPanel(screen=screen, size='M')
	controlPanel = ControlPanel(screen=screen, cell_size='M')
	game = Game()
	
	play_game(screen, cellPanel, controlPanel, game)