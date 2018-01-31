#Heather Stafford
#1/30/18
#fortuneTeller.py

color = input('Pick red or blue: ')
number = int(input('Pick a number from 1 - 4: '))

if color == 'blue' and number == 1:
    print('Someone will buy food for you.')
elif color == 'blue' and number == 2:
    print('You will have good luck for a week.')
elif color == 'blue' and number == 3:
    print('You will finish the quarter with an A.')
elif color == 'blue' and number == 4:
    print('You will live to be 100.')
elif color == 'red' and number == 1:
    print('Someone will do something nice for you today.')
elif color == 'red' and number == 2:
    print('You will not get a lot of sleep tonight.')
elif color == 'red' and number == 3:
    print('You will work your dream job.')
else:
    print('You will get lots of sleep tonight.')
