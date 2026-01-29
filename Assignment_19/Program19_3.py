from functools import reduce

GreaterThanSeventy = lambda a: a >= 70
IncreaseBy10 = lambda a: a + 10
Mult = lambda a, b: a * b


def main():
    Data = list()
    print("Enter no.of elements :")
    Size = int(input())

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Input List :", Data)
    fData = list(filter(GreaterThanSeventy, Data))
    print("List After Filter :", fData)

    MData = list(map(IncreaseBy10, fData))
    print("List After Map :", MData)

    Ret = reduce(Mult,MData)

    print("Mult :", Ret)


if __name__ == "__main__":
    main()
