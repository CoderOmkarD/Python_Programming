def Minimum(No):

    Min = No[0]

    for i in range(len(No)):
        if No[i] < Min:
            Min = No[i]
            
    return Min


def main():

    print("Enter No.of  elements :")
    Value = int(input())

    Data = []

    print("Enter the elements :")
    for i in range(Value):
        A = int(input())
        Data.append(A)

    Ret = Minimum(Data)
    print("Minimum is :", Ret)


if __name__ == "__main__":
    main()
