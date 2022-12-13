#!/usr/bin/env python3
import pygame
from math import cos, sin, radians, sqrt
from random import randint, triangular


def dist(p1, p2):
    return sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))

def gen(ds, d):
    for i in range(0, 20):
        ds[randint(0, 80), randint(0, 80)] = randint(5, 10)
            
    for x in range(0, 80):
        for y in range(0, 80):
            dst = 80
            for p in ds:
                f = dist((x, y), p)
                if f < dst :
                    dst = f
            d[(x, y)] = dst * 4


off = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def step(pl, d, end):
    c = pl[len(pl)-1]
    ps = []
    for o in off:
        ps.append((c[0] + o[0], c[1] + o[1]))
    i = (-1, -1)
    m = 1000000
    for p in ps:
        print(p)
        if p == end:
            pl.append(p)
            return
        if not p in d or p in pl:
            continue
        dst = dist(p, end) * 100 + 240 - d[p]*8
        #print(dst)
        if dst < m:
            m = dst
            i = p
    pl.append(i)

def main():
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    e = True
    ds = {}
    d = {}
    ap = []
    gen(ds, d)

    pl = []
    pl.append((0, 80))
    end = (80, 0)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()                
        
        screen.fill((100, 100, 100))

        for p in d:
            c = 4080/(d[p]+16)
            pygame.draw.rect(screen, (c, 0, (255-c)*0.2), (p[0]*10, p[1]*10, 10, 10), 0)


        
        if e:
            step(pl, d, end)
            if pl[len(pl)-1] == end:
                e = False
                i = 0
                for p in pl:
                    if i % 10 == 0:
                        ap.append((p[0]*10, p[1]*10))
                    i += 1
            for p in pl:
                pygame.draw.rect(screen, (255, 255, 255), (p[0]*10, p[1]*10, 10, 10), 0)

        else:
            pygame.draw.lines(screen, (255, 255, 255), False, ap, 4)
                
        pygame.display.flip()
        clock.tick(60)
        

if __name__ == "__main__":
    main()
