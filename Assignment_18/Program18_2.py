def Maximum(No):

    Max = No[0]

    for i in range(len(No)):
        if No[i] > Max:
            Max = No[i]
            
    return Max


def main():

    print("Enter No.of  elements :")
    Value = int(input())

    Data = []

    print("Enter the elements :")
    for i in range(Value):
        A = int(input())
        Data.append(A)

    Ret = Maximum(Data)
    print("Maximum is :", Ret)


if __name__ == "__main__":
    main()
