import pygame

pygame.init()

W, H = 800, 600
WB, HB = 50, 525
WM, HM = 150, 120
WK, HK = 150, 170
HK2 = 220
W4, H4 = 150, 270
H42 = 320

sc = pygame.display.set_mode((W, H))
FPS = 60
clock = pygame.time.Clock()

surf = pygame.image.load('fon1.jpg').convert_alpha()
sc.blit(surf, (0, 0))

#тарелка 130 54
tr = pygame.image.load('tlv1.png').convert_alpha()
r_tr = tr.get_rect(center = (50, 525))

#патрон
bullet = pygame.Surface((3, 6))
bullet.fill((255, 255, 255))
r_bullet = bullet.get_rect(center = (50, 525))
bullet.set_alpha(0)

#score
f = pygame.font.SysFont('arial', 30)
scb = f.render(str('SCORE'), 1, (0, 255, 0))
score = 0
scorep = f.render(str(score), 1, (0, 255, 0))

#LIVES
livb = f.render(str('LIVES'), 1, (0, 255, 0))
lives = 3

#медуз
class medus(pygame.sprite.Sprite):
    def __init__(self, WM, HM):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('med.png').convert_alpha()
        self.rect = self.image.get_rect(center = (WM, HM))

medusi = pygame.sprite.Group()
for i in range(11):
    medusi.add(medus(WM, HM))
    WM += 50

#krab
class krab(pygame.sprite.Sprite):
    def __init__(self, WK, HK):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('kra.png').convert_alpha()
        self.rect = self.image.get_rect(center = (WK, HK))

krabi = pygame.sprite.Group()
for i in range(11):
    krabi.add(krab(WK, HK))
    krabi.add(krab(WK, HK2))
    WK += 50

#n4
class n4(pygame.sprite.Sprite):
    def __init__(self, W4, H4):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('n4.png').convert_alpha()
        self.rect = self.image.get_rect(center = (W4, H4))

n4i = pygame.sprite.Group()
for i in range(11):
    n4i.add(n4(W4, H4))
    n4i.add(n4(W4, H42))
    W4 += 50

speed_tr = 3
speed_bullet = 5
fb = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        r_tr.x -= speed_tr
    elif keys[pygame.K_RIGHT]:
        r_tr.x += speed_tr
    if keys[pygame.K_SPACE] and fb == 0:
        fb = 1
        bullet.set_alpha(255)
        r_bullet.x = r_tr.x + 37

    if fb == 1:
        r_bullet.y -= speed_bullet
        if r_bullet.y < 0:
            fb = 0
            bullet.set_alpha(0)
            r_bullet.x = r_tr.x + 37
            r_bullet.y = HB

    sc.blit(surf, (0, 0))
    sc.blit(scb, (10, 10))
    sc.blit(scorep, (110, 10))
    sc.blit(livb, (300, 10))
    if lives >= 1:
        sc.blit(tr, (375, 10))
    if lives >= 2:
        sc.blit(tr, (375, 10))
        sc.blit(tr, (460, 10))
    if lives == 3:
        sc.blit(tr, (375, 10))
        sc.blit(tr, (460, 10))
        sc.blit(tr, (545, 10))
    sc.blit(tr, r_tr)
    sc.blit(bullet, r_bullet)
    medusi.draw(sc)
    krabi.draw(sc)
    n4i.draw(sc)

    pygame.display.update()
    clock.tick(FPS)
