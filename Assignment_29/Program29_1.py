import os


def IfExist(FileName):
    Ret = os.path.exists(FileName)
    return Ret


def main():
    
    print("Enter the File Name")
    FileName = input()

    Ret = IfExist(FileName)
    if Ret == True:
        print("File is Exists in the Current Directory")
    else:
        print("File is Not Exists in the Current Directory ")


if __name__ == "__main__":
    main()
