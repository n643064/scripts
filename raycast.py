#!/usr/bin/env python3
import pygame 
from math import sin, cos, atan, radians, degrees
from random import randint as rnd

screen = pygame.display.set_mode((800, 800))


class box:
    x1: int
    x2: int
    y1: int
    y2: int
    w: int
    h: int
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1 + x2
        self.y2 = y1 + y2
        self.w = x2
        self.h = y2
        

rays = []
boxes = []
step = 10
radius = 300
angle_range = 30 
pos = [400, 400]
clock = pygame.time.Clock()
box_min = 20
box_max = 60


def gen_boxes():
    for i in range(30):
        boxes.append(box(rnd(0, 700), rnd(0, 200), rnd(box_min, box_max), rnd(box_min, box_max)))
        boxes.append(box(rnd(0, 700), rnd(500, 700), rnd(box_min, box_max), rnd(box_min, box_max)))
        boxes.append(box(rnd(0, 200), rnd(0, 700), rnd(box_min, box_max), rnd(box_min, box_max)))
        boxes.append(box(rnd(500, 700), rnd(0, 700), rnd(box_min, box_max), rnd(box_min, box_max)))


def main():
    gen_boxes()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        k = pygame.key.get_pressed()
        if k[pygame.K_r]:
            boxes.clear()
            gen_boxes()
        if k[pygame.K_a]:
            pos[0]-=2
        elif k[pygame.K_d]:
            pos[0]+=2
        if k[pygame.K_w]:
            pos[1]-=2
        elif k[pygame.K_s]:
            pos[1]+=2
        m = pygame.mouse.get_pos()
        m = (m[0]-pos[0], m[1]-pos[1])
        
        rays = []
        if m[0] != 0: 
            for angle in range(-angle_range, angle_range):
                angle = angle * 0.5
                a = atan((m[1]) / (m[0]))
                if m[0] < 0:
                    a += radians(180)
                a += radians(angle) 
                #print(a)
                rays.append(raycast(a, pos))
        
        screen.fill((0, 0, 0))
        for r in rays:
                    pygame.draw.line(screen, (255, 255, 255), pos, r, 5)
        for b in boxes:
            pygame.draw.rect(screen, (100, 100, 100), (b.x1, b.y1, b.w, b.h), 0)
        pygame.draw.circle(screen, (150, 150, 255), pos, 5, 0)
        pygame.display.flip()
    
def raycast(a, p):
    s = 0
    v = p
    while s != radius:
        v = (p[0] + cos(a) * s, p[1] + sin(a) * s)
        for b in boxes:
            if v[0] >= b.x1 and v[1] >= b.y1 and v[0] <= b.x2 and v[1] <= b.y2:
                return v
        s += step
    return v

if __name__ == "__main__":
    main()
