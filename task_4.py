# 4 - Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.

url_list = ['https://github.com/alex163li/homework_6', 
            'https://gb.ru/lessons/284811/homework', 
            'https://dzen.ru/?yredirect=true']
url_list = [i for i in map(lambda i: i.lstrip('https://').lstrip('www.'), url_list)]
print(list(map(lambda i: i[:i.find('/')] ,url_list)))