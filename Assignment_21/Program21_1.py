import threading


def CheckPrime(Arr):

    print("Prime Numbers Are : ")
    for j in range(len(Arr)):
        flag = True
        for i in range(2, int((Arr[j] / 2) + 1)):
            if Arr[j] % i == 0:
                flag = False
                break

        if flag == True:
            print(Arr[j], "\t", end="")
    print("")

def CheckNonPrime(Arr):
    print("Non Prime Numbers Are : ")
    for j in range(len(Arr)):
        flag = True
        for i in range(2, int((Arr[j] / 2) + 1)):
            if Arr[j] % i == 0:
                flag = False
                break

        if flag == False:
            print(Arr[j], "\t", end="")
    print("")

def main():
    Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 17, 19]

    Prime = threading.Thread(
        target=CheckPrime,
        args=(Data,)
    )
    NonPrime = threading.Thread(
        target=CheckNonPrime,
        args=(Data,)
    )

    Prime.start()
    NonPrime.start()

    Prime.join()
    NonPrime.join()


if __name__ == "__main__":
    main()
