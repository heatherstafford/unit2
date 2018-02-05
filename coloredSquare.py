#Heather Stafford
#2/2/18
#coloredSquare.py

from random import randint
from ggame import *


red = Color(0xff000,1)
line = LineStyle(3,red)
rectangle = RectangleAsset(100,100,line,red)
    
Sprite(rectangle)
myApp = App()
myApp.run()