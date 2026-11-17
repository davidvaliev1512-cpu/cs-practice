def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    return first / second


def main():
    first = float(input())
    second = float(input())

    print(f"Сумма: {add(first, second)}")
    print(f"Разность: {subtract(first, second)}")
    print(f"Произведение: {multiply(first, second)}")
    print(f"Частное: {divide(first, second)}")


if __name__ == "__main__":
    main()
