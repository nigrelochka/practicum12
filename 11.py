def ind_maxlist(a):
    """
    рекурсивное нахождение индекса максимального элемента в списке
    возвращает кортеж (значение, индекс)
    """
    if len(a) == 1:
        return 0

    max_index_rest = ind_maxlist(a[1:])

    if a[0] >= a[max_index_rest + 1]:
        return 0
    else:
        return max_index_rest + 1


print(ind_maxlist([5]))
