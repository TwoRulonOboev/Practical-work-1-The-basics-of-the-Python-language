# Задача 1: Все отрицательные элементы массива заменить на их абсолютную величину
def replace_negative_with_abs(arr):
    return [abs(x) if x < 0 else x for x in arr]

# Задача 2: Определить, является ли квадратный массив симметричным относительно своей главной диагонали
def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Задача 3: Вывести значение наибольшего элемента в списке и его индекс
def max_element_with_index(lst):
    max_element = max(lst)
    max_index = lst.index(max_element)
    return max_element, max_index

# Задача 4: Определить количество различных слов в тексте
def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

# Задача 5: Подсчет количества единиц товаров, приобретенных покупателями
def count_purchases(n, purchases):
    customer_purchases = {}
    for purchase in purchases:
        customer, item, quantity = purchase.split()
        quantity = int(quantity)
        if customer not in customer_purchases:
            customer_purchases[customer] = {}
        if item in customer_purchases[customer]:
            customer_purchases[customer][item] += quantity
        else:
            customer_purchases[customer][item] = quantity
    return customer_purchases


# Задание 1
arr = [-3, 2, -7, 4, 1]
result_1 = replace_negative_with_abs(arr)
print("Задание 1:", result_1)

# Задание 2
matrix = [
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
]
result_2 = is_symmetric(matrix)
print("Задание 2:", "Матрица симметрична" if result_2 else "Матрица несимметрична")

# Задание 3
lst = [5, 1, 8, 3, 8]
max_val, max_idx = max_element_with_index(lst)
print("Задание 3: Значение максимального элемента:", max_val, "Индекс:", max_idx)

# Задание 4
text = """3
Пример текста с несколькими словами. 
Слова повторяются в этом тексте."""
result_4 = count_unique_words(text)
print("Задание 4: Количество уникальных слов:", result_4)

# Задание 5
n = 3
purchases = [
    "Покупатель1 Товар1 3",
    "Покупатель2 Товар2 5",
    "Покупатель1 Товар2 2"
]
result_5 = count_purchases(n, purchases)
print("Задание 5: Покупки покупателей:", result_5)
