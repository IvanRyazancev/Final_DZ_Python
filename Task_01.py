# Задача 1

# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# Добавляем логирование и ввод с командной строки


import logging

logging.basicConfig(filename='sorter.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


def sorter(numbers):
    n = len(numbers)
    try:

        for i in range(n):
            for j in range(0, n - i - 1):
                if numbers[j] > numbers[j + 1]:
                    logging.info(f"Swapping {numbers[j]} and {numbers[j + 1]}")
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                    logging.info(f"Current state: {numbers}")
        return numbers
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}", exc_info=True)


if __name__ == '__main__':
    try:
        input_numbers = input("Please enter a list of numbers separated by spaces: ")
        input_numbers = list(map(int, input_numbers.split()))
        result = sorter(input_numbers)
        print(result)
    except ValueError as ve:
        print(f"Error: {ve}")
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.error(f"An unexpected error occurred: {str(e)}", exc_info=True)
