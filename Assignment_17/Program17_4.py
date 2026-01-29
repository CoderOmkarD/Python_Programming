def Factorial(No):
    Sum = 0
    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i
    return Sum


def main():
    print("Enter the number..:")
    Value = int(input())
    Ret = Factorial(Value)
    print("Factorial is :", Ret)


if __name__ == "__main__":
    main()
