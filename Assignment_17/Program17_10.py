def CountSumOfDigits(No):
    Sum = 0
    Digit = 0
    while No != 0:
        Digit = int(No % 10)

        Sum = Sum + Digit
        No = int(No / 10)
    return Sum


def main():
    print("Enter the number..:")
    Value = int(input())

    Ret = CountSumOfDigits(Value)

    print("Sum of digits is :", Ret)


if __name__ == "__main__":
    main()
