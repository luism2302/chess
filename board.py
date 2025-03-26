import pygame
from pieces import Pawn

class Square:
	def __init__(self, color : bool, square_size = 100):
		self._square_size: int = square_size
		self._square: pygame.Surface = pygame.Surface((self._square_size, self._square_size))
		self.empty: bool = True
		#True dark false light
		if color:
			self._color = pygame.Color(118,150,86)
			self._square.fill(self._color)
			self.dark =  True
		else:
			self._color = pygame.Color(238,238,210)
			self._square.fill(self._color)
			self.dark = False
	def __repr__(self):
		return f"Square(color = {self._color}, size = {self._square_size}"
	

class Board:
	def __init__(self, square_size : int):
		self.rects: list[pygame.Rect] = []
		self.board: list[Square] = []
		self._square_size: int = square_size
		self.black_pawns = pygame.sprite.Group()
		self.white_pawns = pygame.sprite.Group()
		curr_color: bool = False
		for i in range(8 * 8):
			curr_square = Square(curr_color)
			if (i + 1) % 8 != 0:
				curr_color = not curr_color

			self.board.append(curr_square)
		for rank in range(8):
			for file in range(8):
				curr_rect = pygame.Rect(file * self._square_size, rank * self._square_size, self._square_size, self._square_size)
				self.rects.append(curr_rect)

	def _draw_board(self, surface: pygame.Surface):
		pos_squares = [(self.board[i]._square, self.rects[i]) for i in range(len(self.board))]
		surface.blits(blit_sequence = pos_squares)
		self._draw_pawns(surface)
	
	def _draw_pawns(self, surface: pygame.Surface):
		for i in range(8, 16):
			black_pawn = Pawn(True, self.rects[i], i)
			self.board[i].empty = False
			black_pawn.add(self.black_pawns)
		for i in range(48, 56):
			white_pawn = Pawn(False, self.rects[i], i)
			self.board[i].empty = False
			white_pawn.add(self.white_pawns)
		self.black_pawns.draw(surface)
		self.white_pawns.draw(surface)
	
	def show_moves(self, surface):
		self.white_pawns.update(self.rects, surface)	
		self.black_pawns.update(self.rects, surface)	








	
				

	