#Heather Stafford
#1/31/18
#warmup3.py

num = int(input('Enter a number: '))

if num % 2 == 0 and num % 3 == 0:
    print(num,'is divisible by 2 and 3')
elif num % 3 == 0:
    print(num, 'is divisible by 3')
elif num % 2 == 0:
    print(num,'is divisible by 2')
else:
    print(num, 'is not divisible by 2 or 3')

