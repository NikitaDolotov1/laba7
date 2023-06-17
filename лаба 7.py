from datetime import datetime

def decorator(func):
    def wrapper(distance):
        print("Время запуска функции", datetime.now())
        print("Расстояние", distance)
        print("Сумма", func(distance))

    return wrapper

@decorator
def taxi(distance):
    price = base + add * distance/140
    return round(price, 2)

distance = int(input("Введите дистанцию"))
base = 4
add = 0.25
taxi(distance)