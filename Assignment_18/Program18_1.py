def Addition(No):
    Sum = 0
    for i in range(len(No)):
        Sum = Sum + No[i]
    return Sum


def main():
    print("Enter No.of  elements :")
    Value = int(input())
    Data = []
    print("Enter the elements :")
    for i in range(Value):
        A = int(input())
        Data.append(A)
    Ret = Addition(Data)
    print("Addition is :", Ret)


if __name__ == "__main__":
    main()
