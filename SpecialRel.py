import pygame, sys


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y) -> None:
        super().__init__()
        self.images = []
        self.images.append(pygame.image.load('images/download.jpg'))
        self.images.append(pygame.image.load('images/download (1).jpg'))  
        self.images.append(pygame.image.load('images/download (2).jpg'))     
        self.current_image = 0
        self.image = self.images[self.current_image]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

        self.is_animating = False

    def update(self):
        if self.is_animating == True:

            self.current_image += 0.1
            try:
                if self.current_image >= len(self.images):
                    self.current_image = 0
                    self.is_animating = False

                self.image = self.images[int(self.current_image)]
            except:
                

    def animate(self):
        self.is_animating = True

def main():
    pygame.init()
    clock = pygame.time.Clock

    screen_width = 960
    screen_height = 540
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Sprite Animation")

    moving_sprites = pygame.sprite.Group()
    player = Player(0, 0)
    moving_sprites.add(player)

    clock = pygame.time.Clock()
    
    while True:
        clock.tick((60))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                player.animate()

        screen.fill((0, 0, 0))
        moving_sprites.draw(screen)
        pygame.display.flip()
        moving_sprites.update()
        





main()




