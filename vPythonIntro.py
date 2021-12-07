from vpython import *
from time import *

mRadius= .75
wallThickness = .1
roomWidth = 15
roomDepth = 5
roomHeight = 10

floor = box(pos = vector(0, -roomHeight/2, 0), size = vector(roomWidth, wallThickness, roomDepth), color = color.white)
ceiling = box(pos = vector(0, roomHeight/2, 0), size = vector(roomWidth, wallThickness, roomDepth), color = color.white)
rightWall = box(pos = vector(roomWidth/2, 0, 0), size = vector(wallThickness, roomHeight, roomDepth), color = color.white)
leftWall = box(pos = vector(-roomWidth/2, 0, 0), size = vector(wallThickness, roomHeight, roomDepth), color = color.white)
backWall = box(pos = vector(0, 0, -roomDepth/2), size = vector(roomWidth, roomHeight, wallThickness), color = color.white)
marble = sphere(color = color.red, radius = mRadius)

deltaX = .1
xPos = 0

while True:
    rate(50)
    xPos= xPos + deltaX
    if xPos > roomWidth/2 or xPos < -roomWidth/2:
        deltaX = deltaX * (-1)
    marble.pos=vector(xPos, 0, 0)