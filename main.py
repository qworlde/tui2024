import pygame

pygame.init()

W, H = 800, 600
WB, HB = 50, 525

sc = pygame.display.set_mode((W, H))
FPS = 60
clock = pygame.time.Clock()

surf = pygame.Surface((W, H))
surf.fill((0, 0, 0))
sc.blit(surf, (0, 0))

#тарелка 130 54
tr = pygame.image.load('tlv1.png').convert_alpha()
r_tr = tr.get_rect(center = (50, 550))

#патрон
bullet = pygame.Surface((3, 6))
bullet.fill((255, 255, 255))
r_bullet = bullet.get_rect(center = (50, 525))
bullet.set_alpha(0)

#score
f = pygame.font.SysFont('arial', 30)
scb = f.render(str('SCORE'), 1, (0, 255, 0))
score = 0

#LIVES
livb = f.render(str('LIVES'), 1, (0, 255, 0))
lives = 3

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
    sc.blit(livb, (400, 10))
    sc.blit(tr, r_tr)
    sc.blit(bullet, r_bullet)
    pygame.display.update()
    clock.tick(FPS)