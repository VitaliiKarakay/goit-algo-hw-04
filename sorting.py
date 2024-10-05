import timeit
import random


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1


def timsort(array):
    return sorted(array)


def measure_time(sort_function, array):
    return timeit.timeit(lambda: sort_function(array.copy()), number=1)


sizes = [100, 1000, 10000]
results = {}

for size in sizes:
    arr = [random.randint(0, 10000) for _ in range(size)]

    insertion_time = measure_time(insertion_sort, arr)

    merge_time = measure_time(merge_sort, arr)

    timsort_time = measure_time(timsort, arr)

    results[size] = {
        'Insertion Sort': insertion_time,
        'Merge Sort': merge_time,
        'Timsort': timsort_time
    }

for size, times in results.items():
    print(f"Розмір масиву: {size}")
    for sort_alg, time_taken in times.items():
        print(f"{sort_alg}: {time_taken:.6f} секунд")
    print()
