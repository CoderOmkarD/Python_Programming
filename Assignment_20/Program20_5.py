import threading

lobj=threading.Lock()

def Display():
    with lobj:
        print("Thread ID :", threading.get_ident())
        print("Thread Name :", threading.current_thread())
        for i in range(1,51):
            print(i)

def DisplayReverse():
    with lobj:
        print("Thread ID :", threading.get_ident())
        print("Thread Name :", threading.current_thread())
        for i in range(50,0,-1):
            print(i)


def main():

    T1 = threading.Thread(target=Display)
    T2 = threading.Thread(target=DisplayReverse)
   

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("End of main")


if __name__ == "__main__":
    main()
