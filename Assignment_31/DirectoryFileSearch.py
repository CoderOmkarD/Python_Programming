# this script is used to get the files with perticular extension from a folder using command line input
import os
import sys
import pathlib


def DirectoryFileSearch(DirName, FileExtension):

    if not os.path.exists(DirName):
        print("There is no such directory present in the folder")
        return

    print("Directory Name :", sys.argv[1])
    print("Extension :", sys.argv[2])

    for Dir, SubDirName, FileName in os.walk(DirName):
        Count = 0
        Files = []

        for file in FileName:
            ext = pathlib.Path(file).suffix
            if ext == FileExtension:
                Count = Count + 1
                Files.append(file)

        if Count == 0:
            print(f"There is no files with {FileExtension} Extension")
            return

        for file in Files:
            print(file)


def main():

    Border = "-" * 50
    print(Border)
    print("-----File Search System------")
    print(Border)

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This Script is used to :")
            print("1 :Get the Files from the Input Folder with given extension..")
            print("2 :By using the command line input ..")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as")
            print("ScriptName.py SourceDirectory  Extension")
            print("SourceDirectory : Name of Directory to Search From")
            print("Extension : The extension of the files you want to get")

        else:
            print("Enable to proceed as there is no such option..")
            print("please use --u or --h for more details...")

    # python Demo.py 5 Data
    elif len(sys.argv) == 3:
        print("Inside Projects Logic")

        DirectoryFileSearch(sys.argv[1], sys.argv[2])

    else:
        print("Invalid No.of Command line arguments...")
        print("Enable to proceed as there is no such option..")
        print("please use --u or --h for more details...")

    print(Border)
    print("----------Thank You For Using Our Script----------")
    print(Border)


if __name__ == "__main__":
    main()
