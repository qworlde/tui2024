import pygame

pygame.init()

W, H = 800, 600
WB, HB = 50, 475
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
bullet = pygame.image.load('bull2.png')
r_bullet = bullet.get_rect(center = (50, 475))
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
speed_m = 0.5
p = 1
fb = 0
c = 0
v = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if r_tr.x >= 0:
            r_tr.x -= speed_tr
    elif keys[pygame.K_RIGHT]:
        if r_tr.x <= 725:
            r_tr.x += speed_tr
    if keys[pygame.K_SPACE] and fb == 0:
        fb = 1
        bullet.set_alpha(255)
        r_bullet.x = r_tr.x + 18

    if fb == 1:
        r_bullet.y -= speed_bullet
        if r_bullet.y < 0:
            fb = 0
            bullet.set_alpha(0)
            r_bullet.x = r_tr.x + 18
            r_bullet.y = HB

    if p == 1:
        for n in n4i:
            if n.rect.x >= 740:
                c += 1
                for n1 in n4i:
                    n1.rect.y += 50
                break
            else:
                n.rect.x += 0.5
        
        for kr in krabi:
            if kr.rect.x == 740:
                c += 1
                for kr1 in krabi:
                    kr1.rect.y += 50
                break
            else:
                kr.rect.x += 0.5

        for med in medusi:
            if med.rect.x >= 740:
                c += 1
                for med1 in medusi:
                    med1.rect.y += 50
                break
            else:
                med.rect.x += 0.5
    else:
        print(p)
        for n in n4i:
            n.rect.x -= 0.5
            if n.rect.x <= 0:
                v += 1
                for n1 in n4i:
                    n1.rect.y += 50
                break
            else:
                n.rect.x -= 0.5

        for kr in krabi:
            kr.rect.x -= 0
            if kr.rect.x <= 0:
                v += 1
                for kr1 in krabi:
                    kr1.rect.y += 50
                break
            else:
                kr.rect.x -= 0.5

        for med in medusi:
            med.rect.x -= 0.5
            if med.rect.x <= 0:
                v += 1
                for med1 in medusi:
                    med1.rect.y += 50
                break
            else:
                med.rect.x -= 0.5

    if c == 3:
        p = 0
        c = 0

    if v == 3:
        p = 1
        v = 0
        
    for n in n4i:
        if r_bullet.collidepoint(n.rect.center):
            n.kill()
            fb = 0
            bullet.set_alpha(0)
            r_bullet.x = r_tr.x + 18
            r_bullet.y = HB
            score += 10

    for kr in krabi:
        if r_bullet.collidepoint(kr.rect.center):
            kr.kill()
            fb = 0
            bullet.set_alpha(0)
            r_bullet.x = r_tr.x + 18
            r_bullet.y = HB
            score += 20
    
    for med in medusi:
        if r_bullet.collidepoint(med.rect.center):
            med.kill()
            fb = 0
            bullet.set_alpha(0)
            r_bullet.x = r_tr.x + 18
            r_bullet.y = HB
            score += 40

    scorep = f.render(str(score), 1, (0, 255, 0))
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
