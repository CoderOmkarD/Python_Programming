import os
import sys
import hashlib


def Calculate_Checksum(filename):

    hobj = hashlib.md5()

    fobj = open(filename, "rb")

    while True:
        Data = fobj.read(1024)

        if not Data:
            break
        else:
            hobj.update(Data)

    fobj.close()

    return hobj.hexdigest()


def DirectoryCheckSum(DirName):

    if not os.path.exists(DirName):
        print("There is no such Directory present...")
        return

    for root, subdir, files in os.walk(DirName):
        for file in files:
            file_path = os.path.join(root, file)
            hash = Calculate_Checksum(file_path)

            print(f"FileName : {file}\t File CheckSum : {hash}")


def main():

    Border = "-" * 50
    print(Border)
    print("-----Directory Get CheckSum System------")
    print(Border)

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This Script is used to :")
            print(
                "1 :Calculate the checksum of the each file from the given directory.."
            )
            print("2 :By using the command line input ..")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as")
            print("ScriptName.py SourceDirectory ")
            print(
                "SourceDirectory : Name of Directory to calculate the checksum of the file from"
            )

        else:

            if os.path.isdir(sys.argv[1]):
                DirectoryCheckSum(sys.argv[1])

            else:
                print("Enable to proceed as there is no such option..")
                print("please use --u or --h for more details...")

    else:
        print("Invalid No.of Command line arguments...")
        print("Enable to proceed as there is no such option..")
        print("please use --u or --h for more details...")

    print(Border)
    print("----------Thank You For Using Our Script----------")
    print(Border)


if __name__ == "__main__":
    main()
