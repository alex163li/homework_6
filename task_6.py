# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

import random
numbers = [random.randint(0,100) for i in range(200)]
numbers = list(filter((lambda i: i[0]!=i[1]), enumerate(numbers)))
print(list(filter(lambda i: i[0]+i[1]%5, numbers)))