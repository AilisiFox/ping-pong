from pygame import *

main_win = display.set_mode((700, 500))
background_color = (100, 149, 237)

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, p_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(p_image), (size_x, size_y))
        self.p_speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
    def res(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))

font.init()
font2 = font.Font(None, 36)

class Player(GameSprite):
    def update_r(self):
        keypr = key.get_pressed()
        if keypr[K_w] and self.rect.y > 0:
            self.rect.y -= self.p_speed
        if keypr[K_s] and self.rect.y < 330:
            self.rect.y += self.p_speed
    def update_l(self):
        keypr = key.get_pressed()
        if keypr[K_UP] and self.rect.y > 0:
            self.rect.y -= self.p_speed
        if keypr[K_DOWN] and self.rect.y < 330:
            self.rect.y += self.p_speed

roc1 = Player('Rectangle1.png' , 20,250, 10, 30,170)
roc2 = Player('Rectangle1.png' , 650,250, 10, 30,170)
ball = GameSprite('Ellipse1.png' , 50,250, 10, 40,40)

font.init()
font1 = font.Font(None, 40)
pl1 = font1.render('player 2 is the winner!', True, (255, 215, 0))
pl2 = font1.render('player 1 is the winner!', True, (255, 215, 0))

FPS = 60
clock = time.Clock()
game = True
fin = False
speedx = 4
speedy = 4
while game:
    keys_pr = key.get_pressed()
    for i in event.get():
        if i.type == QUIT:
            game = False

    if fin != True:
        main_win.fill(background_color)
        roc1.update_r()
        roc2.update_l()
        ball.rect.x += speedx
        ball.rect.y += speedy
        
        if ball.rect.y > 450 or ball.rect.y < 0:
            speedy *= -1
        if sprite.collide_rect(roc1, ball) or sprite.collide_rect(roc2, ball):
            speedx *= -1
        if ball.rect.x <= 0:
            main_win.blit(pl1, (200, 200))
            fin = True
        if ball.rect.x >= 700:
            main_win.blit(pl2, (200, 200))
            fin = True
        roc1.res()
        roc2.res()
        ball.res()

    display.update()
    clock.tick(FPS)
