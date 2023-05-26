# У больного в течение N дней измерялось давление. Найти количество дней, когда давление было самое низкое, и распечатать эти дни.
print('У больного в течение N дней измерялось давление. Найти количество дней, когда давление было самое низкое, и распечатать эти дни.')

n = int(input('Количество дней: '))
days = []
temperatures = []

for i in range(1, n + 1):
    x = int(input('Введите давление: '))
    days.append(i)
    temperatures.append(x)

day = days[temperatures.index(min(temperatures))]

print(f'Самое низкое давление было в день {day} = {min(temperatures)}')


