import os
import sys
import hashlib
import time


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


def DirectoryDuplicate(DirName):

    start_time = time.time()

    if not os.path.exists(DirName):
        print("There is no such Directory present...")
        return

    HashCodes = {}

    Duplicatesfile = []

    fobj = open("Log.txt", "w")

    fobj.write("Duplicate Files....\n")

    for root, subdir, files in os.walk(DirName):
        for file in files:
            file_path = os.path.join(root, file)
            hash = Calculate_Checksum(file_path)

            if not hash in HashCodes:

                HashCodes[hash] = file

            else:
                Duplicatesfile.append(file)
                fobj.write(file + "\n")

                os.unlink(file_path)

    end_time = time.time()

    TimeRequired = end_time - start_time
    print("Total Time required is : ", TimeRequired)


def main():

    Border = "-" * 50
    print(Border)
    print("-----Directory Remove Duplicates System With Time------")
    print(Border)

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This Script is used to :")
            print("1 :Get the Duplicates Files from the Directory..")
            print("2 : And create a log file named as log.txt")

            print("    Add the names of duplicate files into the log file")

            print("    And remove those duplicate files")

            print("4 :Calulate the time required to remove duplicates")

            print("3 :By using the command line input ..")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as")
            print("ScriptName.py SourceDirectory ")
            print("SourceDirectory : Name of Directory to delete duplicates files from")

        else:

            if os.path.isdir(sys.argv[1]):
                DirectoryDuplicate(sys.argv[1])

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
