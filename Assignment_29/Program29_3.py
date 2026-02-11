import sys
import os


def GetCopy(FileName):

    Ret = os.path.exists(FileName)

    if Ret == False:
        print("There is no such file in the Directory")
        return
    
    fobj = open(FileName, "r")

    NewFobj = open("Copy.txt", "w")

    Buffer = fobj.read(1024)

    while len(Buffer) > 1:
        NewFobj.write(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()
    NewFobj.close()


def main():

    GetCopy(sys.argv[1])


if __name__ == "__main__":
    main()
