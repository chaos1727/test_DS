import numpy as np

number = np.random.randint(0, 101)  # компьютер загадывает случайное число в пределах 0...100

def randomize(arg):                 # функция отгадывания числа, принимает на вход число от 0 до 100 и пытается его угадать
    first_number = 0                # самое минимальное число
    last_number = 100               # самое максимальное число
    mid_number = last_number // 2   # число посередине между минимальныи и максимальным числом
    count = 0                       # количество попыток
    while count < 21:               # цикл, не более 20 попыток
        count += 1                  # увеличение счетчика
        if mid_number == arg:
            return arg, count
        elif mid_number > arg:
            last_number = mid_number
            mid_number = (first_number + last_number) // 2
        elif mid_number < arg:
            first_number = mid_number
            mid_number = (first_number + last_number) // 2 
    
print(randomize(number))            # вызов функции отгадывания числа, возвращает кортеж (отгаданое число, использованое количество попыток)