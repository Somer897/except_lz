import pandas as pd
from pandas.errors import EmptyDataError

#Чтение файла
#цикл идет, пока не ввести правильную ссылку
while True:
    try:

        link = str(input('Введите ссылку на файл: '))
        file = pd.read_csv(link)

    except FileNotFoundError:   
                                 #проверить на ноуте Permission / asdirectory
        print("Файл не найден, попробуйте ещё раз")    
        
    except PermissionError:

        print('Нет доступа в файл')
        break

    except EmptyDataError:
        print('Файл пустой')
        break

    else:
        break


while True:
    try:
        column = str(input('Введите название изучаемого столбца: '))
        column1 = file[column]
    except KeyError:
        print('Столбец не найден')
    else:
        print('Столбец существует')
    finally:
        try:
            choose = int(input('Хотите продолжить или посмотреть столбцы? (1-продолжение 2-столбцы)'))
            if choose != 1:
                break
        except ValueError:
            break
if choose == 2:
    print(file.columns)


