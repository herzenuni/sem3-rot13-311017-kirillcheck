# Шахов Кирилл 
# Задание - На основе кода с выполнением предыдущего задания  
# реализуйте получение JSON с удаленного хоста и красивый вывод информации на экран. 
def rot13(s):   """ сдвиг на нужную позицию (тут на 13) """
    result = ""

    for v in s:
        c = ord(v)

        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13

        result += chr(c)
    return result

def rot13_file(file_name):   """ Открытие файла в режиме чтения """
    try:
        file = open(file_name, 'r')
    except:
        print("Ошибка открытия файла")
        return

    try:
        data = file.read()
    except:
        print("Ошибка считывания файла")
        return
    finally:
        file.close()

    file = open(file_name, 'w')  """ Запись ответа """

    try:
        file.write(rot13(data))
    except:
        print("Ошибка Записи")
        return
    finally:
        file.close()

    print("Зашифрованный файл")


if __name__ == "__main__":

    menu = """
    1. Поработаем в консоли
    2. Поработаем в файле
    3. Драпаем (выход)
    
       ВЫБИРАЙ...
    """
    while True:
        while True:
            try:
                choice = int(input(menu))
                if choice == 1 or choice == 2 or choice == 3:
                    break
            except:
                print("что-то пошло не так - ошибка вывода")

        if choice == 1:
            print("Итог :", rot13(input("Введите строку :")))
        elif choice == 2:
            rot13_file(input("Выш файл (закодированный) :"))
        elif choice == 3:
            break
