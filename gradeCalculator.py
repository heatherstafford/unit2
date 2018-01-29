#Heather Stafford
#1/29/18
#gradeCalculator.py

grade = int(input('Enter your grade '))
if grade <= 59:
    print('You earned an F')
elif grade <= 69:
    print('You earned a D')
elif grade <= 79:
    print('You earned a C')
elif grade <= 89:
    print('You earned a B')
else:
    print('You earned an A')