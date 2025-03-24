import pygame, sys
from board import Square
def main():
	pygame.init()
	screen = pygame.display.set_mode((800,800))
	background = (0,183,235)
	screen.fill(background)
	pygame.display.flip()

	test_square_black = Square("black")
	test_square_white = Square("white")

	test_square_white._draw_square(screen)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		pygame.display.flip()
	

if __name__ == "__main__":
	main()