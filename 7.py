def nod(a, b):
    """
    рекурсивное вычисление наибольшего общего делителя чисел a и b
    Используется алгоритм Евклида.
    """
    if b == 0:
        return a

    return nod(b, a % b)


if __name__ == "__main__":
    print(nod(8, 0))
print(25%15)
