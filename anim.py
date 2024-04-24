import pygame
import math

g = 9.8

class co2:
    x, y, r, angle = 0, 0, 0, 0
    x1, y1, x2, y2, rchast = 0, 0, 0, 0, 0
    dx, dy = 4, 4
    k = 1
    def __init__(self,  x, y, r, rchast):
        self.x = x 
        self.y = y
        self.r = r
        self.rchast = rchast
        self.color = (255, 15, 15)
        self.angle = math.pi/4
        self.dangle = math.pi/10
        self.set_angle()

    def set_angle(self):
        self.angle = (self.angle + self.dangle) % (2 * math.pi)
        self.x1 = self.x + int(math.cos(self.angle + math.pi) * self.r)
        self.y1 = self.y + int(math.sin(self.angle+math.pi) * self.r)

        self.x2 = self.x + int(math.cos(self.angle) * self.r)
        self.y2 = self.y + int(math.sin(self.angle) * self.r)

    def move_mol(self):
        self.x = self.x + self.dx
        self.y = self.y + self.k * self.dy*2
        if self.y + self.r >=500:
            self.k = -1

width, height = 800, 650
fps = 30
running = True
mol = co2(150, 10, 25, 15)
pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Керосиновая долина")
clock = pygame.time.Clock()

print(mol.x1, mol.y1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((128,128,128))
    pygame.draw.circle(screen, mol.color, (mol.x, mol.y), mol.r)
    pygame.draw.circle(screen, (255,255,255), (mol.x1, mol.y1), mol.rchast)
    pygame.draw.circle(screen, (255,255,255), (mol.x2, mol.y2), mol.rchast)
    pygame.draw.rect(screen, (255, 215, 0), (300, 500, 200, 100))
    font = pygame.font.SysFont('Arial', 48)
    txt = font.render("ЗОЛОТО", False, (0,0,0))
    screen.blit(txt, (320,520))
    mol.move_mol()
    mol.set_angle()
    print(mol.angle, (mol.x1, mol.y1), (mol.x2, mol.y2))
    pygame.display.update()
    clock.tick(fps)
 
pygame.quit()