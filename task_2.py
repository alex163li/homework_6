# 2- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random, math
def enter_rndlist_size ():
    n_list = [(random.randint(1,21)) for i in range(int(input('Введите размер списка: ')))]
    return n_list

n_list = enter_rndlist_size()
print(n_list)

lambda_map_list = list(map(lambda i: n_list[i]*n_list[(-1-i)], [i for i in range(math.ceil(len(n_list)/2))]))
print(lambda_map_list)