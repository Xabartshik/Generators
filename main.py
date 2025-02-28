import sys
import module as m

def print_help():
    print("""
    Эта программа запускает генераторы с заданным числом шагов.

    Использование:
        python script.py [номер_генератора] число_шагов

    Если указан только один аргумент (число_шагов), запускаются все генераторы.
    Если указаны два аргумента (номер_генератора и число_шагов), запускается только указанный генератор.

    Примеры:
        python main.py 10          # Запуск всех генераторов с 10 шагами
        python main.py 3 10        # Запуск только генератора G3 с 10 шагами
    """)

def run_generator(gen_id, N):
    match gen_id:
        case 1:
            gen = m.G1(N)
        case 2:
            gen = m.G2(N)
        case 3:
            gen = m.G3(N)
        case 4:
            gen = m.G4(N)
        case 5:
            gen = m.G5(N)
        case 6:
            gen = m.G6(N)
        case 7:
            gen = m.G7(N)
        case 8:
            gen = m.G8(N)
        case 9:
            gen = m.G9(N)
        case _:
            print(f"Генератор G{gen_id} не найден.")
            return

    print(f"Значения из генератора G{gen_id}:")
    for value in gen:
        print(value)
    print()  # Пустая строка для разделения

def main():
    args = sys.argv[1:]  # Игнорируем первый аргумент (имя скрипта)
    # Вывод справки
    if not args:
        print_help()
        return

    if len(args) == 1:
        # Запуск всех генераторов
        try:
            N = int(args[0])
            for gen_id in range(1, 10):
                run_generator(gen_id, N)
        except ValueError:
            print("Ошибка: число шагов должно быть целым числом.")
    elif len(args) == 2:
        # Запуск конкретного генератора
        try:
            gen_id = int(args[0])
            N = int(args[1])
            run_generator(gen_id, N)
        except ValueError:
            print("Ошибка: номер генератора и число шагов должны быть целыми числами.")
    else:
        print("Неверное количество аргументов.")
        print_help()

if __name__ == '__main__':
    main()