def numbers(x):
    if x < 10:
        print(x)
        return

    print(x % 10)

    numbers(x // 10)


if __name__ == "__main__":
    print("Вывод цифр числа 12345 в обратном порядке:")
    numbers(12345)