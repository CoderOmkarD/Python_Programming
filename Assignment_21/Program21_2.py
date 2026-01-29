import threading


def GetMaximum(Arr):
    Max = Arr[0]
    for i in range(len(Arr)):
        if Arr[i] > Max:
            Max = Arr[i]
    print("Maximum number is : ", Max)


def GetMinimum(Arr):
    Min = Arr[0]
    for i in range(len(Arr)):
        if Arr[i] < Min:
            Min = Arr[i]
    print("Minimum number is : ", Min)


def main():
    Data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 17, 19]

    Max = threading.Thread(target=GetMaximum, args=(Data,))
    Min = threading.Thread(target=GetMinimum, args=(Data,))

    Max.start()
    Min.start()

    Max.join()
    Min.join()


if __name__ == "__main__":
    main()
