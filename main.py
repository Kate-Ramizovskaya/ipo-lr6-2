import random#подключение библиотеки для рандом
height=random.randint(4, 8)#подбор значения с интервала
wight=random.randint(4, 8)#подбор значения с интервала
num=[-15, -4, -2, -7, 0, 3, 5, 12, 9]#список возможных значений
arr=[]#инициализация матрица/двумерного массива
for i in range(height):#цикл для определения высоты
    row=[]#инициализация итогового двумерного массива
    for j in range(wight):#цикл для широты
        row.append(random.choice(num))#заполнение рандомными значениями из допустимых для строк
    arr.append(row)#заполненеи рандомом для столбцов
print('Матрица: ')#вывода фразы "Матрица: "
for row in arr:#цикл для вывода
    for numb in row:#цикл для вывода
        print(f'{numb:4}', end='')# вывод матрицы и условия для форматирования
    print()#вывод матрицы
sum=0#инициализация переменной для дальнейшего подсчета
for row in arr:#цикл for для перебора матрицы
    for value in row:#цикл for для перебора матрицы
        if value%2!=0:#условие для отбора не четных
            sum+=numb#подсчет суммы
print("Сумма нечетных чисел: ", sum)#Вывод итоговой суммы
