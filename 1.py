def pownum(a, n):
    """
    рекурсивное вычисление степени a^n, где a - вещественное число, n - натуральное число
    """
    if n == 0:
        return 1

    return a * pownum(a, n - 1)


print(pownum(2, 3))
