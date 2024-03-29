from classes2d_shapes import Square, Rectangle, Circle, Triangle, Trapezoid, Rhomb, Shape


def main_menu() -> None:
    """ Вывод главного меню """
    print('1: Плоские фигуры\n'
          '2: Выход\n'
          f'Общее количество просмотренных фигур {Shape.count_shapes()}')


def next_menu(shapes: list) -> None:
    """ Вывод меню с фигурами """
    print('Выберите фигуру:')
    for i in shapes:
        print(i)


def print_info(shape: Shape) -> None:
    shape.show_info()


def create_2d_shape(index: str) -> None:
    """ Калькулятор плоских фигур """
    if index == '1':
        """Circle"""
        while True:
            try:
                radius = float(input('Введите значение радиуса окружности: '))
                print_info(Circle(radius))
                break
            except ValueError or TypeError as er:
                print(er)

    elif index == '2':
        """Rectangle"""
        while True:
            try:
                length = float(input('Введите значение длины прямоугльника: '))
                width = float(input('Введите значение ширины прямоугльника: '))
                print_info(Rectangle(width, length))
                break
            except ValueError or TypeError as er:
                print(er)
    elif index == '3':
        """Triangle"""
        while True:

            try:
                side1 = float(input('Введите значение первой стороны треугольника: '))
                side2 = float(input('Введите значение второй стороны треугольника: '))
                side3 = float(input('Введите значение трертьей стороны треугольника: '))

                if (side1 + side2 > side3) or (side1 + side3 > side2) or (side2 + side3 > side1):
                    print("Неверный значения сторон треугольника!")
                    continue

                print_info(Triangle(side1, side2, side3))
                break
            except ValueError or TypeError as er:
                print(er)
    elif index == '4':
        """Square"""
        while True:
            try:
                side = float(input('Введите значение длины стороны квадрата: '))
                print_info(Square(side))
                break
            except ValueError or TypeError as er:
                print(er)
    elif index == '5':
        """Trapezoid"""
        while True:
            try:
                big_foot = float(input('Введите значение большогое основания трапеции: '))
                small_foot = float(input('Введите значение маленького основания трапеции: '))
                side1 = float(input('Введите значение левой сторонй трапеции: '))
                side2 = float(input('Введите значение правой стороны трапеции: '))

                print_info(Trapezoid(big_foot, small_foot, side1, side2))
                break
            except ValueError or TypeError as er:
                print(er)
    elif index == '6':
        """Rhomb"""
        while True:
            try:
                diagonal1 = float(input('Введите значение первой диагонали ромба: '))
                diagonal2 = float(input('Введите значение второй диагонали ромба: '))

                print_info(Rhomb(diagonal1, diagonal2))
                break
            except ValueError or TypeError as er:
                print(er)
    else:
        print('Такой фигуры нет')


def main():
    _2D_SHAPES = ['1: Круг', '2: Прямоугольник', '3: Треугольник', '4: Квадрат', '5: Трапеция', '6: Ромб']

    while True:
        main_menu()
        answer_user = input()

        if answer_user == '1':
            next_menu(_2D_SHAPES)
            answer_user = input()
            create_2d_shape(answer_user)
            continue
        else:
            print('Пока!')
            exit()


if __name__ == "__main__":
    main()
