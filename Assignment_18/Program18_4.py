def CalculateFrequency(Data, No):
    Count = 0
    for i in range(len(Data)):
        if Data[i] == No:
            Count = Count + 1

    return Count


def main():

    print("Enter Data.of  elements :")
    Value = int(input())

    Data = []

    print("Enter the elements :")
    for i in range(Value):
        A = int(input())
        Data.append(A)

    print("Enter the element to find the frequency :")
    Num = int(input())

    Ret = CalculateFrequency(Data, Num)
    print("Frequency is :", Ret)


if __name__ == "__main__":
    main()
