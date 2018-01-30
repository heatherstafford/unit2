#Heather Stafford
#1/29/18
#unitConverter.py

print('1: kilometers to Miles')
print('2: Kilograms to Pounds')
print('3: Liters to Gallons')
print('4: Celsius to Fahrenheit')
num = input('Choose a number: ')
if num == 4:
    celcius = int(input('Enter Degrees in Celcius: '))
    fahrenheit = celcius * 1.8 + 32
    print(celcius,'degrees Celsius is', fahrenheit,'degres in Fahrenheit')