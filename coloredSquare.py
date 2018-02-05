#Heather Stafford
#2/2/18
#coloredSquare.py

from random import randint
from ggame import *

num = randint(1,4)

if num == 1:
    red = Color(0xff0000,1)
    line = LineStyle(3,red)
    rectangle = RectangleAsset(100,100,line,red)
    
    Sprite(rectangle)
    myApp = App()
    myApp.run()
elif num == 2:
    green = Color(0x00FF00,1)
    line = LineStyle(3,green)
    rectangle = RectangleAsset(100,100,line,green)
    
    Sprite(rectangle)
    myApp = App()
    myApp.run()
elif num == 3:
    blue = Color(0x00BFFF,1)
    line = LineStyle(3,blue)
    rectangle = RectangleAsset(100,100,line,blue)
    
    Sprite(rectangle)
    myApp = App()
    myApp.run()
else:
    yellow = Color(0xFFFF00,1)
    line = LineStyle(3,yellow)
    rectangle = RectangleAsset(100,100,line,yellow)
    
    Sprite(rectangle)
    myApp = App()
    myApp.run()