# В течение месяца измерялась T воздуха. Найти  дни месяца, когда T была ниже средней.
print('В течение месяца измерялась T воздуха. Найти  дни месяца, когда T была ниже средней.')

array = []
for i in range(1, 30 + 1):
    x = int(input('Температура воздуха: '))
    array.append((i, x))

summa = 0
for i in array:
    summa += i[1]

avg = summa / len(array)

for day, temperature in array:
    if temperature < avg:
        print(f'Температура была ниже средней в день {day} = {temperature}')



