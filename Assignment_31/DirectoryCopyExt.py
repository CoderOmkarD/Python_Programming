import os
import sys
import pathlib
import shutil


def DirectoryCopyExt(SourceDirName, DestDirName, Ext):

    if not os.path.exists(SourceDirName):
        print("There is no such directory present in the folder")
        return

    if os.path.exists(DestDirName):
        print("The FolderName That should newly Created is already exists:")
        print("Please Enter diffrent name of Copy folder")
        return

    os.mkdir(DestDirName)

    for dir, subdir, files in os.walk(SourceDirName):
        for file in files:

            fileExt = pathlib.Path(file).suffix
            if fileExt == Ext:
                filepath = os.path.join(dir, file)
                shutil.copy2(filepath, DestDirName)

    print("Data Copy Sucessfull....")


def main():

    Border = "-" * 50
    print(Border)
    print("-----Directory Copy System------")
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

        DirectoryCopyExt(sys.argv[1], sys.argv[2], sys.argv[3])

    else:
        print("Invalid No.of Command line arguments...")
        print("Enable to proceed as there is no such option..")
        print("please use --u or --h for more details...")

    print(Border)
    print("----------Thank You For Using Our Script----------")
    print(Border)


if __name__ == "__main__":
    main()
