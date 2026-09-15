
from vpython import *
from time import *
import numpy as np


#Background
mRadius=0.5
wallThickness=0.5
roomWidth=20
roomDepth=20
roomHeight=20

scene.background = color.white

bottomwall=box(pos=vector(0,-roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white, opacity=0.2)
topwall=box(pos=vector(0,roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white, opacity=0.2)
backWall=box(pos=vector(0,0,-roomDepth/2),size=vector(roomWidth,roomHeight,wallThickness), color=color.white, opacity=0.2)
leftWall=box(pos=vector(-roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white, opacity=0.2)
rightWall=box(pos=vector(roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white, opacity=0.2)


#Balls
#b=np.array([ball1,ball2])

#ball1
marble=sphere(radius=mRadius,color=color.blue,make_trail=True)
dXi=.5
dXj=.5
dXk=.5
xPos=0
yPos=0
zPos=0
while True:
    rate(25)
    xPos=xPos+dXi
    yPos=yPos+dXj
    zPos=zPos+dXk
    Xrme=xPos+mRadius
    Xlme=xPos-mRadius
    Ytme=yPos+mRadius
    Ybme=yPos-mRadius
    Zfme=zPos+mRadius
    Zbme=zPos-mRadius
    Rwe=roomWidth/2-wallThickness/2
    Lwe=-roomWidth/2+wallThickness/2
    Bwe=-roomDepth/2+wallThickness/2
    Fwe=roomHeight/2+wallThickness/2
    Cwe=roomHeight/2-wallThickness/2
    if (Xrme>=Rwe or Xlme<=Lwe):
        dXi=dXi*(-1)
    if (Ytme>=Cwe or Ybme<=Bwe):
        dXj=dXj*(-1)
    if (Zfme>=Fwe or Zbme<=Bwe):
        dXk=dXk*(-1)
    marble.pos=vector(xPos,yPos,zPos)

# mRadius2=0.25


# marble=sphere(radius=mRadius2,color=color.red,make_trail=True)
# deltaX=.1
# xPos=0
# while True:
#     rate(25)
#     xPos=xPos+deltaX
#     Xrme=xPos+mRadius
#     Xlme=xPos-mRadius
#     Rwe=roomWidth/2-wallThickness/2
#     Lwe=-roomWidth/2+wallThickness/2
#     if (Xrme>=Rwe or Xlme<=Lwe):
#         deltaX=deltaX*(-1)
#     marble.pos=vector(xPos,0,0)

# mRadius2=0.5
# wallThickness2=0.5
# roomWidth2=20
# roomDepth2=20
# roomHeight2=20

# floor2=box(pos=vector(0,-roomHeight2/2,0),size=vector(roomWidth2,wallThickness2,roomDepth2), color=color.white)
# ceiling2=box(pos=vector(0,roomHeight2/2,0),size=vector(roomWidth2,wallThickness2,roomDepth2), color=color.white)
# backWall2=box(pos=vector(0,0,-roomDepth2/2),size=vector(roomWidth2,roomHeight2,wallThickness2), color=color.white)
# leftWall2=box(pos=vector(-roomWidth2/2,0,0),size=vector(wallThickness2,roomHeight2,roomDepth2), color=color.white)
# rightWall2=box(pos=vector(roomWidth2/2,0,0),size=vector(wallThickness2,roomHeight2,roomDepth2), color=color.white)
# marble2=sphere(radius=mRadius2,color=color.red,make_trail=True)
# deltaX=.1
# xPos=0
# while True:
#     rate(25)
#     xPos=xPos+deltaX
#     Xrme=xPos+mRadius
#     Xlme=xPos-mRadius
#     Rwe=roomWidth/2-wallThickness/2
#     Lwe=-roomWidth/2+wallThickness/2
#     if (Xrme>=Rwe or Xlme<=Lwe):
#         deltaX=deltaX*(-1)
#     marble.pos=vector(xPos,0,0)