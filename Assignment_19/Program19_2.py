Multiplication = lambda a, b: a * b


def main():
    print("Enter two number  :")
    Value1 = int(input())
    Value2 = int(input())

    Ret = Multiplication(Value1, Value2)

    print("Multiplication is : ", Ret)


if __name__ == "__main__":
    main()
