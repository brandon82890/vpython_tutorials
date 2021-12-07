#!/usr/bin/env python3
from vpython import *
from time import *

# Forgive the sloppy code, I am copying the instructor lol
# This is just for my own learning purposes

mRadius=2 
wallThickness=1
roomWidth=15
roomDepth=12
roomHeight=8

floor=box(pos=vector(0,-roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
ceiling=box(pos=vector(0,roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
backWall=box(pos=vector(0,0,-roomDepth/2),size=vector(roomWidth,roomHeight,wallThickness), color=color.white)
leftWall=box(pos=vector(-roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
rightWall=box(pos=vector(roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
marble=sphere(radius=mRadius,color=color.red)

deltaX=.1
deltaY=.1
deltaZ=.1


xPos=0
yPos=1
zPos= -1

while True:
    rate(25)
    xPos=xPos+deltaX
    yPos=yPos+deltaY
    zPos=zPos+deltaZ

    Xrme=xPos+mRadius
    Xlme=xPos-mRadius
    Ytme=yPos+mRadius
    Ybme=yPos-mRadius
    Zbme=zPos-mRadius
    Zfme=zPos+mRadius

    Rightwe=roomWidth/2-wallThickness/2
    Leftwe=-roomWidth/2+wallThickness/2
    Cielingwe=roomHeight/2-wallThickness/2
    Floorwe=-roomHeight/2+wallThickness/2
    Backwe=-roomDepth/2+wallThickness/2
    Frontwe=roomDepth/2-wallThickness/2

    if (Xrme>=Rightwe or Xlme<=Leftwe):
        deltaX=deltaX*(-1)
    
    if (Ytme>=Cielingwe or Ybme<=Floorwe):
        deltaY=deltaY*(-1)
    
    if (Zfme>=Frontwe or Zbme<=Backwe):
        deltaZ=deltaZ*(-1)
    
    marble.pos=vector(xPos,yPos,zPos)