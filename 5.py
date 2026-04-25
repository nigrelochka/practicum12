def mod_number(a, b):
    """
    рекурсивное нахождение остатка от деления a на b

    аргументы:
        a : делимое (натуральное число)
        b : делитель (натуральное число)
    """
    if a < b:
        return a

    return mod_number(a - b, b)


if __name__ == "__main__":
    print(mod_number(10, 3))
