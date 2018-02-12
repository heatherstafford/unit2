#Heather Stafford
#2/12/18
#quiz2.py

firstword = input('Enter a word: ')
secondword = input('Enter another word: ')

letters1 = int(len(firstword))
letters2 = int(len(secondword))

if letters1 == letters2 :
    print('They are the same length.')
elif letters1 > letters2:
    print('The first word is longer.')
else:
    print('The second word is longer.')

if 'p' in firstword and secondword or 'P' in firstword and secondword:
    print('Both words have p')
elif 'p' in firstword or 'P' in firstword:
    print('The first word has p')
elif 'p' in secondword or 'P' in secondword:
    print('The second word has p')
else:
    ('Neither words have p')

print('Enter 2 numbers that add up to 12')
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

if num1 + num2 == 12:
    print('correct')
else:
    print('incorrect')
