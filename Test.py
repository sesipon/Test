#1. Написать функцию, которая принимает на вход список целых чисел и возвращает новый список, содержащий
# только уникальные элементы из исходного списка.
def duplicate(lst)->list:
    return list(set(lst))

#2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум) и возвращает список всех
# простых чисел в заданном диапазоне
def list_of_numbers(a: int, b: int)->list:
    numbers = []
    for i in range(a, b+1):
        numbers.append(i)
    return numbers
#3. Создать класс Point, который представляет собой точку в двумерном пространстве. Класс должен иметь методы
# для инициализации координат точки, вычисления расстояния до другой точки, а также для получения и изменения
# координат.

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, point):
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return distance

    def get_coordinates(self):
        return self.x, self.y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

#4. Написать программу, которая сортирует список строк по длине, сначала по возрастанию,
# а затем по убыванию.

def sort_by_length(lst: list)->list:
    sorted_lst = sorted(lst, key=len)
    revers_lst = sorted(lst, key=len, reverse=True)

    return sorted_lst, revers_lst