#Heather Stafford
#2/5/18
#slope.py

x1 = int(input('x1 ='))
y1 = int(input('y1 ='))
x2 = int(input('x2 ='))
y2 = int(input('y2 ='))
if x2-x1 == 0:
    print('The slope is underfind')
else:
    slope = (y2-y1)/(x2-x1)
    print('The slope is',slope)
    print('The equation of the line is' )
