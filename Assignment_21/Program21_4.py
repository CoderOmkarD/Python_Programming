import threading


def Summation(Arr):
    Sum = 0
    for i in range(len(Arr)):
        Sum = Sum + Arr[i]
    print("Summation is : ", Sum)


def Multiplication(Arr):
    Mult = Arr[0]
    for i in range(len(Arr)):
        Mult = Mult * Arr[i]
    print("Multiplication is :", Mult)


def main():
    Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 17, 19]

    Sum = threading.Thread(target=Summation, args=(Data,))
    Mult = threading.Thread(target=Multiplication, args=(Data,))

    Sum.start()
    Mult.start()

    Sum.join()
    Mult.join()


if __name__ == "__main__":
    main()
