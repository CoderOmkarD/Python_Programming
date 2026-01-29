import threading

Value=0

lobj=threading.Lock()

def Increment():
    with lobj:
        for i in range(1000):
            global Value
            Value=Value+1
            print(Value)



def main():
    T1=threading.Thread(target=Increment)
    T2=threading.Thread(target=Increment)

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__ == "__main__":
    main()
