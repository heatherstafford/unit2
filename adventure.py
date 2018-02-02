#Heather Stafford
#2/2/18
#adventure.py

print('A bear is chaing you.')
print('You come to a river.')
choice1 = input('Do you cross the river?')
if choice1 == 'no':
    print('You try to climb a tree, but the bear knows how to climb faster and eats you.')
else:
    print('You swim accross the river, but a current carries you down stream.')
    print('You notice there is a water fall ahead.')
    choice2 = input('do you grab onto a near by tree?')
    if choice2 == 'no':
        print('You are pulled down the waterfall, and fall a very long way to your death.')
    else:
        print('The tree turns out to be a very large snake that eats you.')
        
        