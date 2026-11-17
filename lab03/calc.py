def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    if second == 0:
        return None
    return first / second


def main():
    first = float(input())
    second = float(input())

    print(f"Сумма: {add(first, second)}")
    print(f"Разность: {subtract(first, second)}")
    print(f"Произведение: {multiply(first, second)}")

    quotient = divide(first, second)
    if quotient is None:
        print("На ноль делить нельзя.")
    else:
        print(f"Частное: {quotient}")


if __name__ == "__main__":
    main()
