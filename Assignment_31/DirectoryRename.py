import os
import sys
import pathlib


def DirectoryRename(DirName, FileExtension, Renamer):

    if not os.path.exists(DirName):
        print("There is no such directory present in the folder")
        return

    print("Directory Name :", sys.argv[1])
    print("Extension :", sys.argv[2])

    for Dir, SubDirName, FileName in os.walk(DirName):
        Count = 0
        for file in FileName:
            ext = pathlib.Path(file).suffix

            if ext == FileExtension:

                file = os.path.join(Dir, file)

                FileWithoutExt = pathlib.Path(file).stem
                Count = Count + 1
                Newname = FileWithoutExt + Renamer
                newfile = os.path.join(Dir, Newname)

                os.rename(file, newfile)

        if Count == 0:
            print(f"There is no files with {FileExtension} Extension")
            return
        else:
            print(f"{Count} files changes to {FileExtension} to -> {Renamer}")


def main():

    Border = "-" * 50
    print(Border)
    print("-----File Renamer System------")
    print(Border)

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This Script is used to :")
            print("1 :Change the file extension..")
            print("2 :By using the command line input ..")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as")
            print("ScriptName.py SourceDirectory ExtensionOfFileToChange NewExtension")
            print("SourceDirectory : Name of Directory to Search From")
            print("Extension : The extension of the files you want to get")

        else:
            print("Enable to proceed as there is no such option..")
            print("please use --u or --h for more details...")

    # python Demo.py 5 Data
    elif len(sys.argv) == 4:
        print("Inside Projects Logic")

        DirectoryRename(sys.argv[1], sys.argv[2], sys.argv[3])

    else:
        print("Invalid No.of Command line arguments...")
        print("Enable to proceed as there is no such option..")
        print("please use --u or --h for more details...")

    print(Border)
    print("----------Thank You For Using Our Script----------")
    print(Border)


if __name__ == "__main__":
    main()
