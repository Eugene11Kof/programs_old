import os
import shutil
#пути к папкам 1 и 2
path1 = 'C:\\Users\spams\OneDrive\Рабочий стол\Дворец'
path2 = 'C:\\Users\spams\OneDrive\Рабочий стол\Геленджик'
a = os.listdir(path1) #файлы и папки внутри Папки 1

for i in a:
    if os.path.isfile(os.path.join(path1, i)): #Проверка на наличие файла в Папке 1
        if not os.path.isfile(os.path.join(path2, i)): # Проверка на отсутствие этого файла в Папке 2
            shutil.copy(os.path.join(path1, i), os.path.join(path2, i)) #Копирование и вставка файла в Папку 2
        if os.path.isfile(os.path.join(path2, i)) and os.path.getsize(os.path.join(path1, i)) != os.path.getsize(os.path.join(path2, i)): #если файл с таким названием есть и в Папке 2, то сверяем их размеры. Если неравны то заменяем файл.
            shutil.copy(os.path.join(path1, i), os.path.join(path2, i))
    if os.path.isdir(os.path.join(path1, i)) and not os.path.isdir(os.path.join(path2, i)): #то же самое с папками
        os.system(f'rd /S /Q {path2}\\{i}')
        shutil.copytree(os.path.join(path1, i), os.path.join(path2, i))

