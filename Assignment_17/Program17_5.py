def CheckPrime(No):

    for i in range(2, int(No / 2 + 1)):
        if No % i == 0:
            return False
            break
    return True


def main():
    print("Enter the number..:")
    Value = int(input())
    Ret = CheckPrime(Value)
    if Ret == True:
        print("It is prime Number")
    else:
        print("It is not a prime number")


if __name__ == "__main__":
    main()
