def CountDigits(No):
    Count = 0

    while No != 0:
        # Count = Count + 1
        Count += 1
        No = int(No / 10)
    return Count


def main():
    print("Enter the number..:")
    Value = int(input())

    Ret = CountDigits(Value)

    print("No.of digits is :", Ret)


if __name__ == "__main__":
    main()
