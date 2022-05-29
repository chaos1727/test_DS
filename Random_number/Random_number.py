import numpy as np

number = np.random.randint(0, 101)

def randomize(arg):
    first_number = 0
    last_number = 100
    mid_number = last_number // 2
    count = 0
    while count < 20:
        count += 1
        if mid_number == arg:
            return arg, count
        elif mid_number > arg:
            last_number = mid_number
            mid_number = (first_number + last_number) // 2
        elif mid_number < arg:
            first_number = mid_number
            mid_number = (first_number + last_number) // 2 
    

print(randomize(number))
        