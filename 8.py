def fib(k):
    if k == 1 or k == 2:
        return 1

    # F(k) = F(k-1) + F(k-2)
    return fib(k - 1) + fib(k - 2)


if __name__ == "__main__":
    print(fib(1))

