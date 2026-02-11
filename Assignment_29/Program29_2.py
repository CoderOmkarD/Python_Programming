import os


def DisplayContent(FileName):
    Ret = os.path.exists(FileName)

    if Ret == False:
        print("There is no such file in the Directory")
        return

    fobj = open(FileName, "r")

    Data = fobj.read()

    print(Data)


def main():

    print("Enter the File Name")
    FileName = input()
    DisplayContent(FileName)


if __name__ == "__main__":
    main()
