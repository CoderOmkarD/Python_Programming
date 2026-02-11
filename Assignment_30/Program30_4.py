import os


def main():

    Data = [1024]

    print("Enter the Source FileName")
    SrcFileName = input()

    print("Enter the Destination FileName")
    DestFileName = input()

    if not (os.path.exists(SrcFileName)):
        print("There is no such file in the directory...")
        return -1

    srcobj = open(SrcFileName, "r")

    Destobj = open(DestFileName, "w")

    Data = srcobj.read()

    Destobj.write(Data)

    print(f"Contents of {SrcFileName} is get copied to {DestFileName}")


if __name__ == "__main__":
    main()
