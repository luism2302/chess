import pygame

class Piece(pygame.sprite.Sprite):
	def __init__(self, color: bool, rect: pygame.Rect, i: int):
		super().__init__()
		self.color: bool  = color
		self.rect: pygame.Rect  = pygame.Rect(rect.left + 15, rect.top + 15, rect.width, rect.height)
		self.i = i
		self.clicked = False

	def update(self):
		pass
	def _show_moves(self):
		pass

class Pawn(Piece):
	def __init__(self, color: bool, rect: pygame.Rect, i: int):
		super().__init__(color, rect, i)
		if self.color:
			self.image = pygame.transform.smoothscale(pygame.image.load("pieces_sprites/b_pawn_1x_ns.png"),(70,70))
		else:
			self.image = pygame.transform.smoothscale(pygame.image.load("pieces_sprites/w_pawn_1x_ns.png"),(70,70))
	def update(self, rects, surface):
		cursor = pygame.mouse.get_pos()
		if self.rect.collidepoint(cursor):
			if pygame.mouse.get_pressed()[0] and not self.clicked:
				self.clicked = True
				if self.color: 
					pygame.draw.circle(surface, (201,200,180), rects[self.i + 8].center, 20)
				else:
					pygame.draw.circle(surface, (201,200,180), rects[self.i - 8].center, 20)
				print("Pawn Clicked")
			if not pygame.mouse.get_pressed()[0]:
				self.clicked = False




		

