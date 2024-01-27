# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.
# Добавляем логирование и ввод с командной строки


import logging
import sys

logging.basicConfig(filename='rectangle.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class Rectangle:
    """
    Класс "Прямоугольник". Принимает геометрические значения сторон прямоугольника,
    чтобы, используя свои методы, вычислять периметр и площадь прямоугольника или квадрата
    """

    def __init__(self, a, b=None):
        self.a = a
        if b is None:
            self.b = a
        else:
            self.b = b

    def perimeter(self):
        logging.info("Calculating perimeter")
        return 2 * (self.a + self.b)

    def area(self):
        logging.info("Calculating area")
        return self.a * self.b

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            side_length1 = int(input("Please enter the width/length of the rectangle: "))
            side_length2 = int(input("Please enter the height of the rectangle: "))
        else:
            side_length1 = int(sys.argv[1])
            side_length2 = int(sys.argv[2]) if len(sys.argv) == 3 else None
        rect_1 = Rectangle(side_length1, side_length2)
        print(f"Perimeter: {rect_1.perimeter()}, Area: {rect_1.area()}")
    except ValueError as ve:
        print(f"Error: {ve}")
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.error(f"An unexpected error occurred: {str(e)}", exc_info=True)
