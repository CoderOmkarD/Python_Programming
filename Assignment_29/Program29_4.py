import sys
import os


def GetCopy(FileName1, FileName2):

    Ret1 = os.path.exists(FileName1)
    Ret2 = os.path.exists(FileName2)

    if Ret1 == False or Ret2 == False:
        print("There is no such file in the Directory")
        return

    fobj1 = open(FileName1, "r")
    fobj2 = open(FileName2, "r")

    Buffer1 = fobj1.read()
    Buffer2 = fobj2.read()

    if Buffer1 == Buffer2:
        print("Successs")
    else:
        print("Failure")


def main():

    GetCopy(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
