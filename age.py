x = int(input('Enter the year of birth\n'))
y = int(input('Enter the month of birth\n'))
z = int(input('Enter the day of birth\n'))

from datetime import date

a = date.today()
b = date(x, y, z)
age = a - b

print('Attention!')
print('Since the day of your birth has passed')
print(age)

