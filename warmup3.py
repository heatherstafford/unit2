#Heather Stafford
#1/31/18
#warmup3.py

num = int(input('Enter a number: '))

if num % 2 and num % 3 == 0:
    print(num,'is divisible by 2 and 3')
elif num % 3 == 0:
    print(num, 'is divisible by 3')
else num % 2 == 0:
    print(num,'is divisible by 2')

