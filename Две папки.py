import os
import shutil
# os.listdir - выдать содержимое папки (один уровень)
# os.path.exists("D:\\test.txt") - проверка файла/папки на существование
# os.path.isfile("D:\\test.txt") - проверка на то что это именно файл
# print(os.path.getsize("D:\\test.txt")) - вычисление размера файла
path1 = 'C:\\Users\spams\OneDrive\Рабочий стол\Дворец'
path2 = 'C:\\Users\spams\OneDrive\Рабочий стол\Геленджик'
#функция, выдающая содержимое папки (до конца)
def walk (path, x):
    x = []
    for dirpath, dirnames, filenames in os.walk(path):
        # перебор папок
        for dirname in dirnames:
            x.append(dirname)
        # перебор файлов
        for filename in filenames:
            x.append(filename)
    return x
a = []
b = []
# вскрываем папку 1 и 2 и создаём 2 списка из имеющихся в них файлов и папок
a = walk (path1, a)
b = walk (path2, b)
print(a)
print(b)
# Пример копирования файла из Папки 1 в 2 и пример проверки размера файла
shutil.copy(os.path.join(path1,'Джакузи с уточками.txt'), path2)
os.path.getsize(os.path.join(path1,'Аквадискотека.txt'))

# проверяем каждый файл из Папки 1: есть ли файл с таким название в Папке 2 и имеет ли он такой же размер как в Папке 1?
# Если такой файл с таким же размером и названием есть, то ничего не делаем. Если нет, то копируем его в Папку 2
# Алгоритм не работает так как методы этих модулей не видят переменную i, а требуют конкретное название файла
for i in a:
    if i not in b or os.path.getsize(os.path.join(path1, i)) != os.path.getsize(os.path.join(path2, i)):
        shutil.copy(os.path.join(path1, i), path2) #добавляем недостающий файл во вторую папку
        

