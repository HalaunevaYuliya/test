print('Please, answer a few questions')
name = input('enter your frst name:\n')
surname = input('enter your surname:\n')
old = int(input('how old are you?\n'))
year = int(input('enter the year of birth\n'))
month = int(input('enter the month of birth\n'))
day = int(input('enter the day of birth\n'))

print('Your personal information:')
print(name, surname, old,'years old')
print('date of birth:',year,'/',month,'/',day)

print('Давайте продолжин на удобном для вас языке')
question_1 = input('почему вы решили попробовать себя в программировании?')
question_2 = input('чего вы хотите достичь через год?')
question_3 = input('а через 5 лет?')
print(question_1)
print(question_2)
print(question_3)
print('Спасибо, за уделенное время.')
