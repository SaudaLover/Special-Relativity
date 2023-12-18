import pygame, sys
import formulas


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed = 0) -> None:
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

        self.speed = speed

    def update(self, speed):
        if self.is_animating == True:

            self.current_image += speed
            if self.current_image >= len(self.images):
                self.current_image = 0
                self.is_animating = False
                self.speed = 0
                

            self.image = self.images[int(self.current_image)]
            

    def animate(self):
        self.is_animating = True


    def load(self, lst_of_photos):
        for photo in lst_of_photos:
            self.images.append(pygame.image.load(photo))

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
        vel = float(input("What Factor of the speed of light do you want to go at?: "))
        length = float(input("What is the height of our einsteins: "))
        if vel > 0 and vel < 1:
            break
        else:
            print("Put it inbetween 0 and 1 please")
    # lst_of_photos = []
    print("Values:")
    print("Shrinking Value: ", formulas.shrink_factor(vel))
    print("Length Contraction: ", formulas.length_contraction(vel))
    print("Time Dilation: ", formulas.time_dilation(vel))
    print("EInstein height contraction: ", formulas.length_einstein_contraction(vel, length))
    # if vel <= 0.99 and vel > 0.5:
    #     lst_of_photos = []
    #     player.speed = vel/25
    # if vel <= 0.55 and vel > 0.1:
    #     lst_of_photos = []
    #     player.speed = vel/15
    # if vel <=0.1:
    #     lst_of_photos = []
    #     player.speed = vel
    # player.load(lst_of_photos)


    while True:

        
        clock.tick((60))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.animate()
                    player.speed = vel/25

        screen.fill((0, 0, 0))
        moving_sprites.draw(screen)
        pygame.display.flip()
        player.update(player.speed)

main()




