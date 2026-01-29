import threading

lobj =threading.Lock()

def DisplayEven():
    with lobj:
        print("Even Numbers :")
        for i in range(1, 21):
            if i % 2 == 0:
                print(i)


def DisplayOdd():
    with lobj:
        print("Odd Numbers :")
        for i in range(1, 21):
            if i % 2 != 0:
                print(i)


def main():
    T1 = threading.Thread(target=DisplayEven)
    T2 = threading.Thread(target=DisplayOdd)

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__ == "__main__":
    main()
