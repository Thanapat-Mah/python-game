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

			if game.state == 'set':
				cellPanel.set_cell(event)

			# check for user trigger event
			bt, status = controlPanel.check_event(event, game)
			if bt == 'quit':
				run = False 
			elif bt == 'cellsize':
				game.cell_size = status
				cellPanel = CellPanel(screen=screen, game=game)
				controlPanel.reset_time()
				game.state = 'set'
			elif bt == 'clear':
				cellPanel.clear()
				controlPanel.reset_time()
				game.state = 'set'
			else:
				game.process_event(bt, status)

		# playing next generation over time
		if game.is_play():
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
	
	game = Game()
	screen = Screen(fullscreen=True)	
	controlPanel = ControlPanel(screen=screen, game=game)
	cellPanel = CellPanel(screen=screen, game=game)
	
	
	play_game(screen, cellPanel, controlPanel, game)