# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

new_string, find_str = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], "йцу"
if (new_string.count(find_str) >= 2):
    print(list(filter(lambda x: x[1] == find_str, enumerate(new_string)))[1][0])
else: print(-1)