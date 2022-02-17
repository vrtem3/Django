class OpenFile:
    def __init__(self, path, type):  # В конструктор объекта контекстного менеджера передаются два аргумент:
        # путь и тип открываемого файла (для записи, для чтения и т. д.)
        self.file = open(path, type)

    def __enter__(self):  # При входе в контекстный менеджер открывается файл
        return self.file  # и возвращается объект для работы с этим файлом

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()  # При выходе из контекстного менеджера файл закрывается


with OpenFile('hello.txt', 'wt') as f:
    f.write('Что-то пишем сначала!\n')

with OpenFile('hello.txt', 'at') as a:
    a.write('И продолжаем записывать!\n')


