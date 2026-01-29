from functools import reduce

Even = lambda a: a % 2 == 0
Square = lambda a: a * a
Add = lambda a, b: a + b


def main():
    Data = list()
    print("Enter no.of elements :")
    Size = int(input())

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Input List :", Data)
    fData = list(filter(Even, Data))
    print("List After Filter :", fData)

    MData = list(map(Square, fData))
    print("List After Map :", MData)

    Ret = reduce(Add, MData)

    print("Add :", Ret)


if __name__ == "__main__":
    main()
