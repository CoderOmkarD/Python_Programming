import os


def Frequency(FileName, Value):

    Ret = os.path.exists(FileName)

    Count = 0

    if Ret == False:
        print("There is no such file in the Directory")
        return

    fobj = open(FileName, "r")

    Data = fobj.read()

    NewString = Data.lower()

    NewStringX = NewString.split()

    Value = Value.lower()

    for word in NewStringX:
        if Value == word:
            Count = Count + 1

    print("Frequncy is :", Count)


def main():
    print("Enter the FileName :")
    FileName = input()
    print("Enter the String:")
    Value = input()
    Frequency(FileName, Value)


if __name__ == "__main__":
    main()
