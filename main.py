import pygame, sys
from board import Square, Board
def main():
	pygame.init()
	screen = pygame.display.set_mode((800,800))
	background = (0,183,235)
	screen.fill(background)
	pygame.display.flip()
	board = Board(100)
	board._draw_board(screen)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				sys.exit()
		board.show_moves(screen)
		pygame.display.flip()
	

if __name__ == "__main__":
	main()