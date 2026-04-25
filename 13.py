def odd_list(a, n):
    if n == 0:
        return []

    result = odd_list(a, n - 1)

    # проверяем n-й элемент (индекс n-1) на четность
    if a[n - 1] % 2 == 0:
        result.append(a[n - 1])

    return result


if __name__ == "__main__":
    print(odd_list([1, 2, 3, 4, 5], 5))
