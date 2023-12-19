import pygame
import sys
import formulas


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed = 0) -> None:
        super().__init__()
        self.images = [] 
        self.images.append(pygame.image.load('images\\Untitled presentation.png'))
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
                self.current_image = -1
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
            if vel == 0.01:
                break
        else:
            print("Put it inbetween 0 and 1 please")
    lst_of_photos = []
    print("Values:")
    print("Shrinking Value: ", formulas.shrink_factor(vel))
    print("Length Contraction: ", formulas.length_contraction(vel))
    print("Time Dilation: ", formulas.time_dilation(vel))
    print("EInstein height contraction: ", formulas.length_einstein_contraction(vel, length))
    if vel == 0.01:
        vel = 0.1
    if vel <= 0.99 and vel > 0.45:
        player.images.pop()
        lst_of_photos = ['images\\first_simul\MINI MAN 1\\1(real).jpg', 'images\\first_simul\MINI MAN 1\\2.jpg','images\\first_simul\MINI MAN 1\\3.jpg','images\\first_simul\MINI MAN 1\\4.jpg','images\\first_simul\MINI MAN 1\\5.jpg','images\\first_simul\MINI MAN 1\\6.jpg','images\\first_simul\MINI MAN 1\\7.jpg','images\\first_simul\MINI MAN 1\\8.jpg','images\\first_simul\MINI MAN 1\\9.jpg','images\\first_simul\MINI MAN 1\\10.jpg','images\\first_simul\MINI MAN 1\\11.jpg','images\\first_simul\MINI MAN 1\\12.jpg','images\\first_simul\MINI MAN 1\\13.jpg','images\\first_simul\MINI MAN 1\\14.jpg']
        player.speed = vel/25
    if vel <= 0.45 and vel > 0.1:
        player.images.pop()
        lst_of_photos = ['images\\second_simul\\mini man 2 (1).jpg', 'images\\second_simul\\mini_man_2(2).jpg', 'images\\second_simul\\mINI_mAN_2(3).jpg', 'images\\second_simul\\mini_man_2(4).jpg', 'images\\second_simul\\mini_man_2(5).jpg', 'images\\second_simul\\mini_man_2(6).jpg', 'images\\second_simul\\Mini_man_2(7).jpg', 'images\\second_simul\\mini_man_2(8).jpg', 'images\\second_simul\\mini_man_2(9).jpg', 'images\\second_simul\\mini_man_2(10).jpg', 'images\\second_simul\\mini_man_2(11).jpg', 'images\\second_simul\\mini_man_2(12).jpg', 'images\\second_simul\\MiniMan2(13).jpg', 'images\\second_simul\\miniman2(14).jpg']
        player.speed = vel/15
    if vel <= 0.1:
        player.images.pop()
        lst_of_photos = ['C:\\practice_for_GCIS\\Special-Relativity\\images\\third_simul\\1.jpg', 'C:\\practice_for_GCIS\\Special-Relativity\\images\\third_simul\\2.jpg','C:\\practice_for_GCIS\\Special-Relativity\\images\\third_simul\\3.jpg','C:\\practice_for_GCIS\\Special-Relativity\\images\\third_simul\\4.jpg','images\\third_simul\\5.jpg','images\\third_simul\\6.jpg','images\\third_simul\\7.jpg','images\\third_simul\\8.jpg','images\\third_simul\\9.jpg','images\\third_simul\\10.jpg','images\\third_simul\\11.jpg','images\\third_simul\\12.jpg','images\\third_simul\\13.jpg','images\\third_simul\\14.jpg']
        player.speed = vel*1000
    player.load(lst_of_photos)


    while True:
        
        clock.tick(60)
        events = pygame.event.get()
        for event in events:
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




