import os

def main():

    print("Enter the FileName")

    Count = 0

    FileName = input()

    if not (os.path.exists(FileName)):
        print("There is no such file in the directory...")
        return -1

    fobj = open(FileName, "r")


    for Lines in fobj:
        Count = Count + 1

    print("No.of lines is : ", Count)

if __name__ == "__main__":
    main()

