#текущая дата
a = 2021 
b = 8
c = 25
#дата рождения
x = 1980 
y = 8
z = 25

if b == y and c == z:
    print(a - x)
elif (b - y) <= 0 and (c - z) < 0 or (z - c) <= 0 and (b - y) < 0:
    print(a - x - 1)
else:
    print(a - x)


# с учетом, что день рождения с 00:00 дня, следующего за днем рождения
##    if (b - y) <= 0 and (c - z) <= 0 or (z - c) <= 0 and (b - y) < 0:
##    print(a - x - 1)
##else:
##    print(a - x)  

# короткий вариант при наступлении ДР с 00:00 начала дня
##if (b - y) >= 0 and (c - z) >= 0 or (z - c) >= 0 and (b - y) > 0:
##    print(a - x)
##else:
##    print(a - x -1)
