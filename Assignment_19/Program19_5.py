from functools import reduce


def CheckPrime(No):
    for i in range(2, int((No / 2) + 1)):
        if No % i == 0:
            return False
    return True


Square = lambda a: a * 2
Add = lambda a, b: a if a > b else b


def main():
    Data = list()
    print("Enter no.of elements :")
    Size = int(input())

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Input List :", Data)
    fData = list(filter(CheckPrime, Data))
    print("List After Filter :", fData)

    MData = list(map(Square, fData))
    print("List After Map :", MData)

    Ret = reduce(Add, MData)

    print("Add :", Ret)


if __name__ == "__main__":
    main()
