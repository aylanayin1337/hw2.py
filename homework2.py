day = int(input('Введите день рождения'))
month = int(input('Введите месяц рождения'))
if day > 31 and month <= 0:
    print('Неверно введённое число')
elif month > 12 and month <= 0:
    print('Неверно введённый месяц')
elif month == 2 and day >= 29:
    print('В Феврале до 29 дней')
elif (day >= 21 and month == 3) or (day <= 20 and month == 4):
    print('Овен')
elif (day >= 21 and month == 4) or (day <= 21 and month == 5):
    print('Телец')
elif (day >= 22 and month == 5) or (day <= 21 and month == 6):
    print('Близнецы')
elif (day >= 22 and month == 6) or (day <= 22 and month == 7):
    print('Рак')
elif (day >= 23 and month == 7) or (day <= 21 and month == 8):
    print('Лев')
elif (day >= 22 and month == 8) or (day <= 23 and month == 9):
    print('Дева')
elif (day >= 24 and month == 9) or (day <= 23 and month == 10):
    print('Весы')
elif (day >= 24 and month == 10) or (day <= 22 and month == 11):
    print('Скорпион')
elif (day >= 23 and month == 11) or (day <= 22 and month == 12):
    print('Стрелец')
elif (day >= 23 and month == 12) or (day <= 20 and month == 1):
    print('Козерог')
elif (day >= 21 and month == 1) or (day <= 19 and month == 2):
    print('Водолей')
elif (day >= 20 and month == 2) or (day <= 20 and month == 3):
    print('Водолей')
else:
    print('Неверно введённый формат, введите сначала число, затем месяц')