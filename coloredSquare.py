#Heather Stafford
#2/2/18
#coloredSquare.py

from random import randint
from ggame import *

num = randint(1,4)

if num == 1:
    red = color(0xff000,1)
    line = LineStyle(3,red)
    retangle = RectangleAsset(100,100,line,red)
    
    Sprite(rectangle)
    myApp = App()