import numpy as np
number = np.random.randint(1, 100)
count = 0
while True:
    count+=1
    p_number = int(input('Number?:'))
    if p_number < number:
        print('more')
    elif p_number > number:
        print('less')
    else:
        print(f'Congrutulation! Try is {count}')
        break