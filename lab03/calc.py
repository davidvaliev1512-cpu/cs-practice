def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def main():
    first = float(input())
    second = float(input())

    print(f"Сумма: {add(first, second)}")
    print(f"Разность: {subtract(first, second)}")


if __name__ == "__main__":
    main()
