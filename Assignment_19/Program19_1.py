Square = lambda a: 2**a


def main():
    print("Enter a number  :")
    Value = int(input())

    Ret = Square(Value)

    print("Square is : ", Ret)


if __name__ == "__main__":
    main()
