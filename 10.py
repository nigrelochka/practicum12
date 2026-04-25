def maxlist(a):
    """
    рекурсивное нахождение максимального элемента в списке целых чисел.
    """
    if len(a) == 1:
        return a[0]

    # сравниваем первый элемент с максимумом остальной части списка
    max_rest = maxlist(a[1:])

    if a[0] > max_rest:
        return a[0]
    else:
        return max_rest


if __name__ == "__main__":
    print(maxlist([5]))
