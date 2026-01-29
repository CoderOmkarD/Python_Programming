import threading

lobj = threading.Lock()


def EvenList(Arr):
    Sum = 0
    with lobj:
        for i in range(len(Arr)):
            if Arr[i] % 2 == 0:
                Sum = Sum + Arr[i]
    print("Summation of Even : ", Sum)


def OddList(Arr):
    Sum = 0
    with lobj:
        for i in range(len(Arr)):
            if Arr[i] % 2 != 0:
                Sum = Sum + Arr[i]
    print("Summation of Odd : ", Sum)


def main():

    Value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    T1 = threading.Thread(target=EvenList, args=(Value,))
    T2 = threading.Thread(target=OddList, args=(Value,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("End of main")


if __name__ == "__main__":
    main()
