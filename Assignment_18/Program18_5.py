from MarvellousNum import ChkPrime


def ListPrime(Data):
    Sum = 0
    for i in range(len(Data)):
        Ret = ChkPrime(Data[i])
        if Ret == True:
            Sum = Sum + Data[i]
    return Sum


def main():

    print("Enter Data.of  elements :")
    Value = int(input())

    Data = []

    print("Enter the elements :")
    for i in range(Value):
        A = int(input())
        Data.append(A)

    Ret = ListPrime(Data)
    print("Addition is :", Ret)


if __name__ == "__main__":
    main()
