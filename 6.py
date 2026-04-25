def degree5(n):
    """
    определяет, является ли натуральное число n степенью числа 5.
    """
    if n == 1:
        return 0

    if n % 5 != 0:
        return -1

    prev_degree = degree5(n // 5)

    if prev_degree == -1:
        return -1

    return prev_degree + 1


if __name__ == "__main__":
    print(degree5(5))
print(5//5)
