def ten_to_bin(x):
    if x == 0:
        return "0"
    if x == 1:
        return "1"

    # делим число на 2 и добавляем остаток от деления
    return ten_to_bin(x // 2) + str(x % 2)


if __name__ == "__main__":
    print(ten_to_bin(0))
