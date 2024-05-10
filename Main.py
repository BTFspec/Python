print(5, 8, 4)
             
n = None  # None - пустое значение; можно указать пустое значение если не знаем какое оно будет;
# в python не нужно писать тип данных в начале как это делали в C#;
# n = 5 int; n = "efsedsfse" str;
 
print(n)

"""
так комитят несколько строк
"""

# ctrl+k ctrl+c закоминить несколько строк
# ctrl+k ctrl+u убрать комиты

n ='s\'s' # \ слеш дает добавлять кавычки внутрь строки

print(type(n)) # type выводит в терминал тип данных 

a = 5
b = 5.45
c = 'Hello'
print (f"{a} - {b} - {c}") # интерполяция строк
print ("{} - {} - {}" .format(a,b,c)) # интерполяция строк

                            # ВВОД ДАННЫХ c терминала
print('Введите первую строку ')
a = int(input()) 
b = int(input('Введите вторую строку: '))
print(a,'+',b, '=',a + b)

# ПРИВЕДЕНИЕ ТИПОВ ДАННЫХ

c = 5.34
print(c)
print(type(c))
c = int(c)       # из float в int
print(c)
print(type(c))

c = 5.34
print(c)
print(type(c))
c = str(c)       # из float в str
print(c)
print(type(c))

a = 8.12332
b = 3.22121
print(round(a+b, 2)) #функция round определяем сколько цифр останется после запятой в данном случае указали 2;

#Сокращенные операции присваивания

# в C# внутри цикла for мы писали i++. Это было сокращение от i = i + 1.

iter = 2
iter += 3 # iter = iter + 3
iter -= 4 # iter = iter - 4
iter *= 5 # iter = iter * 5
iter /= 5 # iter = iter / 5
iter //= 5 # iter = iter // 5
iter %= 5 # iter = iter % 5
iter **= 5 # iter = iter ** 5

