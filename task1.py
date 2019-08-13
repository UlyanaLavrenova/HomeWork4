# Var 7
# Записать из файла А в файл В те строки, которые содержат только одно слово

# помещаем текст в строковую переменную a
a = 'А я не знал, что я расту\n\
Все время, каждый час.\n\
Я сел на стул —\n\
Но я расту,\n\
Расту, шагая в класс.\n\
Расту,\n\
Когда гляжу в окно,\n\
Расту,\n\
Когда сижу в кино,\n\
Когда светло,\n\
Когда темно,\n\
Расту,\n\
Расту я все равно.\n\
Идет борьба\n\
За чистоту,\n\
Я подметаю\n\
И расту.\n\
Сажусь я с книжкой\n\
На тахту,\n\
Читаю книжку\n\
И расту.\n\
Стоим мы с папой\n\
На мосту,\n\
Он не растет,\n\
А я расту.\n\
Отметку ставят мне\n\
Не ту,\n\
Я чуть не плачу,\n\
Но расту.\n\
Расту и в дождик,\n\
И в мороз,\n\
Уже я маму\n\
Перерос!'

# запись переменной а в файл А
with open("fileA.txt", "w") as fileA:
    fileA.write(a)


try:
    # открытие файла А в режиме чтения
    with open("fileA.txt", "r") as fileA:
        # открытие файла В в режиме записи
        with open("fileB.txt", "w") as fileB:
            # построчное чтение файла А
            for line in fileA.readlines():
                # если в строке файла А не встречаются пробелы, что значит, что там одно слово,
                # то эта строка записывается в файл В
                if line.count(' ') == 0:
                    fileB.write(line)
except FileNotFoundError:
    print("Файл A не найден")


try:
    # чтение файла В для проверки
    with open("fileB.txt", "r") as fileB:
        print("Содержимое файла В:")
        print(fileB.read() + "\n")
except FileNotFoundError:
    print("Файл В не найден")


try:
    # поиск самого длинного слова
    with open("fileB.txt", "r") as fileB:
        longer_word = ''
        for line in fileB.readlines():
            new_line = ''
            for symbol in [',', '.', '!', '?', '\n', ':']:
                if symbol in line:
                    new_line = line.replace(symbol, '')
            if len(new_line) > len(longer_word):
                longer_word = new_line
        print("Саммое длинное слово в файле В - '" + longer_word + "'")
except FileNotFoundError:
    print("Файл В не найден")