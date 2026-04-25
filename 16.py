def ten_to_n(x, n):
    digits = "0123456789ABCDEF"

    if x < n:
        return digits[x]

    return ten_to_n(x // n, n) + digits[x % n]


if __name__ == "__main__":
    print("Двоичная система (n=2):")
    print(ten_to_n(10, 2))