from random import randrange
from numpy import loadtxt



# 1. Найти медиану массива с помощью сортировки MergeSort

# Merges two subarrays of arr[]. Слияние двух подмассивов массива arr
# First subarray is arr[l..m] Первый подмассив это arr[l..m]
# Second subarray is arr[m+1..r] Второй подмассив это arr[m+1..r]

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):


L[i] = arr[l + i]

for j in range(0, n2):
    R[j] = arr[m + 1 + j]

# Merge the temp arrays back into arr[l..r]
i = 0  # Initial index of first subarray
j = 0  # Initial index of second subarray
k = l  # Initial index of merged subarray

while i < n1 and j < n2:
    if L[i] <= R[j]:
        arr[k] = L[i]
        i += 1
    else:
        arr[k] = R[j]
        j += 1
    k += 1

# Copy the remaining elements of L[], if there
# are any
while i < n1:
    arr[k] = L[i]
    i += 1
    k += 1

# Copy the remaining elements of R[], if there
# are any
while j < n2:
    arr[k] = R[j]
    j += 1
    k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


# 2. Найти медиану массива с помощью процедуры рандомизированного выбора RSelect
def partition(x, pivot_index=0):
    i = 0
    if pivot_index != 0: x[0], x[pivot_index] = x[pivot_index], x[0]
    for j in range(len(x) - 1):
        if x[j + 1] < x[0]:
            x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
            i += 1
    x[0], x[i] = x[i], x[0]
    return x, i


def RSelect(x, k):
    if len(x) == 1:
        return x[0]
    else:
        xpart = partition(x, randrange(len(x)))
        x = xpart[0]  # partitioned array
        j = xpart[1]  # pivot index
        if j == k:
            return x[j]
        elif j > k:
            return RSelect(x[:j], k)
        else:
            k = k - j - 1
            return RSelect(x[(j + 1):], k)


# 3. Сформируем массивы с тестовыми примерами
# Тестовый пример №1
# 10 целых чисел, представляющих массив из 10 элементов, найти медиану
test1 = list(loadtxt('test1.txt', dtype='int'))
test2 = list(loadtxt('test2.txt', dtype='int'))

# Тест 1 - Найти медиану (то есть 5-й наименьший элемент)
n = len(test1)
median = n // 2 - 1
print(f"Исходный массив: {test1}")
mergeSort(test1, 0, n - 1)
print(f"Отсортированный массив: {test1}")
print(f"Медиана: {test1[median]}")
# print(RSelect(test1, median))

print('\n')

# Тест 2 - Найти медиану (т. е. статистику 50-го порядка)
n = len(test2)
median = n // 2 - 1
print(f"Исходный массив: {test2}")
start = time.time()  ## точка отсчета времени

mergeSort(test2, 0, n - 1)

end = time.time() - start  ## собственно время работы программы

print(f"Время: {end}")  ## вывод времени
print(f"Отсортированный массив: {test2}")
print(f"Медиана: {test2[median]}")
# print(RSelect(test2, median))

print('\n')
#
file = open("pi.txt", "r")
data = file.read()
data_into_list = data.replace('\n', ' ').split(' ')
data_into_list = [int(cell) for cell in data_into_list]
file.close()

print(f"Исходный массив: {data_into_list}")
n = len(data_into_list)
median = n // 2 - 1
mergeSort(data_into_list, 0, n - 1)
print(f"Отсортированный массив: {data_into_list}")
print(f"Медиана: {data_into_list[median]}")