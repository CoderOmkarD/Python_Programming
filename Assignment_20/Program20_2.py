import threading

lobj = threading.Lock()


def EvenFactors(No):
    Sum = 0
    with lobj:
        for i in range(1, int(No / 2 + 1)):
            if i % 2 == 0:
                Sum = Sum + i
    print("Summation of Even Factors : ", Sum)


def OddFactors(No):
    Sum = 0
    with lobj:
        for i in range(1, int(No / 2 + 1)):
            if i % 2 != 0:
                Sum = Sum + i
    print("Summation of Odd Factors : ", Sum)


def main():

    print("Enter the Number :")
    Value = int(input())

    T1 = threading.Thread(target=EvenFactors, args=(Value,))
    T2 = threading.Thread(target=OddFactors, args=(Value,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("End of main")


if __name__ == "__main__":
    main()
