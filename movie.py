#Heather Stafford
#1/29/18
#movie.py

age = int(input('Enter your age: '))

if age <= 8:
    print('You can watch G Rated movies')
elif age <= 12:
    print('You can watch PG Rated movies')
elif age <= 16:
    print('You can watch PG-13 Rated movies')
else:
    print('You can watch R Rated movies')