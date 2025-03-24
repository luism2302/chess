import pygame

class Square:
	def __init__(self, color, left = 10, top = 10, width = 50, height = 50):
		self._left = left
		self._top = top
		self._width = width
		self._height = height
		self._rectangle = pygame.Rect(self._left, self._top, self._width, self._height)

		match color:
			case "black":
				self._color = pygame.Color(0,0,0)
			case "white":
				self._color = pygame.Color(255,255,255)
			case _:
				raise(Exception("Invalid color: only black and white allowed"))
	
	def _draw_square(self, surface):
		pygame.draw.rect(surface, self._color, self._rectangle)
	