# импорты

# глобальные переменные
FIELD = ['' * 3 for _ in range(3)]


# функции
def field():
    global FIELD
    pass


# чтение .ini файла


# запуск суперцикла работы приложения и обработки общих команд
while True:
    command = input()

    if command in ('quit', "выход"):  # обработка выхода из приложения
        break

#Ввод имени игрока