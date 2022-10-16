import pygame
from math import pi, atan2


class Bow(pygame.sprite.Sprite):
    def __init__(self, initial_position: tuple):
        super().__init__()

        self.image = pygame.Surface((45, 10))
        self.image.fill('blue')
        self.rect = self.image.get_rect(midleft=initial_position)

    def rotate(self, player_center):
        cursor_position = pygame.mouse.get_pos()
        
        # Calcula o ângulo entre o centro do jogador e o cursor
        relative_position = pygame.Vector2(cursor_position) - pygame.Vector2(self.rect.midleft)
        angle = (180 / pi) * -atan2(relative_position[1], relative_position[0])

        bow_image_copy = pygame.transform.rotate(self.image, angle)
        self.image = bow_image_copy
        self.rect = self.image.get_rect(midleft = player_center)

        """Rotate the image of the sprite around a pivot point."""
        """ # Rotate the image.
        self.image = pygame.transform.rotozoom(self.image, -angle, 1)
        # Rotate the offset vector.
        offset_rotated = self.offset.rotate(angle)
        # Create a new rect with the center of the sprite + the offset.
        self.rect = self.image.get_rect(center=self.rect.center+offset_rotated) """

    def update(self, player_center):
        self.rect.midleft = player_center

        #self.rotate(player_center)