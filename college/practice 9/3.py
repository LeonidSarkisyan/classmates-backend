# Известно количество жителей по N городам России. Распечатать название городов с количеством жителей равное среднему по России.
print('Известно количество жителей по N городам России. Распечатать название городов с количеством жителей равное среднему по России.')

cities_count = int(input('Введите количество городов: '))
cities = []
cities_population = []

for i in range(cities_count):
    print("Введите название города")
    city_name = input()
    cities.append(city_name)
    print("Введите количество населения")
    city_population = int(input())
    cities_population.append(city_population)

avg_population = sum(cities_population)/len(cities_population)
print(avg_population)

for index in range(len(cities_population)):
    if cities_population[index] == avg_population:
        print(cities[index])

