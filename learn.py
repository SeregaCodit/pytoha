"""
🔶 Задача 1: Обробка даних сенсорів квадрокоптера
Умова: Тобі надійшов список зчитаних векторів прискорення
 (зароляти випадкову кількіть від 10  до 50)
 (кожне значення кожного вектору потрібно зароляти у діапазоні 0 до 100) з IMU сенсора
 (у форматі (x, y, z) в одиницях G), і ти хочеш:

Нормалізувати кожен вектор (розрахувати його довжину та поділити всі компоненти на неї).

Заокруглити кожну компоненту до 3 знаків після коми.

Зберегти як список кортежів нормалізованих значень.

Вхідні дані:

acc_vectors = [
    (0.0, 1.0, 0.0),
    (0.5, 0.5, 0.707),
    (1.0, 1.0, 1.0),
    (0.0, 0.0, -1.0)
]
Підказка:

Напиши кастомну функцію normalize_vector(v) — обчислює нормалізований вектор.

Потім використай map() з lambda, щоб одразу округлити результат.


"""
import random
from math import sqrt

from numpy.lib.function_base import iterable

random.seed(42)

def get_length(vec:tuple) -> float:
    squared_vector = tuple(map(lambda x: x ** 2, vec))
    vec_sum = sum(squared_vector)
    length = sqrt(vec_sum)
    return length

def normalize_vector(vec:tuple, length:float):
    """
    Через цю функіую ми довжину ділимо на значення векторів
    :param vec: не нормалізований вектор
    :return: нормалізований вектор
    """
    # normalized = (length / vec[0], length / vec[1], length / vec[2])
    # for i in vec:
         # vec_1 = length / i
         # vec_2 = length / i
         # vec_3 = length / i

    # vec_list = list(vec)

    # for i in range(len(vec_list)):
    #     vec_list[i] /= length
    #     # print(vec_list[i])
    #     vec = tuple(vec_list)
    # print(vec)


    norm_vec = map(lambda x: round(x / length, 3), vec)
    return norm_vec

vectors = []


for i in range(4):
    vector = tuple(random.randint(1, 101) for j in range(3))
    length = get_length(vector)
    normalized_vector = tuple(normalize_vector(vector, length))
    vectors.append(normalized_vector)

print(vectors)
# print(vectors[0][0])
# print("v", vectors)



# vec_length = get_length(vectors[0])
# print(vec_length)
# normalized_vector = normalize_vector(vectors[0], vec_length)
# print(tuple(normalized_vector))
#
# length_list = map(get_length, vectors)
# normalize_vectors = map(normalize_vector, [vectors, 0])
# print(tuple(normalize_data), tuple(normalize_vectors))
