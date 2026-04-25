def count(n):
    """
    рекурсивное вычисление количества цифр в натуральном числе
    """
    if n < 10:
        return 1

    return 1 + count(n // 10)


if __name__ == "__main__":
    print(count(123455))