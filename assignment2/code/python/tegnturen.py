#!/usr/bin/python
# vim: set fileencoding=utf8
from Graph1 import knuder, d
import pygame
from math import ceil, sqrt

tur = [8, 7, 5, 6]
#tur = [4, 5, 3, 2]
#tur = [1, 3, 5, 7, 6, 4, 2, 0]
# længde = 0.6

# Skriv turen der skal tegnes og regnes på hér:
#tur = [52,16,78,59,20,9,8,10,55,56,0,1,5,4,3,7,6,64,77,66,67,15,63,14,69,31,79,32,33,34,35,76,36,38,39,40,41,42,43,44,23,46,50,48,25,30,28,72,62,60]
# længde = 22.5947502248

# tur = [52,16,78,59,20,9,8,10,55,56,0,1,5,4,3,7,6,64,77,66,67,15,63,14,69,31,79,32,33,34,35,76,36,38,39,40,41,42,43,50,46,44,23,48,25,30,28,72,62,60]
# længde = 22.5962322985

# tur = [15,63,14,69,31,79,32,33,34,35,76,36,38,39,40,41,42,43,50,46,44,23,25,48,27,30,72,62,60,52,16,78,59,20,9,8,10,55,56,0,1,5,4,3,7,6,64,77,66,67]
# længde = 22.6214917199

# tur = [43,42,41,40,39,38,36,76,35,34,33,32,79,31,69,14,63,15,67,66,77,64,6,7,3,4,5,1,0,56,55,10,9,8,59,78,16,20,52,60,62,72,30,27,48,25,23,44,46,50]
# længde = 22.6341492122

# tur = [25,27,30,72,62,60,52,16,78,59,20,9,8,10,55,56,0,1,5,4,3,7,6,64,77,66,67,15,63,14,69,31,79,32,33,34,35,76,36,38,39,40,41,42,43,44,23,46,50,48]
# længde = 22.7578129624

# tur = [31,79,32,33,34,35,76,36,38,39,40,41,42,43,50,46,44,23,25,48,27,30,72,14,62,60,52,16,78,59,20,9,8,10,55,56,0,1,5,4,3,7,6,64,63,77,66,67,15,68]
# længde = 22.7596011376

# tur = [59,78,16,52,60,62,72,30,27,47,50,45,23,44,43,42,41,40,39,38,36,76,35,25,34,33,32,79,31,69,14,63,65,67,66,77,64,6,7,3,4,5,1,0,56,55,10,8,9,20]
# længde = 22.7917111669

# tur = [66,67,15,68,63,14,62,60,52,72,27,48,25,29,31,79,32,33,34,35,76,36,38,39,40,41,42,43,44,23,46,50,20,16,78,59,8,9,10,55,56,0,1,5,4,3,7,6,64,77]
# længde = 22.829822712112403

# tur = [51,27,30,25,48,50,46,23,44,43,42,41,40,39,38,36,76,35,34,33,32,79,31,69,70,14,63,15,67,66,77,64,6,7,4,3,0,56,55,54,11,8,58,18,19,16,78,1,2,60,62,52]
# længde = 22.8839506520

# tur = [60,52,16,78,59,20,9,8,54,55,56,0,1,2,4,3,7,6,64,77,66,67,15,63,14,68,31,79,32,33,34,35,76,36,38,39,40,41,42,43,44,23,46,50,48,25,30,28,72,62]
# længde = 22.8988494030

# tur = [67,15,68,63,14,62,60,52,72,27,48,25,29,31,79,32,33,34,35,76,36,38,39,40,41,42,43,44,23,46,50,20,16,59,8,11,10,55,56,57,0,1,5,4,3,7,6,64,77,66]
# længde = 22.957086842777795

# tur = [67,15,68,63,14,62,60,52,72,27,48,25,29,31,79,32,33,34,35,76,36,38,39,40,41,42,43,44,23,46,50,20,16,59,8,9,10,55,56,57,0,1,5,4,3,7,6,64,77,66]
# længde = 23.177498638379735

D = d

####
KNUDE_FARVE = (0, 0, 0)
KNUDE_SIZE = 5

STI_FARVE = (32, 189, 45)
STI_TYKKELSE = 3

D_FARVE = (206, 213, 242)
TEKST_FARVE = (0, 0, 0)

#######################
#######################

pygame.init()
window = pygame.display.set_mode((600, 600))

window.fill((255, 255, 255))

# Find grænserne for input
minX = minY = float('infinity')
maxX = maxY = float('-infinity')
for k in knuder:
    if k[0] < minX: minX = k[0]
    if k[1] < minY: minY = k[1]

    if k[0] > maxX: maxX = k[0]
    if k[1] > maxY: maxY = k[1]

minS = min(minX, minY) - D
maxS = max(maxX, maxY) + D
dS = maxS-minS

def knude(k): # Flyt knuden over på vores nye koordinatsystem
    (x, y) = knuder[k]
    return (25 + int(550 * (x - minS)/dS), 575 - int(550 * (y - minS)/dS))

def dist(i, j):
    (x1, y1) = knuder[i]
    (x2, y2) = knuder[j]
    return sqrt((x1-x2)**2 + (y1-y2)**2)

# Find længden på turen
length = 0
for i in range(0, len(tur)):
    length += dist(tur[i], tur[(i + 1)%len(tur)])
print "Turens længde er", length, "km"

pygame.display.set_caption('TCP - Esben & Sebastian - dist = ' + str(length) + 'km')

# Tegn d-dækningen
d_size = int(ceil(550 * D / dS))
for i in range(0, len(tur)):
    pygame.draw.circle(window, D_FARVE, knude(tur[i]), d_size)

# Tegn stierne
for i in range(0, len(tur)):
    pygame.draw.line(window, STI_FARVE, knude(tur[i]), knude(tur[(i+1)%len(tur)]), STI_TYKKELSE)

# Tegn knuderne
for k in range(0, len(knuder)):
    pygame.draw.circle(window, KNUDE_FARVE, knude(k), KNUDE_SIZE)

# Tegn labels på knuderne
font = pygame.font.Font(None, 17)
for k in range(0, len(knuder)):
    label = font.render(str(k), True, TEKST_FARVE)
    labelRect = label.get_rect()
    labelRect.midbottom = knude(k)
    labelRect.bottom -= 4
    window.blit(label, labelRect)

# Display the screen
pygame.display.flip()
pygame.image.save(window,'graph.png')

# Loop until quit is requested
stop = False
while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
