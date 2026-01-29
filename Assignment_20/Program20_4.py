import threading


def Small(Data):
    Count = 0
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread())
    for i in range(len(Data)):
        if Data[i] >= "a" and Data[i] <= "z":
            Count = Count + 1
    print("No .of lowercase characters :", Count)


def Capital(Data):
    Count = 0
    for i in range(len(Data)):
        if Data[i] >= "A" and Data[i] <= "Z":
            Count = Count + 1
    print("No .of uppercase characters :", Count)


def Digits(Data):
    Count = 0
    for i in range(len(Data)):
        if Data[i] >= "0" and Data[i] <= "9":
            Count = Count + 1
    print("No .of Digits  :", Count)


def main():

    print("Enter the string :")
    Value = input()

    T1 = threading.Thread(target=Small, args=(Value,))
    T2 = threading.Thread(target=Capital, args=(Value,))
    T3 = threading.Thread(target=Digits, args=(Value,))

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("End of main")


if __name__ == "__main__":
    main()
